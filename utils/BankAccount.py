import json


class BankAccount:
    """Банковский счет"""

    def __init__(self, operations_file):
        self.operations_file = operations_file
        self.get_executed_transactions()

    def get_executed_transactions(self):
        """получить выполненные операции"""
        executed_transactions = []
        with open(self.operations_file) as file:
            orders = json.load(file)

        for order in orders:
            # фильтрация по наличию свойства state
            if 'state' in order:
                # фильтрация по state = EXECUTED
                if order['state'] == 'EXECUTED':
                    executed_transactions.append(order)
        # обратная сортировка по времени
        sorted_executed_transactions = sorted(executed_transactions, key=lambda x: x['date'], reverse=True)
        return sorted_executed_transactions

    def get_last_executed_transactions(self, order_count=5):
        """получить последние операции"""
        executed_transactions = self.get_executed_transactions()
        last_order_list = []
        order_len = len(executed_transactions)
        if order_len < 5:
            order_count = order_len

        for index in range(order_count):
            order = executed_transactions[index]
            if 'Открытие вклада' in order['description']:
                last_order = self.__parse_deposit_opening_info(order)
            elif 'Перевод' in order['description']:
                last_order = self.__parse_money_order_info(order)
            else:
                continue
            last_order_list.append(last_order)
        return last_order_list

    def __parse_deposit_opening_info(self, transaction):
        """парсинг открытия счета"""
        date = self.__format_date(transaction['date'])
        to_name = self.__format_to_name(transaction['to'])
        return [
            f"{date} {transaction['description']}",
            to_name
        ]

    def __parse_money_order_info(self, order):
        """парсинг перевода"""
        # время
        date = self.__format_date(order['date'])
        # from
        from_name_list = order['from'].split()
        # банковский счет
        bank_acc_from = from_name_list[-1]
        bank_acc_from_list = [bank_acc_from[index:index + 4] for index in range(0, len(bank_acc_from), 4)]
        bank_acc_from = f"{bank_acc_from_list[0]} {bank_acc_from_list[1][:2]}** **** {bank_acc_from_list[-1]}"
        # from
        from_name_list.pop()
        from_name = ' '.join(from_name_list) + ' ' + bank_acc_from
        # to
        to_name = self.__format_to_name(order['to'])
        return [
            f"{date} {order['description']}",
            f"{from_name} -> {to_name}",
            f"{order['operationAmount']['amount']} {order['operationAmount']['currency']['name']}"
        ]

    @staticmethod
    def __format_date(time):
        """форматировать время"""
        time_list = time[:10].split('-')
        time_list = time_list[::-1]
        return '.'.join(time_list)

    @staticmethod
    def __format_to_name(to_name_str):
        """форматировать получателя"""
        to_name_list = to_name_str.split()
        bank_account = '**' + to_name_list[1][-4:]
        return f"{to_name_list[0]} {bank_account}"

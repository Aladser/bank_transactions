import json


class BankAccount:
    """Банковский счет"""

    def __init__(self, transactions_file):
        self.transactions_file = transactions_file
        self.get_executed_transactions()

    def get_executed_transactions(self):
        """получить выполненные операции"""
        executed_transactions = []
        with open(self.transactions_file) as file:
            transactions = json.load(file)

        for transaction in transactions:
            # фильтрация по наличию свойства state
            if 'state' in transaction:
                # фильтрация по state = EXECUTED
                if transaction['state'] == 'EXECUTED':
                    executed_transactions.append(transaction)
        # обратная сортировка по времени
        sorted_executed_transactions = sorted(executed_transactions, key=lambda x: x['date'], reverse=True)
        return sorted_executed_transactions

    def get_last_executed_transactions(self, transaction_count=5):
        """получить последние операции"""
        executed_transactions = self.get_executed_transactions()
        last_transaction_list = []
        transaction_list_len = len(executed_transactions)
        if transaction_list_len < 5:
            transaction_count = transaction_list_len

        for index in range(transaction_count):
            transaction = executed_transactions[index]
            if 'Открытие вклада' in transaction['description']:
                last_transaction = self.__parse_deposit_opening_info(transaction)
            elif 'Перевод' in transaction['description']:
                last_transaction = self.__parse_money_order_info(transaction)
            else:
                continue
            last_transaction_list.append(last_transaction)
        return last_transaction_list

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

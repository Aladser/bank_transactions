import json


def get_executed_money_orders(json_file):
    """получить выполненные переводы"""
    executed_orders = []
    with open(json_file) as file:
        orders = json.load(file)

    for order in orders:
        # фильтрация по наличию свойства state
        if 'state' in order:
            # фильтрация по state = EXECUTED и типу Перевод
            if order['state'] == 'EXECUTED' and 'from' in order:
                executed_orders.append(order)
    # обратная сортировка по времени
    sorted_executed_orders = sorted(executed_orders, key=lambda x: x['date'], reverse=True)
    return sorted_executed_orders


def get_last_executed_money_orders(executed_operations, operation_count=5):
    """получить последние переводы"""
    last_order_list = []
    order_len = len(executed_operations)
    if order_len < 5:
        operation_count = order_len

    for i in range(operation_count):
        operation = executed_operations[i]
        description = operation['description']
        # время
        time_list = operation['date'][:10].split('-')
        time_list = time_list[::-1]
        time = '.'.join(time_list)
        # from
        from_name_list = operation['from'].split()
        # банковский счет
        bank_acc_from = from_name_list[-1]
        bank_acc_from_list = [bank_acc_from[i:i + 4] for i in range(0, len(bank_acc_from), 4)]
        bank_acc_from = f"{bank_acc_from_list[0]} {bank_acc_from_list[1][:2]}** **** {bank_acc_from_list[-1]}"
        # from
        from_name_list.pop()
        from_name = ' '.join(from_name_list) + ' ' + bank_acc_from
        # to
        to_name_list = operation['to'].split()
        bank_acc_to = '**' + to_name_list[-1][-4:]
        to_name_list.pop()
        to_name = f"{' '.join(to_name_list)} {bank_acc_to}"
        # money
        # итоговый массив одной операции
        last_order = [
            f"{time} {description}",
            f"{from_name} -> {to_name}",
            f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
        ]

        last_order_list.append(last_order)
    return last_order_list

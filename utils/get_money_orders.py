import json


def get_executed_transactions(json_file):
    """получить выполненные переводы"""
    executed_orders = []
    with open(json_file) as file:
        orders = json.load(file)

    for order in orders:
        # фильтрация по наличию свойства state
        if 'state' in order:
            # фильтрация по state = EXECUTED и типу Перевод
            if order['state'] == 'EXECUTED':
                executed_orders.append(order)
    # обратная сортировка по времени
    sorted_executed_orders = sorted(executed_orders, key=lambda x: x['date'], reverse=True)
    return sorted_executed_orders


def get_last_executed_transactions(executed_orders, order_count=5):
    """получить последние операции"""
    last_order_list = []
    order_len = len(executed_orders)
    if order_len < 5:
        order_count = order_len

    for i in range(order_count):
        order = executed_orders[i]
        if 'Открытие вклада' in order['description']:
            last_order = get_deposit_opening_info(order)
            last_order_list.append(last_order)
            continue

        description = order['description']
        # время
        date = format_date(order['date'])
        # from
        from_name_list = order['from'].split()
        # банковский счет
        bank_acc_from = from_name_list[-1]
        bank_acc_from_list = [bank_acc_from[i:i + 4] for i in range(0, len(bank_acc_from), 4)]
        bank_acc_from = f"{bank_acc_from_list[0]} {bank_acc_from_list[1][:2]}** **** {bank_acc_from_list[-1]}"
        # from
        from_name_list.pop()
        from_name = ' '.join(from_name_list) + ' ' + bank_acc_from
        # to
        to_name = format_to_name(order['to'])
        # сумма перевода
        last_order = [
            f"{date} {description}",
            f"{from_name} -> {to_name}",
            f"{order['operationAmount']['amount']} {order['operationAmount']['currency']['name']}"
        ]

        last_order_list.append(last_order)
    return last_order_list


def get_deposit_opening_info(transaction):
    """парсинг открытия счета"""
    date = format_date(transaction['date'])
    description = transaction['description']
    to_name = format_to_name( transaction['to'])
    return [
        f"{date} {description}",
        to_name
    ]


def format_date(time):
    """форматировать время"""
    time_list = time[:10].split('-')
    time_list = time_list[::-1]
    return '.'.join(time_list)


def format_to_name(to_name_str):
    """форматировать счет получателя"""
    to_name_list = to_name_str.split()
    bank_account = '**' + to_name_list[1][-4:]
    return f"{to_name_list[0]} {bank_account}"

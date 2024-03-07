import json


def get_last_acc_transactions(json_file, operation_count=5):
    operation_output_list = []
    """ возвращает 5 последних выполенных переводов """
    with open('data/operations.json') as file:
        operations = json.load(file)

    executed_operations = []
    for oprt in operations:
        # фильтрация по наличию свойства state
        if 'state' in oprt:
            # фильтрация по state = EXECUTED и типу Перевод
            if oprt['state'] == 'EXECUTED' and 'from' in oprt:
                executed_operations.append(oprt)
    # обратная сортировка по времени
    sorted_executed_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

    for i in range(operation_count):
        operation = sorted_executed_operations[i]
        description = operation['description']
        # время
        time_list = operation['date'][:10].split('-')
        time_list = time_list[::-1]
        time = '.'.join(time_list)
        # from
        from_name_str = operation['from']
        from_name_list = from_name_str.split()
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
        to_name = f"{' '.join(to_name_list)} **{bank_acc_to}"

        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        operation_output_list.append(f"{time} {description}\n{from_name} -> {to_name}\n{amount} {currency}\n")
        print(1)
        return operation_output_list

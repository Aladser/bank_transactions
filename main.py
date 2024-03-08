import utils

OPERATION_JSON_FILE = 'data/operations.json'


def main():
    executed_transactions = utils.get_executed_transactions(OPERATION_JSON_FILE)
    last_executed_transactions = utils.get_last_executed_transactions(executed_transactions)
    for order in last_executed_transactions:
        [print(str) for str in order]
        print()


if __name__ == "__main__":
    main()

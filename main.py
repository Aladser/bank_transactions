import utils

OPERATION_JSON_FILE = 'data/operations.json'


def main():
    executed_money_orders = utils.get_executed_money_orders(OPERATION_JSON_FILE)
    last_executed_money_orders = utils.get_last_executed_money_orders(executed_money_orders)
    for order in last_executed_money_orders:
        [print(str) for str in order]
        print()


if __name__ == "__main__":
    main()

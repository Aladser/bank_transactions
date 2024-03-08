from utils import BankAccount

OPERATION_JSON_FILE = 'data/operations.json'


def main():
    bank_account = BankAccount(OPERATION_JSON_FILE)

    for operation in bank_account.get_last_executed_transactions():
        [print(str) for str in operation]
        print()


if __name__ == "__main__":
    main()

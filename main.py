from classes import BankAccount

TRANSACTIONS_FILE = 'data/operations.json'
TRANSACTIONS_FILE1 = 'data/test_operations.json'


def main():
    bank_account = BankAccount(TRANSACTIONS_FILE)
    for transaction in bank_account.get_last_executed_transactions():
        [print(str) for str in transaction]
        print()


if __name__ == "__main__":
    main()

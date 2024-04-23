from src import BankAccount

TRANSACTIONS_FILE = 'data/operations.json'
TRANSACTIONS_FILE1 = 'data/test_operations.json'

if __name__ == "__main__":
    bank_account = BankAccount(TRANSACTIONS_FILE)
    for transaction in bank_account.get_last_executed_transactions():
        [print(line) for line in transaction]
        print()


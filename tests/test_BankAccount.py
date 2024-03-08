import os, unittest
from classes import BankAccount

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_dir = f"{root_dir}/data/"
test_file_path = f"{data_dir}test_operations.json"
test_1_output = [
    {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
    {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}
]
test_2_output = [
    ['26.08.2019 Перевод организации', 'Maestro 1596 83** **** 5199 -> Счет **9589', '31957.58 руб.'],
    ['03.07.2019 Перевод организации', 'MasterCard 7158 30** **** 6758 -> Счет **5560', '8221.37 USD'],
    ['23.03.2018 Открытие вклада', 'Счет **2431']
]


class TestBankAccount(unittest.TestCase):

    def test_get_executed_money_orders(self):
        bank_account = BankAccount(test_file_path)
        self.assertEqual(bank_account.get_executed_transactions(), test_1_output)

    def test_get_last_executed_money_orders(self):
        bank_account = BankAccount(test_file_path)
        self.assertEqual(bank_account.get_last_executed_transactions(), test_2_output)

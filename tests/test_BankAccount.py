import os
import unittest
from utils import *

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_dir = f"{root_dir}/data/"
test_file_path = f"{data_dir}test_operations.json"
test_1_output = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                  'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                  'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                  'to': 'Счет 64686473678894779589'},
                 {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                  'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                  'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                  'to': 'Счет 35383033474447895560'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                  'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                  'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                  'to': 'Счет 11776614605963066702'}
                 ]
test_2_ouput = [
    ['26.08.2019 Перевод организации', 'Maestro 1596 83** **** 5199 -> Счет **9589', '31957.58 руб.'],
    ['03.07.2019 Перевод организации', 'MasterCard 7158 30** **** 6758 -> Счет **5560', '8221.37 USD'],
    ['30.06.2018 Перевод организации', 'Счет 7510 68** **** 6952 -> Счет **6702', '9824.07 USD']
]


class TestGetMoneyOrder(unittest.TestCase):

    def test_get_executed_money_orders(self):
        bank_account = BankAccount(test_file_path)
        self.assertEqual(bank_account.get_executed_transactions(), test_1_output)

    def test_get_last_executed_money_orders(self):
        bank_account = BankAccount(test_file_path)
        self.assertEqual(bank_account.get_last_executed_transactions(), test_2_ouput)

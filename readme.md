## Код для виджета «Операции по счетам»

``BankAccount`` - класс, который отвечает за получение денежных операций

Для получения необходимых данных выполнены следующие шаги:
+ фильтрация строк JSON-файла наличием ключа ``state='EXECUTED'``
с помощью метода ``BankAccount.get_executed_transactions()``
+ полученный массив строк сортируется по ключу времени по убыванию
+ выводятся 5 последних по времени операций при помощи метода 
``BankAccount.get_last_executed_transactions()``

Тесты выполняются для ``pytest`` и ``unittest``. Основными тестами являются ``unittest``.
Для тестов используется урезанный массив данных *test_operations.json*

###  Тестирование покрытия тестами
``pytest --cov=src --cov-report=html``

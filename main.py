from src.generators import filter_by_currency
from src.search_and_count import process_bank_search
from src.utils import read_json_file
from src.read_transactions import read_csv_transactions, read_excel_transactions
from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_card_number
from typing import Callable

print(""" 
   Привет! Добро пожаловать в программу работы 
           с банковскими транзакциями.
""")

dict_file = {1: read_json_file, 2: read_csv_transactions, 3: read_excel_transactions}
path_file = {
    1: "D:/SkyPro/home_work/data/operations.json",
    2: "D:/SkyPro/home_work/data/transactions.csv",
    3: "D:/SkyPro/home_work/data/transactions_excel.xlsx"
}

status = ["EXECUTED", "CANCELED", "PENDING"]


def main():
    while True:
        print(
            ' Выберите необходимый пункт меню:\n '
            ' 1. Получить информацию о транзакциях из JSON-файла\n '
            ' 2. Получить информацию о транзакциях из CSV-файла\n '
            ' 3. Получить информацию о транзакциях из XLSX-файла\n '
        )
        user_input: int = int(input())
        if user_input == 1:
            print('Для обработки выбран JSON-файл\n')
        elif user_input == 2:
            print('Для обработки выбран CSV-файл\n')
        elif user_input == 3:
            print('Для обработки выбран EXCEL-файл\n')
        else:
            print('        !!! Некорректный ввод !!!\n')

        get_func: Callable | None = dict_file.get(user_input)
        if get_func:
            path_to_file: str = path_file.get(user_input)
            transaction = get_func(path_to_file)
            break

    print(len(transaction))

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
              f'Доступные для фильтрации статусы: {",".join(status)}')
        input_status: str = input().upper()
        if input_status in status:
            transaction = filter_by_state(transaction, input_status)
            print(f'Операции отфильтрованы по статусу "{input_status}", {len(transaction)}')
            break
        else:
            print(f'Статус операции "{input_status}" недоступен.')

    print('Отсортировать по дате? Да/Нет')
    input_date: bool = input().lower() == 'да'
    if input_date:
        print('Отсортировать по возрастанию или по убыванию?')
        input_type_of_sorting: bool = input().lower() == 'по убыванию'
        transaction = sort_by_date(transaction, input_type_of_sorting)
        print(len(transaction))

    print('Выводить только рублевые транзакции? Да/Нет')
    user_input: bool = input().lower() == 'да'
    if user_input:
        transaction = list(filter_by_currency(transaction, 'RUB'))
        print(f"Нашлось рублевых: {len(transaction)}")

    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет?')
    if user_input:
        print('Введите слово для фильтрации:')
        user_word: str = input().lower()
        transaction = process_bank_search(transaction, user_word)

    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(transaction)}')

    for trans in transaction:
        state = trans.get('state')
        date = trans.get('date')
        amount = trans.get('amount')
        currency_name = trans.get('currency_name')
        currency_code = trans.get('currency_code')
        from_account = trans.get('from') if isinstance(trans.get('from'), str) else None
        to_account = trans.get('to')
        description = trans.get('description')


        out_print = f'{date[:10]}.{date[5:7]}.{date[:4]} {description}'
        check_to = get_mask_card_number(to_account) if to_account else "Нет данных"
        if from_account:
            check_from = ' -> ' + get_mask_card_number(from_account)
        else:
            check_from = ''  # не выводим стрелку если нет FROM


        summ_print = f'Сумма: {amount} {currency_code}'
        print(f'{out_print}\n{check_to}{check_from}\n{summ_print}')


if __name__ == '__main__':
    main()

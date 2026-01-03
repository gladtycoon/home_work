import re
from collections import Counter


def process_bank_search(transaction: list[dict], search_string: str) -> list[dict]:
    """ Функция принимает список словарей с данными о банковских
    операциях и строку поиска, и возвращает список словарей,
    у которых в описании есть данная строка """

    filtered_data = [data for data in transaction if re.search(search_string.lower(), data.get('description', '').lower())]
    return filtered_data


def process_bank_operations(transaction: list[dict], category: list) -> dict:
    """ Функция принимает список словарей с данными
    о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории """

    result_transaction = [
        data["description"] for data in transaction if data["description"] in list(map(lambda x: x, category))
    ]
    count_by_category = dict(Counter(result_transaction))
    return count_by_category

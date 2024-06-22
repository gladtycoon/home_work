from typing import Any, Dict, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: List[Dict[str, dict[Any, Any]]], type_of_currency: str) -> str:
    """Принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди id операций, в которых указана заданная валюта"""

    print("\n*** id операций с выбранной валютой ***")
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == type_of_currency:
            yield transaction["id"]


for usd_transactions in filter_by_currency(transactions, "USD"):

    print(usd_transactions)


def transaction_descriptions(transactions: List[Dict[str, dict[Any, Any]]]) -> str:
    """Принимает список словарей и возвращает описание каждой операции по очереди"""

    print("\n*** Типы банковских операций ***")
    for transaction in transactions:
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(len(transactions)):
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> int:
    """Генерирует номера карт в заданном диапазоне"""

    print("\n*** Сгенерированные номера карт ***")
    for num in range(start, stop + 1):
        card_number = f"{num:016d}"
        formated_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formated_card_number


for card_number in card_number_generator(1, 5):
    print(card_number)

import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv("../.env")


def return_amount_transactions(transactions: Any) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    amount = float(transactions["operationAmount"]["amount"])
    currency = transactions["operationAmount"]["currency"]["code"]
    # print(amount, currency)
    if currency == "RUB":
        return amount
    else:
        API_KEY = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        # status_code = response.status_code
        # print(f'Статус код: {status_code}')
        return response.json()
        #return round(response.json()["result"], 2)


if __name__ == "__main__":
    result = return_amount_transactions(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
    print(f"Сумма транзакции равна: \n{result}")

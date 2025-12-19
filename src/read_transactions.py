""" Модуль для чтения финансовых транзакций из файлов разных форматов """

import csv
from typing import Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict]:
    """Функция, которая принимает путь до csv-файла, считывает транзакции и возвращает список словарей"""
    transactions_from_csv = []
    with open(file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            transactions_from_csv.append(dict(row))
        return transactions_from_csv


def read_excel_transactions(file_path: str) -> List[Dict]:
    """Функция, которая принимает путь до excel-файла, считывает транзакции и возвращает список словарей"""
    df = pd.read_excel(file_path)
    transactions_from_excel = df.to_dict(orient="records")

    return transactions_from_excel


if __name__ == "__main__":
    result_from_csv = read_csv_transactions("data/transactions.csv")
    result_from_excel = read_excel_transactions("data/transactions_excel.xlsx")
    print("\n", result_from_csv)
    print("\n", result_from_excel)

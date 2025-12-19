""" Тестирование функций чтения транзакций из файлов разных форматов """

import unittest
from unittest.mock import mock_open, patch

from src.read_transactions import read_csv_transactions, read_excel_transactions


def test_read_csv_transactions():
    mock_csv_data = """ id; state;amount; description
1;EXECUTED; 100.50; Оплата услуг
2;PENDING; 200.00; Перевод другу """

    mock_file = mock_open(read_data=mock_csv_data)
    with patch("builtins.open", mock_file):
        with patch("csv.DictReader") as mock_reader:
            mock_reader.return_value = [
                {"id": "1", "state": "EXECUTED", "amount": "100.50", "description": "Оплата услуг"},
                {"id": "2", "state": "PENDING", "amount": "200.00", "description": "Перевод другу"},
            ]

            result = read_csv_transactions("test.csv")

            assert (result, list)
            assert (len(result), 2)
            assert (result[0]["id"], "1")
            assert (result[0]["state"], "EXECUTED")
            assert (result[0]["amount"], "100.50")
            assert (result[1]["state"], "PENDING")

            mock_file.assert_called_once_with("test.csv", "r", encoding="utf-8")
            mock_reader.assert_called_once()

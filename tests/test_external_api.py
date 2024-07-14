from unittest.mock import patch, mock_open
from src.external_api import return_amount_transactions


@patch('requests.get')
def tests_return_amount_transactions(mock_get):
    mock_get.return_value.json.return_value = 718518.305495
    assert return_amount_transactions(mock_get) == 718518.305495

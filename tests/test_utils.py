from unittest.mock import patch, mock_open

from src.utils import get_path_to_json_file


# def test_get_path_to_json_file():
#     with patch('builtins.open', mock_open()) as mock_file:
#         with patch('json.load') as mock_load:
#             mock_load.return_value = {'transactions': [{'id': '1', 'amount': 100}]}
#             assert get_path_to_json_file(mock_file) == {'transactions': [{'id': '1', 'amount': 100}]}


@patch("builtins.open", new_callable=mock_open, read_data='{"transaction_id": 1}')
def test_get_path_to_json_file(mock_file):
    transactions = get_path_to_json_file("test.json")
    assert transactions == {"transaction_id": 1}
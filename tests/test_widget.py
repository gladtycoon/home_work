import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "number_acc_or_card, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 **** **** 6361"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 **** **** 6361"),
    ],
)
def test_mask_account_card(number_acc_or_card, expected):
    assert mask_account_card(number_acc_or_card) == expected


@pytest.fixture
def unformatted_data():
    return "2018-07-11T02:26:18.671407"


def test_get_data(unformatted_data):
    assert get_data(unformatted_data) == "11.07.2018"

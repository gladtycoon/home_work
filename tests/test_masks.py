import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number():
    return "7000792289606361"


@pytest.fixture
def account_number():
    return "73654108430135874305"


def test_mask_card_number(card_number, account_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"
    assert get_mask_account(account_number) == "**4305"

import pytest

from src.widget import mask_account_card


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"

@pytest.mark.parametrize("x, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("1596837868705199", "1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("64686473678894779589", "**9589"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Classic a831982476737658", "Visa Classic Неправильно ввели номер карты!"),
])
def test_mask_account_card_param(x, expected):
    assert mask_account_card(x) == expected

# def test_mask_account_card_error(x, expected):

import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("x, expected", [
    ("1596837868705199", "1596 83** **** 5199"),
    (1596837868705199, "1596 83** **** 5199"),
    ("159683786870519a", "Неправильно ввели номер карты!"),
    (15968, "Неправильно ввели номер карты!"),
    ("15968", "Неправильно ввели номер карты!"),
    ('',"Неправильно ввели номер карты!")
])
def test_get_mask_card_number(x, expected):
    assert get_mask_card_number(x) == expected

@pytest.mark.parametrize("x, expected", [
    ("64686473678894779589", "**9589"),
    (64686473678894779589, "**9589"),
    ("ad686473678894779589", "Неправильно ввели номер счёта!"),
    ("646864", "Неправильно ввели номер счёта!"),
    (646864, "Неправильно ввели номер счёта!"),
    ("", "Неправильно ввели номер счёта!")
])
def test_get_mask_account(x, expected):
    assert get_mask_account(x) == expected

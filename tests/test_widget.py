import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"

@pytest.mark.parametrize("x, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("1596837868705199", "Без названия 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("64686473678894779589", "Без названия **9589"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Classic a831982476737658", "Visa Classic Неправильно ввели номер карты!"),
])
def test_mask_account_card_param(x, expected):
    assert mask_account_card(x) == expected

def test_mask_account_card_error():
    with pytest.raises(AttributeError):
        mask_account_card(-1)

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-03-11T02:26:18") == "11.03.2024"
    assert get_date("2024-03-11") == "11.03.2024"
    assert get_date("2024/03/11") == "11.03.2024"
    assert get_date("2024/03/1") == "Неправильный формат даты!"
    assert get_date("02:26:18.671407") == "Неправильный формат даты!"


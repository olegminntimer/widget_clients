from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"
    assert get_mask_card_number(1596837868705199) == "1596 83** **** 5199"
    assert get_mask_card_number("159683786870519a") == "Неправильно ввели номер карты!"
    assert get_mask_card_number(15968) == "Неправильно ввели номер карты!"
    assert get_mask_card_number("15968") == "Неправильно ввели номер карты!"
    assert get_mask_card_number('') == "Неправильно ввели номер карты!"

def test_get_mask_account():
    assert get_mask_account("64686473678894779589") == "**9589"
    assert get_mask_account(64686473678894779589) == "**9589"
    assert get_mask_account("ad686473678894779589") == "Неправильно ввели номер счёта!"
    assert get_mask_account("646864") == "Неправильно ввели номер счёта!"
    assert get_mask_account(646864) == "Неправильно ввели номер счёта!"
    assert get_mask_account("") == "Неправильно ввели номер счёта!"

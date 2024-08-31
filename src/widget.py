import re

from src import masks


def mask_account_card(account: str) -> str:
    """Функция возвращает замаскированный номер"""

    account_list = account.split()  # Создаем список слов
    new_account = ""

    if len(account_list) == 1:
        new_account = "Без названия "
    elif len(account_list) > 1:
        new_account = " ".join(account_list[:-1]) + " "
    else:
        return "Неправильно ввели номер карты или счёта!"

    # Для карты
    if len(account_list[-1]) == 16:
        new_account += masks.get_mask_card_number(account_list[-1])
    # Для счёта
    elif len(account_list[-1]) == 20:
        new_account += masks.get_mask_account(account_list[-1])

    return new_account


def get_date(date_: str) -> str:
    """Возвращает дату в формате "ДД.ММ.ГГГГ" """
    date_list = re.split(r"[-.,/]", date_)

    if (
        len(date_list[0]) == 4
        and date_list[0].isdigit()
        and len(date_list[1]) == 2
        and date_list[1].isdigit()
        and len(date_list[2]) >= 2
    ) and date_list[2][:2].isdigit():
        return date_list[2][:2] + "." + date_list[1] + "." + date_list[0]
    else:
        return "Неправильный формат даты!"

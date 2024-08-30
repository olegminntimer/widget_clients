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

    return  new_account


def get_date(date_: str) -> str:
    """Возвращает дату в формате "ДД.ММ.ГГГГ" """

    return ".".join(date_[:10].split("-")[::-1])

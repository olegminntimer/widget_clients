from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску."""

    card_number = str(card_number)  # Введенное приводим к типу str

    if card_number.isdigit() and len(card_number) == 16:
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    else:
        return "Неправильно ввели номер карты!"


def get_mask_account(account: Union[str, int]) -> str:
    """Функция get_mask_account принимает на вход номер счёта и возвращает его маску."""

    account = str(account)  # Введенное приводим к типу str

    if account.isdigit() and len(account) == 20:
        return "**" + account[16:]
    else:
        return "Неправильно ввели номер счёта!"

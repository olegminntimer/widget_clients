import logging
from logging import DEBUG
from pathlib import Path
from typing import Union

BASE_DIR = Path(__file__).resolve().parent.parent
file_name = str(BASE_DIR / 'logs' / 'masks.log')

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(file_name)
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(DEBUG)

def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску."""

    card_number = str(card_number)  # Введенное приводим к типу str
    logger.debug('Validating the card')
    if card_number.isdigit() and len(card_number) == 16:
        logger.debug('Successful verification')
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    else:
        logger.error('Incorrect format')
        return "Неправильно ввели номер карты!"


def get_mask_account(account: Union[str, int]) -> str:
    """Функция get_mask_account принимает на вход номер счёта и возвращает его маску."""

    account = str(account)  # Введенное приводим к типу str
    logger.debug('Validating the account')
    if account.isdigit() and len(account) == 20:
        logger.debug('Successful verification')
        return "**" + account[16:]
    else:
        logger.error('Incorrect format')
        return "Неправильно ввели номер счёта!"

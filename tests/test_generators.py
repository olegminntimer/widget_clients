import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import transactions


def test_filter_by_currency_usd(transactions):
    gen = filter_by_currency(transactions, "USD")
    assert next(gen) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(gen) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }

def test_filter_by_currency_rub(transactions):
    gen = filter_by_currency(transactions, "RUB")
    assert next(gen) == {
        "id": 873106923,
        "date": "2019-03-23T01:09:46.296404",
        "state": "EXECUTED",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(gen) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }
def test_filter_by_currency_another(transactions):
    gen = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(gen)

def test_filter_by_currency_empty():
    gen = filter_by_currency([], "EUR")
    with pytest.raises(StopIteration):
        next(gen)

def test_transaction_descriptions(transactions):
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"

def test_transaction_descriptions_empty():
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)

def test_card_number_generator():
    gen = card_number_generator(15, 18)
    assert next(gen) == "0000 0000 0000 0015"
    assert next(gen) == "0000 0000 0000 0016"
    assert next(gen) == "0000 0000 0000 0017"
    assert next(gen) == "0000 0000 0000 0018"
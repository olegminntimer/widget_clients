from pathlib import Path

from src.utils import get_json


def test_get_json():
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_name = str(BASE_DIR / "data" / "operations_2.json")
    operation_list = get_json(file_name)
    assert operation_list == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


def test_get_json_not_exist():
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_name = str(BASE_DIR / "data" / "operations_3.json")
    operation_list = get_json(file_name)
    assert operation_list == []


def test_get_json_null():
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_name = str(BASE_DIR / "data" / "operations_null.json")
    operation_list = get_json(file_name)
    assert operation_list == []


def test_get_json_err():
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_name = str(BASE_DIR / "data" / "operations_err.json")
    operation_list = get_json(file_name)
    assert operation_list == []

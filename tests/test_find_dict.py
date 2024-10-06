from src.find_dict import search_by_line, search_by_type

list_example = [
  {"description": "Перевод организации"},
  {"description": "Перевод организации"},
  {"description": "Перевод организации"},
  {"description": "Открытие вклада"},
  {"description": "Перевод со счета на счет"},
  {"description": "Перевод со счета на счет"}
]

def test_search_by_line():
    assert search_by_line(list_example, 'Перевод') == [
  {"description": "Перевод организации"},
  {"description": "Перевод организации"},
  {"description": "Перевод организации"},
  {"description": "Перевод со счета на счет"},
  {"description": "Перевод со счета на счет"}
]

def test_search_by_type():
    assert search_by_type(list_example) == {
        "Перевод организации" : 3,
        "Открытие вклада" : 1,
        "Перевод со счета на счет" : 2
    }
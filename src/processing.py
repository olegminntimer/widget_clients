from typing import List, Dict, Any

# DL = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(dict_list: List[Dict], state: str = 'EXECUTED') -> List[Dict[Any, Any]]:
    ''' Функция возвращает список словарей по ключу state '''
    return list(filter(lambda v: v['state'] == state, dict_list))

def sort_by_date(list_to_be_sorted: List[Dict], sort_by: bool = True) -> List[Dict[Any, Any]]:
    ''' Функция сортирует список словарей по дате (по умолчанию - убывание) '''
    return sorted(list_to_be_sorted, key=lambda d: d['date'], reverse=sort_by)

# print(filter_by_state(DL)) #,'CANCELED'))
# print(sort_by_date(DL,False))

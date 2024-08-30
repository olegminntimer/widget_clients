from typing import Any, Dict, List


def  filter_by_state(dict_list: List[Dict], state: str = "EXECUTED") -> List[Dict[Any, Any]]:
    """Функция возвращает список словарей по ключу state"""

    return list(filter(lambda v: v["state"] == state, dict_list))


def sort_by_date(list_to_be_sorted: List[Dict], sort_by: bool = True) -> List[Dict[Any, Any]]:
    """Функция сортирует список словарей по дате (по умолчанию - убывание)"""

    return sorted(list_to_be_sorted, key=lambda d: d["date"], reverse=sort_by)

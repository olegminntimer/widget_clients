import re
from collections import Counter


def search_by_line(transactions: list, word: str) -> list:
    """Функция для поиска в списке словарей операций по заданной строке."""
    transactions_line = []
    for transaction in transactions:
        if re.search(word, transaction["description"]):
            transactions_line.append(transaction)
    return transactions_line


def search_by_type(transactions: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа."""
    transactions_type = []
    for transaction in transactions:
        transactions_type.append(transaction["description"])
    return dict(Counter(transactions_type))

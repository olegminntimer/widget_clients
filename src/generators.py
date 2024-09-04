def filter_by_currency(dict_list: list, currency:str):
    """ Функция-генератор, которая выдает транзакции из входного списка
     транзакций dict_list в соответствии с заданной валютой currency """
    for d in dict_list:
        if d.get("operationAmount").get("currency").get("code") == currency:
            yield d


def transaction_descriptions(dict_list):
    """ Функция-генератор, которая выдает описание каждой транзакции из входного списка транзакций dict_list """

    for i in dict_list:
        yield i.get("description")


def card_number_generator(start:int, stop:int):
    """ Функция-генератор, которая генерирует номера карт
     в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999 """

    max_width = 16
    for i in range(start, stop + 1):
        value_str = f"{i:0{max_width}}"
        yield f"{value_str[:4]} {value_str[4:8]} {value_str[8:12]} {value_str[12:16]}"

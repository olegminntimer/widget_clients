from curses.ascii import isdigit


def filter_by_currency(dict_list: list, currency:str):
    """ Функция-генератор, которая выдает транзакции из входного списка
     транзакций dict_list в соответствии с заданной валютой currency """

    for i in dict_list:
        if i.get("operationAmount").get("currency").get("code") == currency:
            yield i


def card_number_generator(start:int, finish:int):
    """ Функция-генератор, которая генерирует номера карт
     в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999 """

    # if (isdigit(start) and isdigit(finish) and
    # (0 <= start <= 9999999999999999) and (0 <= finish <= 9999999999999999)):
    max_width = 16
    for i in range(start, finish):
        value_str = f"{i:0{max_width}}"
        yield f"{value_str[:4]} {value_str[4:8]} {value_str[8:12]} {value_str[12:16]}"
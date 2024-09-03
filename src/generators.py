def filter_by_currency(dict_list: list, currency:str):
    """ Функция-генератор, которая выдает транзакции из входного списка
     транзакций dict_list в соответствии с заданной валютой currency """

    for i in dict_list:
        if i.get("operationAmount").get("currency").get("code") == currency:
            yield i

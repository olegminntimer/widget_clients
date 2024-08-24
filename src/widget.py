from src import masks

input_data = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
    # "Неправильно ввели номер карты!",
]

date_old = '2024-03-11T02:26:18.671407'

def mask_account_card(account: str) -> str:
    """Функция возвращает замаскированный номер"""

    account_list = account.split()  # Создаем список слов

    account_name = " ".join(account_list[:-1])  # Название без номера

    if account_list[0] == "Неправильно":  # Выходим если введена ошибочная запись
        new_account = account
    #  Для карты
    elif len(account_list[-1]) == 16:
        new_account = account_name + " " + masks.get_mask_card_number(account_list[-1])
    # Для счёта
    elif len(account_list[-1]) == 20:
        new_account = account_name + " " + masks.get_mask_account(account_list[-1])
    return new_account

def get_date(date_: str)->str:
    ''' Возвращает дату в формате "ДД.ММ.ГГГГ" '''

    date_new = date_[:10].split("-")


    return date_new

print(get_date(date_old))

# for i in input_data:  # Тест
#     print(mask_account_card(i))

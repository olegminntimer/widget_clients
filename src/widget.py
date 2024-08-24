import masks

input_data = [
    'Maestro 1596837868705199',
    'Счет 64686473678894779589',
    'MasterCard 7158300734726758',
    'Счет 35383033474447895560',
    'Visa Classic 6831982476737658',
    'Visa Platinum 8990922113665229',
    'Visa Gold 5999414228426353',
    'Счет 73654108430135874305',
    'Неправильно ввели номер карты!',
]


def mask_account_card(account: str)->str:
    ''' Функция возвращает замаскированный номер '''


    account_list = account.split()
    return ' '.join(account_list[:-1])

    if account_list[0] == 'Неправильно':
        return account
    elif len(account_list[-1]) == 16:
        return get_mask_card_number(account_list[-1])
        # return account_list[:-1] + ' ' + get_mask_card_number(account_list[-1])
    elif len(account_list[-1]) == 20:
        return account_list[:-1] + ' ' + get_mask_account(account_list[-1])

for i in input_data:
    print(mask_account_card(i))

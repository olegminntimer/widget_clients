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
]


def mask_account_card(account: str)->str:
    ''' Функция возвращает замаскированный номер '''


    account_list = account.split()
    return ' '.join(account_list)

    if account_list[0] == 'Неправильно':
        return account
    elif len(account_list[-1]) == 16:
        pass
    elif len(account_list[-1]) == 20:
        pass

for i in input_data:
    print(mask_account_card(i))

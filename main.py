from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

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

date_old = "2024-03-11T02:26:18.671407"

DL = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def main():
    ''' Основная вызывающая функция '''
    # print(get_date(date_old))
    #
    # for i in input_data:  # Тест
    #     print(mask_account_card(i))

    list_of_dict = filter_by_state(DL)
    for i in list_of_dict:
        print(i)
    print()

    list_of_dict = filter_by_state(DL,'CANCELED')
    for i in list_of_dict:
        print(i)
    print()

    list_of_dict = sort_by_date(DL)
    for i in list_of_dict:
        print(i)
    print()

    list_of_dict = sort_by_date(DL, False)
    for i in list_of_dict:
        print(i)
    print()


if __name__ == '__main__':
    main()
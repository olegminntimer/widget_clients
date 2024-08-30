from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

input_data = [
    "Счёт 64686473678894779589",
    "Счёт 646864736788q4779589",
    "64686473678894779589",
    "64686473678894a79589",
    "MasterCard 7158300734726758",
    "MasterCard 7q58300734726758",
    "Счёт 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счёт 73654108430135874305",
]

date_old = "2024-03-11T02:26:18.671407"

dict_list_example= [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def main():
    """Основная функция"""

    # print(get_date(date_old))

    # for i in input_data:  # Тест
    #     print(mask_account_card(i))

    # list_of_dict = filter_by_state(dict_list_example)
    # for i in list_of_dict:
    #     print(i)
    # print()

    # list_of_dict = filter_by_state(dict_list_example, "CANCELED")
    # for i in list_of_dict:
    #     print(i)
    # print("--------------")
    #
    # list_of_dict = filter_by_state(dict_list_example, "WRONG")
    # for i in list_of_dict:
    #     print(i)
    # print("--------------")

    list_of_dict = sort_by_date(dict_list_example)
    for i in list_of_dict:
        print(i)
    print()

    list_of_dict = sort_by_date(dict_list_example, False)
    for i in list_of_dict:
        print(i)
    print()

    # i = 'a'
    # while i != 'q':
    #     i = input("Введи значение: ")
    #     print(mask_account_card(i))


if __name__ == "__main__":

    main()

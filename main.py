from pathlib import Path

from src.find_dict import search_by_line, search_by_type
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_pandas import read_csv, read_xlsx
from src.utils import get_json


def main():
    ''' Основная программа обработки транзакций '''

    greeting = input('''Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Ваш выбор: ''')
    BASE_DIR = Path(__file__).resolve().parent
    while True:
        if greeting == '1':
            print('Для обработки выбран JSON-файл.')
            file_name = str(BASE_DIR / "data" / "operations.json")
            transactions_main = get_json(file_name)
            break
        elif greeting == '2':
            print('Для обработки выбран CSV-файл.')
            file_name = str(BASE_DIR / "data" / "transactions.csv")
            transactions_main = read_csv(file_name)
            break
        elif greeting == '3':
            print('Для обработки выбран EXCEL-файл.')
            file_name = str(BASE_DIR / "data" / "transactions_excel.xlsx")
            transactions_main = read_xlsx(file_name)
            break
        else:
            greeting = input('Нет такого пункта. \nВаш выбор: ')

    while True:
        filtering = input('''\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
Ваш выбор: ''').upper()
        if filtering in ['EXECUTED', 'CANCELED', 'PENDING']:
            break
        else:
            print(f'Статус операции "{filtering}" недоступен.')
    transactions_filtering = filter_by_state(transactions_main, filtering)
    transactions_main = transactions_filtering
    print(f'Операции отфильтрованы по статусу "{filtering}"')

    while True:
        sort_date = input('\nОтсортировать операции по дате? Да/Нет (Yes/No) - ').lower()
        if sort_date in ['да', 'д', 'yes', 'y']:
            while True:
                # ascending=возрастание, descending=убывание
                ascending = input('\nОтсортировать по возрастанию или по убыванию? ').lower()
                if ascending == 'по возрастанию':
                    transactions_main = sort_by_date(transactions_filtering, False)
                    break
                elif ascending == 'по убыванию':
                    transactions_main = sort_by_date(transactions_filtering, True)
                    break
            break
        elif sort_date in ['нет', 'n', 'no', 'n']:
            break

    while True:
        trans_rub = input('\nВыводить только рублевые транзакции? Да/Нет (Yes/No) - ').lower()
        if trans_rub in ['да', 'д', 'yes', 'y']:
            transactions_currency = []
            for i in filter_by_currency(transactions_main, 'RUB'):
                transactions_currency.append(i)
            transactions_main = transactions_currency
            break
        elif trans_rub in ['нет', 'n', 'no', 'n']:
            break

    while True:
        filtered_ = input('''\nОтфильтровать список транзакций по определенному слову
в описании? Да/Нет (Yes/No) - ''').lower()
        if filtered_ in ['да', 'д', 'yes', 'y']:
            filtered_word = input('Введите слово для поиска: ')
            transactions_main = search_by_line(transactions_main, filtered_word)
            break
        elif filtered_ in ['нет', 'n', 'no', 'n']:
            break

    print(search_by_type(transactions_main))

    print('\nРаспечатываю итоговый список транзакций...')
    print('\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')


if __name__ == '__main__':
    main()

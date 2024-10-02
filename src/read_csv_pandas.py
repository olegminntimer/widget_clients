import logging
from pathlib import Path

import  pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent # print(BASE_DIR) #C:\Users\remus\PycharmProjects\widget_clients
file_name_csv = str(BASE_DIR / 'data' / 'transactions.csv') #C:\Users\remus\PycharmProjects\widget_clients\data\operations.json
file_name_xlsx = str(BASE_DIR / 'data' / 'transactions_excel.xlsx') #C:\Users\remus\PycharmProjects\widget_clients\data\operations.json

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename=str(BASE_DIR / 'logs' / 'read_csv_pandas.log'),
    filemode='w',
    encoding='utf-8',
)
logger_csv = logging.getLogger('csv')
logger_xlsx = logging.getLogger('xlsx')


def read_csv(filename:str) -> list:
    ''' Функция считывает финансовые операции из csv-файла и выдает список словарей с транзакциями '''
    logger_csv.debug('Открываем csv-файл для чтения')
    try:
        reader_csv = pd.read_csv(filename, delimiter=';')
        logger_csv.debug('Считали csv')
    except FileNotFoundError:
        logger_csv.error('Файл csv не найден')
        return []
    return reader_csv.to_dict(orient='records')

def read_xlsx(filename:str) -> list:
    ''' Функция считывает финансовые операции из excel-файла и выдает список словарей с транзакциями '''
    logger_csv.debug('Открываем excel-файл для чтения')
    try:
        reader_xlsx = pd.read_excel(filename)
        logger_xlsx.debug('Считали excel')
    except FileNotFoundError:
        logger_xlsx.error('Файл excel не найден')
        return []
    return reader_xlsx.to_dict(orient='records')



# if __name__ == "__main__":
#
#
#     # print(read_csv(file_name_csv))
#     print(read_xlsx(file_name_xlsx))
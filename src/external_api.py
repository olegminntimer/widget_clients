import os

import requests
from dotenv import load_dotenv


def get_convert(transaction_: dict) -> float:
    ''' Функция возвращает сумму транзакции в рублях, если есть необходимость,
     то конвертирует в рубли из другой валюты '''

    code = transaction_.get("operationAmount").get("currency").get("code")
    summ = transaction_.get("operationAmount").get("amount")
    if code == "RUB":
        return float(summ)
    else:
        load_dotenv()
        apikey = os.getenv("API_KEY")
        headers = {
            "apikey": apikey
        }
        response_json = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?from={code}&to=RUB&amount={summ}', headers=headers).json()
        return response_json["result"]

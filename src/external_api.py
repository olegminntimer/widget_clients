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
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": summ,
            "from": code,
            "to": "RUB"
        }

        apikey = os.getenv("API_KEY")
        headers = {
            "apikey": apikey
        }

        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return round(float(result.get("result")), 2)

import json
import logging
from json import JSONDecodeError
from logging import DEBUG
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file_name = str(BASE_DIR / "logs" / "utils.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(file_name)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(DEBUG)


def get_json(path_to_file: str) -> list:
    """Функция принимает путь до файла и возвращает данные в формате json"""

    try:
        logger.debug("Opening the file...")
        with open(path_to_file, encoding="utf-8") as f:
            data = json.load(f)
            logger.debug("The data was considered")
            # data_out = []
            # for i in data:
            #     if 'id' in i:
            #         record_out = {
            #             'id' : i['id'],
            #             'state' : i['state'],
            #             'date' : i['date'],
            #             'amount' : i["operationAmount"]["amount"],
            #             'currency_name' : i["operationAmount"]["currency"]["name"],
            #             'currency_code' : i["operationAmount"]["currency"]["code"],
            #             'to' : i['to'],
            #             'description' : i['description']
            #         }
            #         if 'from' in i:
            #             record_out['from'] = i['from']
            #         data_out.append(record_out)
            return data
    except JSONDecodeError:
        logger.error("JSONDecodeError - Invalid JSON data.")
        return []
    except FileNotFoundError:
        logger.error("FileNotFoundError - The file does not exist.")
        return []
    except ValueError:
        logger.error("ValueError - Invalid JSON data.")
        return []

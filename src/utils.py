import json


def get_json(path_to_file: str) -> list:
    """Функция принимает путь до файла и возвращает данные в формате json"""

    try:
        with open(path_to_file, encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []
    except ValueError:
        return []

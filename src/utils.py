import json


def get_file(path_to_file: str) -> list:
    ''' Функция принимает путь до файла и возвращает список словарей '''

    try:
        with open(path_to_file, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return []





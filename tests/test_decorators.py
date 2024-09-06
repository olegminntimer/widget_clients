from src.decorators import log


def test_log_console(capsys):
    """Тест декоратора, который выводит результат работы функции в консоль"""

    @log()
    def add_numbers(a, b):
        return a / b

    add_numbers(2, 5)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n"


def test_log_console_zero(capsys):
    """Тест декоратора, который выводит результат работы функции в консоль"""

    @log()
    def add_numbers(a, b):
        return a / b

    add_numbers(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers error: division by zero. Inputs: (2, 0), {}\n"


def test_log_file():
    """Тест декоратора, который выводит результат работы функции в файл"""

    @log(filename="mylog.txt")
    def division(a, b):
        return a / b

    division(4, 5)
    with open("mylog.txt", "r") as file:
        lines = file.readlines()
        last_line = lines[-1]
    assert last_line == "division ok\n"


def test_log_file_zero():
    """Тест декоратора, который выводит результат работы функции в файл"""

    @log(filename="mylog.txt")
    def division(a, b):
        return a / b

    division(4, 0)
    with open("mylog.txt", "r") as file:
        lines = file.readlines()
        last_line = lines[-1]
    assert last_line == "division error: division by zero. Inputs: (4, 0), {}\n"

import os.path
from typing import Any, Callable, Optional


def log(filename: Optional[str] = "") -> Callable[[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]:
    """Декоратор выводит результат работы функции в консоль или файл"""

    def decorator(func):
        def inner(*args, **kwargs):
            name = func.__name__
            try:
                func(*args, **kwargs)
                conclusion = f"{name} ok"
            except Exception as e:
                conclusion = f"{name} error: {e}. Inputs: {args}, {kwargs}"
            if filename != "":
                if os.path.isfile(filename):
                    with open(filename, "a") as my_file:
                        my_file.write(conclusion + "\n")
                else:
                    with open(filename, "w") as my_file:
                        my_file.write(conclusion + "\n")
            else:
                print(conclusion)

            return func

        return inner

    return decorator

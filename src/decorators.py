from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Логирует вызов функции и ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = "my_function ok\n"
            except Exception as e:
                log_message = f"my_function error: {e}. Inputs: {args}, {kwargs}\n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return wrapper

    return decorator


#log(filename="mylog.txt")  # для вывода в файл mylog.txt
@log()                        # для печати в консоль
def my_function(x, y):
    return x + y


if __name__ == "__main__":
    print(my_function(1, 2))

from functools import wraps
from typing import Any, Callable


# Реализация двух функций для одновременного прохождения всех тестов
def log_to_logfile(filename: str) -> Callable:
    """Логирует вызов функции и ее результат в файл"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result_1 = func(*args, **kwargs)
                log_message = "my_function ok\n"
            except Exception as e:
                result_1 = "Error when executing code. Read mylog.txt\n"
                log_message = f"my_function error: {e}. Inputs: {args}, {kwargs}\n"
            with open(filename, "a", encoding="utf-8") as file:
                file.write(log_message)

            return result_1

        return wrapper

    return decorator


def log_to_console() -> Callable:
    """Логирует вызов функции и ее результат в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result_2 = func(*args, **kwargs)
                log_message = "my_function ok"
            except Exception as e:
                result_2 = "Error when executing code."
                log_message = f"my_function error: {e}. Inputs: {args}, {kwargs}"
            print(log_message)

            return result_2

        return wrapper

    return decorator


@log_to_logfile(filename="mylog.txt")  # для вывода в файл mylog.txt
def my_function_1(x, y):
    return x + y


@log_to_console()  # для печати в консоль
def my_function_2(x, y):
    return x / y


# Реализация декораторов по ТЗ (исходя из требований домашнего задания)


# def log(filename: str | None = None) -> Callable:
#     """Логирует вызов функции и ее результат в файл или в консоль"""
#
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         def wrapper(*args: Any, **kwargs: Any) -> Any:
#             try:
#                 result = func(*args, **kwargs)
#                 log_message = "my_function ok\n"
#             except Exception as e:
#                 result = "Error when executing code. Read mylog.txt"
#                 log_message = f"my_function error: {e}. Inputs: {args}, {kwargs}\n"
#             if filename:
#                 with open(filename, "a", encoding="utf-8") as file:
#                     file.write(log_message)
#             else:
#                 print(log_message)
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# # @log(filename="mylog.txt")  # для вывода в файл mylog.txt
# # def my_function(x, y):
# #     return x / y
#
#
# @log()                        # для печати в консоль
# def my_function(x, y):
#     return x + y
#
#
if __name__ == "__main__":
    print(my_function_1(12, 0))
    print(my_function_2(12, 0))

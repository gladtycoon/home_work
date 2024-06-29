import pytest

from src.decorators import my_function_1, my_function_2

# from src.decorators import my_function, log       # для тестирования декоратора, выполненного по ТЗ


def test_log_to_logfile():
    assert my_function_1(2, 1) == 3   # Положительный исход


def test_log_to_console():
    with pytest.raises(Exception):            # Выбрасывает исключение
        my_function_2(2, 0)


def test_log_to_console(capsys):              # Перехват сообщения в консоль (если логфайла нет)

    my_function_2(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"

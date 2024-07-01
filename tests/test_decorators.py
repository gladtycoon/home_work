#import pytest                            # для теста с выбросом исключения

from src.decorators import my_function    # для тестирования декоратора, выполненного по ТЗ


def test_log():

    assert my_function(2, 1) == 3   # Положительный исход


# def test_log_to_exception():
#
#     with pytest.raises(Exception):       # Выбрасывает исключение
#         my_function()


def test_log_to_console(capsys):           # Перехват сообщения в консоль (если логфайла нет)

    my_function(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"

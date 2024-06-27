import pytest

from src.decorators import my_function, log


def test_log_1():  # Положительный исход
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_2():  # Выбрасывает исключение
    with pytest.raises(Exception):
        my_function()


def test_log_3(capsys):  # Перехват сообщения (выполняется, если логфайла нет)

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"

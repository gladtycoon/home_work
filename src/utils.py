import json

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                    filename='logs/utils.log',
                    filemode='w'
                    )

def get_path_to_json_file(path: str) -> list[dict]:
    """Принимает путь до json-файла и возвращает список транзакций"""
    logger.info('Начало работы приложения...')
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            try:
                logger.info('Путь до json-файла корректный. Выполнение приложения...')
                transactions_list = json.load(json_file)
            except json.JSONDecodeError:
                logger.error('Ошибка содержания JSON-файла...')
                print("Ошибка содержания JSON-файла")
                transactions_list = []
    except FileNotFoundError:
        logger.error('Файл не найден...')
        print("Файл не найден")

    logger.info('Конец работы приложения...')
    return transactions_list



if __name__ == "__main__":
    path = "D:\\Projects\\home_work\\data\\operations.json"
    transactions_list = get_path_to_json_file(path)
    print(transactions_list)

import json
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename="D:/SkyPro/home_work/logs/utils.log",
    filemode="w",
)


def read_json_file(file_path: str) -> list[dict]:
    """ Принимает путь до json-файла и возвращает список транзакций """
    logger.info("Начало работы приложения...")

    try:
        transactions_list = json.load(open(file_path, "r", encoding="utf-8"))
        logger.info("Путь до json-файла корректный. Выполнение приложения...")
        transactions = []
        for transaction in transactions_list:
            id_ = transaction.get("id")
            state = transaction.get("state")
            amount = transaction.get("operationAmount", {}).get("amount")
            currency_name = transaction.get("operationAmount", {}).get("currency", {}).get("name")
            currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
            date = transaction.get("date")
            description = transaction.get("description")
            transactions.append({
                'id': transaction.get("id"),
                'state': transaction.get("state"),
                'date': transaction.get("date"),
                'amount': amount,
                'currency_name': currency_name,
                'currency_code': currency_code,
                'from': transaction.get("from"),
                'to': transaction.get("to"),
                'description': transaction.get("description")})
        logger.info("Конец работы приложения...")
        return transactions
    except Exception as e:
        print(f'Ошибка при обработке JSON-файла: {e}')
        return []

    # try:
    #     with open(file_path, "r", encoding="utf-8") as json_file:
    #         try:
    #             logger.info("Путь до json-файла корректный. Выполнение приложения...")
    #             transactions_list = json.load(json_file)
    #         except json.JSONDecodeError:
    #             logger.error("Ошибка содержания JSON-файла...")
    #             print("Ошибка содержания JSON-файла")
    #             transactions_list = []
    # except FileNotFoundError:
    #     logger.error("Файл не найден...")
    #     print("Файл не найден")
    #
    # logger.info("Конец работы приложения...")
    # return transactions_list


if __name__ == "__main__":
    path = "D:/SkyPro/home_work/data/operations.json"
    transactions_list = read_json_file(path)
    # print(transactions_list)
    # print(json.dumps(transactions_list, indent=2, ensure_ascii=False))

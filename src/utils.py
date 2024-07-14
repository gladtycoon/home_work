import json


def get_path_to_json_file(path: str) -> list[dict]:
    """Принимает путь до json-файла и возвращает список транзакций"""
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            try:
                transactions_list = json.load(json_file)
            except json.JSONDecodeError:
                print("Ошибка содержания JSON-файла")
                transactions_list = []
    except FileNotFoundError:
        print("Файл не найден")

    return transactions_list


if __name__ == "__main__":
    path = "D:\\Projects\\home_work\\data\\operations.json"
    transactions_list = get_path_to_json_file(path)
    print(transactions_list)

from typing import Any, Dict, List


def filter_by_state(list_of_data: List[Dict[str, Any]], condition: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Принимает список словарей и возвращает новый список словарей,
    у которых ключ содержит переданное в функцию значение"""
    filtered_list = []
    for data in list_of_data:
        if data["state"] == condition:
            filtered_list.append(data)
    return filtered_list


def sort_by_date(list_of_data: List[Dict[str, Any]], reverse_list: bool = True) -> List[Dict[str, Any]]:
    """Принимает список словарей и возвращает отсортированный по дате список"""
    sorted_list = sorted(list_of_data, key=lambda date_list: date_list["date"], reverse=reverse_list)
    return sorted_list


if __name__ == "__main__":
    test_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(test_data, "CANCELED"))
    print(sort_by_date(test_data, True))

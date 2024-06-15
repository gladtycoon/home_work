def mask_account_card(demask_number: str) -> str:
    """Маскирует номер счета или карты"""
    mask_number = ""
    count_digits = 0
    count_letters = 0
    count_spaces = 0
    for i in range(len(demask_number)):
        if demask_number[i].isalpha():
            mask_number += demask_number[i]
            count_letters += 1
        elif demask_number[i] == " ":
            mask_number += " "
            count_spaces += 1
        else:
            mask_number += demask_number[i]
            count_digits += 1
    if count_digits == 20:
        return f"{mask_number[:5]}**{mask_number[-4:]}"
    else:
        if count_spaces > 2:
            return f"{mask_number[:count_letters+1]} {mask_number[-19:-15]} **** **** {mask_number[-4:]}"
        else:
            return f"{mask_number[:count_letters+1]} {mask_number[-16:-12]} **** **** {mask_number[-4:]}"


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))


def get_data(date: str) -> str:
    """Принимает строку и возвращает форматированную дату"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


print(get_data("2018-07-11T02:26:18.671407"))

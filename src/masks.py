import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename="D:/SkyPro/home_work/logs/masks.log",
    filemode="w",
)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты"""
    logger.info("Начало работы приложения...")
    logger.info("Возвращаем замаскированный номер карты...")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета"""
    logger.info("Возвращаем замаскированный номер счета...")
    return f"**{account_number[-4:]}"


print(get_mask_account("73654108430135874305"))
logger.info("Конец работы приложения...")

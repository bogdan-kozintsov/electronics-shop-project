from src.item import Item
from config import *

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('ite.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(DAMAGED_ITEMS)
    # InstantiateCSVError: Файл item.csv поврежден

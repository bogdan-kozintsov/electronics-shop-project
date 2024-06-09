import csv
import os


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.args = args
        print(self.args)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.discount_level = 1.0
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.discount_level * self.quantity

    def apply_discount(self, pay_rate) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        return f"{self.__name}"

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            with open(file) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                count = 0
                item_all = []
                for row in reader:
                    if count == 0:
                        count += 1
                    else:
                        item_all.append(cls(row[0], row[1], row[2]))
            cls.all = item_all
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {file}')

        except IndexError:
            raise InstantiateCSVError(f'Файл {file} поврежден')

    @staticmethod
    # возвращаает число из числа-строки

    def string_to_number(value):
        return int(float(value))

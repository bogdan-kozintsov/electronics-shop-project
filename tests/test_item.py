"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
import os
import csv


@pytest.fixture
def position():
    return Item("Смартфон", 100, 1)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 100
    assert position.quantity == 1


def test_calculate_total_price(position):
    assert position.calculate_total_price() == 100


def test_apply_discount(position):
    Item.pay_rate = 0.8
    position.apply_discount(Item.pay_rate)
    assert position.price == 80


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_truncate():
    item = Item('Телефон', 25000, 3)
    item.name = 'Суперсмартфон'
    assert item.name == 'Суперсмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    test1 = Item.all[0]
    assert test1.name == "Смартфон"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

@pytest.fixture()
def item1():
    return Item("Смартфон", 10000, 20)

def test__repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test__str__(item1):
    assert str(item1) == 'Смартфон'
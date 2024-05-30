from src.item import Item
from src.phone import Phone

def test__str__():
    phone1 = Phone("Sony Xperia 1", 70000, 4, 2)
    assert str(phone1) == 'Sony Xperia 1'

def test__repr__phone():
    phone1 = Phone("Sony Xperia 1", 70000, 4, 2)
    assert repr(phone1) == "Phone('Sony Xperia 1', 70000, 4, 2)"

    assert phone1.number_of_sim == 2



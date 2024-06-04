from src.keyboard import Keyboard


def test_change_lang():
    kb = Keyboard('Logitech K480', 3399, 100)
    assert str(kb) == "Logitech K480"
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"

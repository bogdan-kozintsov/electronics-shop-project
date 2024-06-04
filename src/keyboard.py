from src.item import Item


class Mixin:
    _language: str = 'EN'

    def change_lang(self) -> None:
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'

    @property
    def language(self) -> str:
        return self._language


class Keyboard(Item, Mixin):
    pass

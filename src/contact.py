from dataclasses import dataclass


@dataclass
class Contact:
    """Класс данных - контакт"""

    name: str = ''
    phone: str = ''
    note: str = ''

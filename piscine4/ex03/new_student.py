import random
import string
from dataclasses import dataclass, field


def generate_id():
    return ''.join(random.choices(string.ascii_uppercase, k=15))


@dataclass
class Student:
    """

    """
    name: string
    surname: string
    active: bool = True
    id: string = field(init=False, default_factory=generate_id)
    login: string = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname

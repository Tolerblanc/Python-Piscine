from abc import ABC, abstractmethod


class Character(ABC):
    """
    abstract base class for characters
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for abstract base class. 
        Can't instantiate abstract base class directly.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Kill the character
        """
        self.is_alive = False


class Stark(Character):
    """
    I am Ironman?
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Stark class, inherits from Character
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Kill the character. Overrides Character.die()
        """
        super().die()

from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon class, inherits from Character
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Baratheon class, inherits from Character
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        String representation of Baratheon class
        """
        return f'({self.family_name}, {self.eyes}, {self.hairs})>'

    def __repr__(self):
        """
        Representation of Baratheon class
        """
        return f'({self.family_name}, {self.eyes}, {self.hairs})>'

    def die(self):
        """
        Kill the character. Overrides Character.die()
        """
        super().die()


class Lannister(Character):
    """
    Lannister class, inherits from Character
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Lannister class, inherits from Character
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        String representation of Lannister class
        """
        return f'({self.family_name}, {self.eyes}, {self.hairs})>'

    def __repr__(self):
        """
        Representation of Lannister class
        """
        return f'({self.family_name}, {self.eyes}, {self.hairs})>'

    def die(self):
        """
        Kill the character. Overrides Character.die()
        """
        super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Create a Lannister
        """
        return cls(first_name, is_alive)

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class, inherits from Baratheon and Lannister
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor for King class, inherits from Baratheon and Lannister
        """
        super().__init__(first_name, is_alive)

    # @property
    def get_eyes(self):
        """
        Get the eyes color of the character
        """
        return self.eyes

    # @property
    def get_hairs(self):
        """
        Get the hairs color of the character
        """
        return self.hairs

    # @eyes.setter
    def set_eyes(self, eyes):
        """
        Set the eyes color of the character
        """
        self.eyes = eyes

    # @hairs.setter
    def set_hairs(self, hairs):
        """
        Set the hairs color of the character
        """
        self.hairs = hairs

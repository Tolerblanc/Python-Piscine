class calculator:
    """
    calculator docstring
    """

    def __init__(self, vector: list[int | float]):
        """
        constructor docstring
        """
        self.vector = vector
        self.len = len(vector)

    def __repr__(self):
        """
        representation for vector
        """
        return f'{self.vector}'

    def __add__(self, object: int | float) -> None:
        """
        add operator docstring
        """
        for i in range(self.len):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object: int | float) -> None:
        """
        mul operator docstring
        """
        for i in range(self.len):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object: int | float) -> None:
        """
        sub operator docstring
        """
        for i in range(self.len):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object: int | float) -> None:
        """
        truediv operator docstring
        """
        try:
            for i in range(self.len):
                self.vector[i] /= object
            print(self.vector)
        except ZeroDivisionError:
            print('ZeroDivision: operand is zero')

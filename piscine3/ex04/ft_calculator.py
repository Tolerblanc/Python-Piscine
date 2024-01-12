class calculator:
    """
    calculator docstring
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """

        """
        print(f'Dot product is: {sum([a * b for a, b in list(zip(V1, V2))])}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        """
        print(f'Add Vector is: {[float(a + b) for a, b in list(zip(V1, V2))]}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        """
        print(
            f'Sous Vector is: {[float(a - b) for a, b in list(zip(V1, V2))]}')

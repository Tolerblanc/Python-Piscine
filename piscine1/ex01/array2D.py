import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice the list from start to end, and return the result

    Args:
        :param family (list): list of names
        :param start (int): start index
        :param end (int): end index

    Returns:
        list: sliced list

    Exceptions:
        ValueError: if start or end is not an integer
        IndexError: if start or end is out of range
    """
    try:
        np_family = np.array(family)
        sliced_family = np_family[start:end]
        print(f'My shape is : {np_family.shape}')
        print(f'My new shape is : {sliced_family.shape}')
        return sliced_family.tolist()
    except ValueError:
        print('ValueError: start or end is not an integer')
    except IndexError:
        print('IndexError: start or end is out of range')
    except Exception as e:
        print(e)

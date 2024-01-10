import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    np_family = np.array(family)
    sliced_family = np_family[start:end]
    print(f'My shape is : {np_family.shape}')
    print(f'My new shape is : {sliced_family.shape}')
    return sliced_family.tolist()

import numpy as np


def ft_invert(array: np.array) -> np.array:
    array = np.array(array)
    return 255 - array


def ft_red(array: np.array) -> np.array:
    array = np.array(array)
    red_array = array.copy()
    red_array[:, :, 1] = 0  # Zero out green
    red_array[:, :, 2] = 0  # Zero out blue
    return red_array


def ft_green(array: np.array) -> np.array:
    array = np.array(array)
    green_array = array.copy()
    green_array[:, :, 0] = 0  # Zero out red
    green_array[:, :, 2] = 0  # Zero out blue
    return green_array


def ft_blue(array: np.array) -> np.array:
    array = np.array(array)
    blue_array = array.copy()
    blue_array[:, :, 0] = 0  # Zero out red
    blue_array[:, :, 1] = 0  # Zero out green
    return blue_array


def ft_grey(array: np.array) -> np.array:
    # Assuming pre-computed weights for red, green, blue
    array = np.array(array)
    weight_red = 0.299
    weight_green = 0.587
    weight_blue = 0.114

    grey_array = np.dot(
        array[..., :3], [weight_red, weight_green, weight_blue])
    grey_array = grey_array.astype(np.uint8)
    return np.stack((grey_array,)*3, axis=-1)

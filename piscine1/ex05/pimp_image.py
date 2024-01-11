import numpy as np


def ft_invert(array: np.array) -> np.array:
    """
    invert the color of the image

    Args:
        array (np.array): image array

    Returns:
        np.array: inverted image array
    """
    array = np.array(array)
    return 255 - array


def ft_red(array: np.array) -> np.array:
    """
    keep only the red color of the image
    zero out the green and blue channel

    Args:
        array (np.array): image array

    Returns:
        np.array: red-filtered image array
    """
    array = np.array(array)
    red_array = array.copy()
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    return red_array


def ft_green(array: np.array) -> np.array:
    """
    keep only the green color of the image
    zero out the red and blue channel

    Args:
        array (np.array): image array

    Returns:
        np.array: green-filtered image array
    """
    array = np.array(array)
    green_array = array.copy()
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    return green_array


def ft_blue(array: np.array) -> np.array:
    """
    keep only the blue color of the image
    zero out the red and green channel

    Args:
        array (np.array): image array

    Returns:
        np.array: blue-filtered image array
    """
    array = np.array(array)
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    return blue_array


def ft_grey(array: np.array) -> np.array:
    """
    convert the image to grey scale
    map each pixel to green channel value

    Args:
        array (np.array): image array

    Returns:
        np.array: grey-scale image array
    """
    grey_array = array.copy()
    single_channel = grey_array[:, :, 1]

    grey_array[:, :, 0] = single_channel
    grey_array[:, :, 1] = single_channel
    grey_array[:, :, 2] = single_channel

    return grey_array

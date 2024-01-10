import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Load Image from path and transform into np.array

    Args:
        :param path: image file's path

    Returns:
        np.array that contains loaded image's RGB values

    Exceptions:
        Catches IOError when the file(or path) is invalid
    """
    try:
        img = Image.open(path)
        # img.show()
        img_vector = np.array(img)
        return img_vector
    except Exception as e:
        print(e)
        return []

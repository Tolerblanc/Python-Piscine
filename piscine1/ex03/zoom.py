import numpy as np
from load_image import ft_load
from PIL import Image


def main():
    """
    day01 ex03 main function
    load image, crop and resize it, then show it
    """
    try:
        origin = ft_load("../../assets/animal.jpeg")
        print(f'The shape of image is: {origin.shape}')
        print(origin)
        zoomed = Image.fromarray(origin).convert("L")
        zoomed = zoomed.crop((450, 100, 850, 500)).resize((400, 400))
        zoomed.show()
        zoomed_array = np.array(zoomed)
        print(f'New shape after slicing: {zoomed_array.shape}')
        print(zoomed_array)
    except Exception:
        print('failed to load image')


if __name__ == "__main__":
    main()

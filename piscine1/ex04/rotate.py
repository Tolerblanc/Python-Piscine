import numpy as np
from load_image import ft_load
from PIL import Image


def main():
    try:
        origin = ft_load("../../assets/animal.jpeg")
        zoomed = Image.fromarray(origin).convert("L")
        zoomed = zoomed.crop((450, 100, 850, 500)).resize((400, 400))
        zoomed_array = np.array(zoomed)
        print(f'The shape of image is: {zoomed_array.shape}')
        print(zoomed_array)

        transposed = np.array(
            list(zip(*zoomed_array.tolist()))).astype(np.uint8)
        print(transposed)
        Image.fromarray(transposed).show()

        print(f'New shape after Transpose: {transposed.shape}')

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

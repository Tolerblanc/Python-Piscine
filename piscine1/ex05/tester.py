from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red
from PIL import Image

array = ft_load("../../assets/landscape.jpeg")
Image.fromarray(ft_invert(array)).show()
Image.fromarray(ft_red(array)).show()
Image.fromarray(ft_green(array)).show()
Image.fromarray(ft_blue(array)).show()
Image.fromarray(ft_grey(array)).show()
print(ft_invert.__doc__)

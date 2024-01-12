def ft_mean(nums: list[int | float]) -> float:
    """
    get the float mean of a list of ints or floats

    Args:
        :param `nums (list[int | float])`: list of ints or floats

    Returns:
        `float`: mean of nums
    """
    return sum(nums) / len(nums)


def ft_median(nums: list[int | float]) -> int | float:
    """
    get the median of a list of ints or floats

    Args:
        :param `nums (list[int | float])`: list of ints or floats

    Returns:
        `(int | float)`: median of nums
    """
    lst = sorted(nums)
    center_idx = len(lst) // 2
    return lst[center_idx] if len(lst) % 2 == 1 \
        else (lst[center_idx] + lst[center_idx - 1]) / 2


def ft_quartile(nums: list[int | float]) -> list[int | float]:
    """
    get the 1Q and 3Q of a list of ints or floats
    uses Tukey's hinges method: https://en.wikipedia.org/wiki/Quartile#Method_2

    Args:
        :param `nums (list[int | float])`: list of ints or floats

    Returns:
        `list[int | float]`: 1Q and 3Q of nums
    """
    lst = sorted(nums)
    center_idx = len(lst) // 2
    left = lst[:center_idx] if len(lst) % 2 == 0 else lst[:center_idx + 1]
    right = lst[center_idx:]
    return [ft_median(left), ft_median(right)]


def ft_stddev(nums: list[int | float]) -> float:
    """
    get the standard deviation of a list of ints or floats

    Args:
        :param `nums (list[int | float])`: list of ints or floats

    Returns:
        `float`: standard deviation of nums
    """
    return ft_variance(nums) ** 0.5


def ft_variance(nums: list[int | float]) -> float:
    """
    get the variance of a list of ints or floats

    Args:
        :param `nums (list[int | float])`: list of ints or floats

    Returns:
        `float`: variance of nums
    """
    mean = ft_mean(nums)
    deviations = [num - mean for num in nums]
    return ft_mean([deviation ** 2 for deviation in deviations])


def ft_statistics(*args, **kwargs) -> None:
    """
    print the mean, median, 1Q, 3Q, standard deviation,
    and variance of a list of ints or floats
    """
    if len(args) == 0:
        print('ERROR')
        return
    for arg in args:
        if type(arg) not in (int, float):
            print('ERROR')
            return

    for value in kwargs.values():
        if value == "mean":
            print(f'mean : {ft_mean(args)}')
        elif value == "median":
            print(f'median : {ft_median(args)}')
        elif value == "quartile":
            print(f'quartile : {ft_quartile(args)}')
        elif value == "std":
            print(f'std : {ft_stddev(args)}')
        elif value == "var":
            print(f'var : {ft_variance(args)}')

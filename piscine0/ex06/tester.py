from ft_filter import ft_filter


def main():
    """
    ex06-1 ft_filter test with original filter
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('Case1: filter odds')
    print('----- original filter -----')
    print(filter(lambda x: x % 2, nums))
    print(list(filter(lambda x: x % 2, nums)))
    print('---------------------------')
    print('-----    ft filter    -----')
    print(ft_filter(lambda x: x % 2, nums))
    print(list(ft_filter(lambda x: x % 2, nums)))
    print('---------------------------')
    print()

    print('Case2: filter evens')
    print('----- original filter -----')
    print(filter(lambda x: not x % 2, nums))
    print(list(filter(lambda x: not x % 2, nums)))
    print('---------------------------')
    print('-----    ft filter    -----')
    print(ft_filter(lambda x: not x % 2, nums))
    print(list(ft_filter(lambda x: not x % 2, nums)))
    print('---------------------------')
    print()

    print('Case3: filter multiples of 3')
    print('----- original filter -----')
    print(filter(lambda x: not x % 3, nums))
    print(list(filter(lambda x: not x % 3, nums)))
    print('---------------------------')
    print('-----    ft filter    -----')
    print(ft_filter(lambda x: not x % 3, nums))
    print(list(ft_filter(lambda x: not x % 3, nums)))
    print('---------------------------')
    print()


if __name__ == "__main__":
    main()

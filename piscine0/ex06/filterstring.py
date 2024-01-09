from ft_filter import ft_filter
import sys


def main():
    """
    ex06-2 main function
    split the string by spaces and filter the words whose length is greater than N # noqa: E501
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        S = sys.argv[1].split()
        N = int(sys.argv[2])
        print([word for word in ft_filter(lambda x: len(x) > N, S)])
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()

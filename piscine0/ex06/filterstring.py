from ft_filter import ft_filter
import sys


def main():
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

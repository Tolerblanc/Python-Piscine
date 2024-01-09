import sys


def count_characters(string: str) -> None:
    """
    count uppercase letters, lowercase letters, punctuation marks, spaces and digits

    Args:
        @param `string`: str to count

    Returns:
        None

    Exception:
        Never Raised.
    """
    punctuation = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    print(f'The text contains {len(string)} characters:')
    print(f'{sum(1 for s in string if s.isupper())} upper letters')
    print(f'{sum(1 for s in string if s.islower())} lower letters')
    print(f'{sum(1 for s in string if s in punctuation)} punctuation marks')
    print(f'{sum(1 for s in string if s.isspace())} spaces')
    print(f'{sum(1 for s in string if s.isdigit())} digits')


def main():
    """
    main function for ex05.
    check argv length and get string, put it as a parameter.
    """
    if len(sys.argv) >= 3:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 2:
        count_characters(sys.argv[1])
        return

    print("What is the text to count?")
    try:
        buffer = input()
    except EOFError:
        pass
    count_characters(buffer)


if __name__ == "__main__":
    main()

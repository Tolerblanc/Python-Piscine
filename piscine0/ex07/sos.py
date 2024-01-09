import sys


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    morse_code = ''
    NESTED_MORSE = {
        ' ': '/ ',
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
        'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
        'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ',
        'Z': '--.. ',

        '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. '
    }

    for character in sys.argv[1]:
        if character.capitalize() not in NESTED_MORSE:
            print("AssertionError: the arguments are bad")
            return
        morse_code += NESTED_MORSE[character.capitalize()]
    print(morse_code[0:-1])


if __name__ == "__main__":
    main()

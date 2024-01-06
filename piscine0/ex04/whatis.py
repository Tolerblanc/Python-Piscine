import sys

if len(sys.argv) >= 3:
    print("AssertionError: more than one argument is provided")

try:
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
        print("I'm Even." if num % 2 == 0 else "I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")

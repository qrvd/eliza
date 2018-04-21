#!/usr/bin/env python
# This is a Python 3 script!

def respond(text):

    words = text.split()

    # Decompose
    # Match to keywords
    # Pick the most specific rule
    # Transform the text to match that rule.

    return "I understand..."


def main():

    # The user may stop the program using Ctrl-C.
    while True:
        text = raw_input('> ')
        response = respond(text)
        print(response)

# We don't need to run the main() function if
# the code is being imported as a library.
if __name__ == "__main__":
    main()

#!/usr/bin/python3
def text_indentation(text):
    """This module prints a text with 2 new lines after each of these
    characters: ., ? and :
    Args:
        text (str): string to print
    Raises:
        TypeError: test must be a string
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")

    i = 0
    for _ in range(len(text)):
        if (i <= len(text) - 1):
            print(text[i], end="")
            if (text[i] == "." or text[i] == "?" or text[i] == ":"):
                print()
                print()
                if (i < len(text) - 1 and text[i + 1] == " "):
                    i += 1
                    while (text[i] == " "):
                        i += 1
                else:
                    i += 1
            else:
                i += 1
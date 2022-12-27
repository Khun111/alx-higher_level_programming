#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    lines = text.split('\n')
    for line in lines:
        words = line.split()
        for i, word in enumerate(words):
            if word[-1] in ['.', ':', '?']:
                print(word[:-1], end='\n\n')
            else:
                print(word, end=' ')
        print()

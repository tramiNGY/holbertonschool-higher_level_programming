#!/usr/bin.python3
'''
The 5-text_indentation module supplies one function text_indentation.
It permits to print a tet with 2 new lines after each of those characters:
., ? and :
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text is None:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in '.?:':
            print("{}".format(text[i]), end='')
            print()
            print()
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            print("{}".format(text[i]), end='')
        i += 1

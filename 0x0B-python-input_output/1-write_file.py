#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 1. Write to a file """


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written. Overwrites if existing content.

    Args:
        filename (str): name of file to be opened
        text (str): chars to be written

    """
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written

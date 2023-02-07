#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 5. Save Object to a file  """

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj (any): object to be serialized
        filename (any): File pointer to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

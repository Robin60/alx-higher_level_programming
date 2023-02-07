#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 4. From JSON string to Object  """

import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.
    Args:
        my_obj (any): Serialized object to be deserialized
    Return:
        Deserialized object
    """
    return json.loads(my_str)

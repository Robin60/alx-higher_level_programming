#!/usr/python3
"""Python inheritance"""


class MyList(List):
    """MyList inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort) """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)

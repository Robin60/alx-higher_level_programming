#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 7. Load, add, save  """


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argvs = argv[1:]

try:
    contents = load_from_json_file("add_item.json")
except Exception:
    contents = []
finally:
    for arg in argvs:
        contents.append(arg)
    save_to_json_file(contents, "add_item.json")

#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to URL"""

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {'q': q}
    response = requests.post(url, data=query)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            obj = response.json()
            if len(obj) == 0:
                print('No result')
                sys.exit()
            _id = obj.get('id')
            name = obj.get('name')
            print("[{}] {}".format(_id, name))
        except ValueError as invalid_json:
            print('Not a valid JSON')

#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
   of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY \
            id ASC", (sys.argv[4], ))
    rows = cursor.fetchall()
    [print(row) for row in rows]
    cursor.close()
    con.close()

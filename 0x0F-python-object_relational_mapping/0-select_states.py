#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                        passwd=argv[2], db=argv[3], charset='utf8')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    [print(row) for row in rows]
    cursor.close()
    con.close()

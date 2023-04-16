#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    if len(sys.argv) != 4:
        sys.exit('Use: 0-select_states.py <mysql username> <mysql password>'
                 '<database name>')
    con = MySQL.connect(host='localhost', port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cursor = con.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities as c LEFT JOIN "
                   "states as s ON c.states.id = states.id;")
    rows = cursor.fetchall()
    [print(row) for row in rows]
    cursor.close()
    con.close()

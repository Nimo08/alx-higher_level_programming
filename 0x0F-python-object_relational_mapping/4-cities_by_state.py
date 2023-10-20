#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    #  prevent sql injection
    query = """SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states
    ON cities.state_id = states.id ORDER BY id ASC"""
    cur.execute(query)
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    conn.close()

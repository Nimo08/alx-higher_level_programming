#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state, using the database
hbtn_0e_4_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    #  prevent sql injection
    query = """SELECT cities.name FROM cities INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE _utf8mb4 %s COLLATE utf8mb4_0900_as_cs
    ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    if query_rows:
        res = ', '.join(row[0] for row in query_rows)
        print(res)
    cur.close()
    conn.close()

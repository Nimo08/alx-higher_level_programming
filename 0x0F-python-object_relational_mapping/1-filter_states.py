#!/usr/bin/python3
"""
Lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
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
    cur.execute("""SELECT id, name FROM states
                WHERE name LIKE _utf8mb4 'N%' COLLATE utf8mb4_0900_as_cs
                ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

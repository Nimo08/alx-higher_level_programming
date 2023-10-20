#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    #  prevent sql injection
    query = "SELECT id, name FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, (state_name_searched,))
    query_row = cur.fetchone()
    if query_row:
        print(query_row)
    cur.close()
    conn.close()

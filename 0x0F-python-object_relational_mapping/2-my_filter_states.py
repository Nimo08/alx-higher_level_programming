#!/usr/bin/python3
"""
Takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
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

    user_query = """SELECT id, name FROM states
    WHERE name = %s ORDER BY id ASC"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute(user_query, ('{}%'.format(state_name_searched),))
    query_row = cur.fetchone()
    if query_row:
        print(query_row)
    cur.close()
    conn.close()

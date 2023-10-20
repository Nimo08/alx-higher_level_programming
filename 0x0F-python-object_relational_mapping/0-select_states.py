#!/usr/bin/python3
import MySQLdb
import sys


"""
Takes 3 arguments: mysql username, mysql password and
database name (no argument validation needed)
Connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by states.id
Code should not be executed when imported
"""


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    """
    Connects to a MySQL server running on localhost at port 3306
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name,
                           charset="utf8")
    """
    Cursor object to interact with database
    """
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

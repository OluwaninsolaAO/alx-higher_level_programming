#!/usr/bin/python3
"""Safely Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument."""


if __name__ == '__main__':
    import sys
    import MySQLdb

    _, user, passwd, db, name = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         password=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s \
                ORDER BY states.id ASC", (name,))
    for row in cur.fetchall():
        print(row)

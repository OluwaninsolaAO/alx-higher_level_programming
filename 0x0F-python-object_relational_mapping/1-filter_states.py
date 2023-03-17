#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    _, user, passwd, db = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
            password=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%'")
    for row in cur.fetchall():
        print(row)

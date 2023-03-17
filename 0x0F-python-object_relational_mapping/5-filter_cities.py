#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    _, user, passwd, db, state = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         password=passwd, db=db)
    cur = db.cursor()
    num = cur.execute("SELECT cities.name FROM cities INNER JOIN\
                      states on cities.state_id = states.id WHERE\
                      states.name = %s ORDER BY cities.id ASC", (state,))
    for row in cur.fetchall():
        print('{}'.format(row[0]), end='')
        if num != 1:
            print(', ', end='')
            num -= 1
    print()
    cur.close()
    db.close()

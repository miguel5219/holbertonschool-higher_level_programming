#!/usr/bin/python3
""" script that list all cities from database """

import MySQLdb
from sys import argv


def cities_state():
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    if ';' in argv[4]:
        return

    cur_ =db.cursor()
    query_ = "SELECT t1.id, t1.name, t2.name \
              FROM cities t1 \
              LEFT JOIN states t2 \
              ON t1.state_id = t2.id \
              WHERE t2.name = '{}' \
              ORDER BY t1.id ASC".format(argv[4])
    cur_.execute(query_)

    rows = cur_.fetchall()
    for i, row in enumerate(rows)
        if i > 0:
            print(', ',  end="")
        print(row[1], end="")
    print()

    db.close()


if __name__ == "__main__":
    cities_state()

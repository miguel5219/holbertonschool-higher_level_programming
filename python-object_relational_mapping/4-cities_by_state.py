#!/usr/bin/python3
""" module contains the function cities_state """

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

    cur_ = db.cursor()
    query_ = "SELECT t1.id, t1.name, t2.name \
              FROM cities t1 \
              LEFT JOIN states t2 \
              ON t1.state_id = t2.id \
              ORDER BY t1.id ASC"
    cur_.execute(query_)

    rows = cur_.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    cities_state()

#!/usr/bin/python3
""" module lists all states from the database htbn_0e_0_usa sorted
in ascending order by states.id """

import MySQLdb
from sys import argv


def _filter_states():
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cur_ = db.cursor()
    query_ = "SELECT id, name FROM states WHERE BINARY name ='{}' \
              ORDER BY states.id ASC".format(argv[4])
    cur_.execute(query_)

    rows = cur_.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    _filter_states()

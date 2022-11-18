#!/usr/bin/python3
""" module contains the function safe_filter_states
"""

import MySQLdb
from sys import argv


def safe_filter_states():
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    if 'i' in argv[4]:
        return

    cur_ = db.cursor()
    query_ = "SELECT id, name FROM states WHERE BINARY name = '{}' \
              ORDER BY states.id ASC".format(argv[4])
    cur_.execute(query_)

    rows = cur_.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    safe_filter_states()

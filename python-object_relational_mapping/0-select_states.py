#!/usr/bin/python3
""" this module listas all states from database
hbtn_0e_0_usa sorted in ascendiing order by
states.id """

import MySQLdb
from sys import argv


def MySQLconnect():
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password='',
        database=argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()
    for col in rows:
        print(col)

    db.close()


if __name__ == "__main__":
    MySQLconnect()

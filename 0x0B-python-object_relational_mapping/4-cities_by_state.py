#!/usr/bin/python3
"""lists all cities from database"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities, states\
                WHERE states.id = state_id\
                ORDER BY id ASC")
    poopla = cur.fetchall()
    for x in poopla:
        print(x)
    cur.close()
    db.close()

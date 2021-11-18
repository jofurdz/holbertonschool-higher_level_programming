#!/usr/bin/python3
"""takes arguments and displays all values that match"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, userName=argv[1],
                         password=argv[2], dataBase=argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = %(name)s\
         ORDER BY states.id ASC", {'name': argv[4]})
    poopla = cur.fetchall()
    for x in poopla:
        print(x)
    cur.close
    db.close()

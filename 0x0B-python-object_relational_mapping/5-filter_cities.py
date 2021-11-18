#!/usr/bin/python3
"""takes name of state as arg and lists all cities of state"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT cities.name, states.name\
         FROM cities INNER JOIN states ON cities.state_id = states.id\
         ORDER BY cities.id ASC")
    poopla = cur.fetchall()
    
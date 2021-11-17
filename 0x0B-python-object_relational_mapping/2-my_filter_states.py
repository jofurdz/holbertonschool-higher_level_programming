#!/usr/bin/python3
"""takes an argument and displays all values in the states table"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, userName=argv[1],
                         password=argv[2], dataBase=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE BINARY name = '{}'\
                ORDER BY id ASC".format(argv[4]))
    poopla = cur.fetchall()
    for x in poopla:
        print(x)

    cur.close()
    conn.close()

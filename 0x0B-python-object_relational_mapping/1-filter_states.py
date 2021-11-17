#!/usr/bin/python3
"""lists all states with N from database"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, userName=argv[1],
                         password=argv[2], dataBase=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    poopla = cur.fetchall()
    for x in poopla:
        if x[1].startswith('N'):
            print(x)
    cur.close()
    conn.close()

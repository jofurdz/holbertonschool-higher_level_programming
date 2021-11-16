#!/usr/bin/python3
"""lists all states from database"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, userName=argv[1],
                         passWord=argv[2], dataBase=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    poopla = cursor.fetchall()
    for x in poopla:
        print(x)

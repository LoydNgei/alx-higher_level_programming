#!/usr/bin/python3


""" write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""

import MySQLdb
import sys

if __name__ == '__main__':

    mydb = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
            )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY states.id ASC", {'name': sys.argv[4]})

    rows_inside = mycursor.fetchall()

    for row in rows_inside:
        print(row)

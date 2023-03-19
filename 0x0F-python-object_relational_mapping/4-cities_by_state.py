#!/usr/bin/python3

""" a script that lists all cities from the database hbtn_0e_4_usa"""

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

    mycursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
    rows_selected = mycursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)

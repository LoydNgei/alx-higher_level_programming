#!/usr/bin/python3

"""A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

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

    mycursor.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name %s\
            ORDER BY cities.id", (sys.argv[4], ))
    rows_selected = mycursor.fetchall()
    print(", ".join([row[0] for row in rows_selected]))

    mycursor.close()
    mydb.close()

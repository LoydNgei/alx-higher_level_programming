#!/usr/bin/python3

"""A script that lists all states from the database 'hbtn_0e_0_usa'
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

    mycursor.execute("SELECT * FROM states")

    rows_inside = mycursor.fetchall()

    for row in rows_inside:
        print(row)

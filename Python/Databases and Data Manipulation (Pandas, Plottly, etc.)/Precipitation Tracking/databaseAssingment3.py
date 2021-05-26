'''
Author: Brogan Avery
Date: 2020/10/13
Project Title: edit tables
'''

import csv
import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return conn

def get_rows():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Precipitation")
    rows = cur.fetchall() # list of row tuples
    return rows

def update_precipitation(updatedRow):
    cur = conn.cursor()
    cur.execute('UPDATE Precipitation SET precipitation=? WHERE date=? AND location=?', updatedRow)

def update_date(updatedRow):
    cur = conn.cursor()
    cur.execute('UPDATE Precipitation SET date=? WHERE date=?', updatedRow)

def delete_county():
    cur = conn.cursor()
    cur.execute("DELETE FROM Location WHERE county = 'Travis'")
    cur.execute("DELETE FROM Precipitation WHERE location = 'Travis'")

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

    conn = create_connection("weather_tracking.db")
    with conn:
        rows = get_rows()


# change precipitation
        updatedRows = []
        for row in rows:
            rainInMm = row[0] * 25.4
            updatedRows.append((rainInMm, row[1], row[3]))

        for row in updatedRows:
            update_precipitation(row)


# change date

        currentDates = []
        for row in rows:
            currentDates.append(row[1])

        newDates = ['5/31/16']
        for i in range(1,30):
            newDates.append('6/' + str(i) + '/16')

        oldAndNewDates = []
        for i in range(30):
            oldAndNewDates.append((newDates[i],currentDates[i]))

        for row in oldAndNewDates:
            update_date(row)

#delete country
        delete_county()

    conn.commit()
    conn.close()
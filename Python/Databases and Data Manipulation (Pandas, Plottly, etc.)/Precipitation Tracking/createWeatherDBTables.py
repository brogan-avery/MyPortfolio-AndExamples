'''
Author: Brogan Avery
Date: 2020/10/08
Project Title: Weather database table creation
'''

import sqlite3
from sqlite3 import Error

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

    return conn  # connection object


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

    database = "weather_tracking.db"

# declare tables
    createPrecipitationTable = """ CREATE TABLE IF NOT EXISTS Precipitation (
                                            precipitation float,
                                            date text,
                                            precip_type text,
                                            location text,
                                            PRIMARY KEY(date,location),
                                            FOREIGN KEY (location) 
                                                REFERENCES Location (county)
                                        ); """

    createLocationTable = """CREATE TABLE IF NOT EXISTS Location (
                                        county text PRIMARY KEY,
                                        state text
                                    );"""

# create connection and database if it doesn't already exist
    conn = create_connection(database)

# create tables
    if conn is not None:
        create_table(conn, createPrecipitationTable)
        create_table(conn, createLocationTable)
    else:
        print("Error! cannot create the database connection.")

    with sqlite3.connect('weather_tracking.db') as db:
        newline_indent = '\n   '

        cur = db.cursor()

        result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        table_names = sorted(list(zip(*result))[0])
        print("\ntables are:" + newline_indent + newline_indent.join(table_names))

        for table_name in table_names:
            result = cur.execute("PRAGMA table_info('%s')" % table_name).fetchall()
            column_names = list(zip(*result))[1]
            print(("\ncolumn names for %s:" % table_name)
                  + newline_indent
                  + (newline_indent.join(column_names)))
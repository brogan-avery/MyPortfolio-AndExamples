"""
***************************************************
Title: Add to database
Author: Brogan Avery
Created: 2020-10-27
Description : Creates or opens a database connection and table. Adds data from the Roman Coin CSV file into the database.
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

import sqlite3
from sqlite3 import Error
import csv

def create_connection(database):
    conn = None #connection object
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_record(conn,newRow):
    sql = ''' REPLACE INTO Coins(CoinId,Deity,Denomination,Material,Mint,FrontDescription,Portrait,Region,BackDescription,Year)
                  VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, newRow)

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

    # declare table(s)
    createCoinTable = """ CREATE TABLE IF NOT EXISTS Coins (
                                                CoinId text,
                                                Deity text,
                                                Denomination text,
                                                Material text,
                                                Mint text,
                                                FrontDescription text,
                                                Portrait text,
                                                Region text,
                                                BackDescription text,
                                                Year text,
                                                PRIMARY KEY(CoinId)
                                                
                                            ); """

# create database connection if it doesn't already exist
    conn = create_connection("romanCoin.db")

# create tables if none exist
    if conn is not None:
        create_table(conn, createCoinTable)

    else:
        print("Error! cannot create the database connection.")

# prepare data from the csv file to add to database table
    with open('RomanCoins.csv') as input_file:
        tableData = csv.DictReader(input_file)
        allRows = [(row['CoinId'],row['Deity'],row['Denomination'],row['Material'],row['Mint'],row['FrontDescription'],row['Portrait'],row['Region'],row['BackDescription'],row['Year']) for row in tableData]

# add the list of all the row tuples to the database tables
    conn = create_connection("romanCoin.db")
    with conn:
        for row in allRows:
            add_record(conn,row)
    conn.commit()
    conn.close()



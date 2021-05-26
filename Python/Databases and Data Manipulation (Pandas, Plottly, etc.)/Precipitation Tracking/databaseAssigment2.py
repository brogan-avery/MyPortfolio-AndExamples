'''
Author: Brogan Avery
Date: 2020/10/08
Project Title: insert weather data into tableDatas
'''

import csv
import sqlite3
from sqlite3 import Error
import pandas as pd
from matplotlib.pyplot import *

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return conn

def add_record_to_precipitation_table(conn,newRow):
    sql = ''' REPLACE INTO Precipitation(precipitation,date,precip_type,location)
                  VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, newRow)

def add_record_to_location_table(conn,newRow):
    sql = ''' REPLACE INTO Location(county,state)
                  VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, newRow)

def create_dataframe():
    df = pd.read_sql_query("SELECT p.date, p.location, l.state, p.precipitation FROM Precipitation p INNER JOIN  Location l on p.location = l.county", sqlite3.connect('weather_tracking.db'))
    df.columns = ['date', 'county', 'state', 'rain fall (inches)']
    return df

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

# prepare data from travis county csv table to add to database tables 'Precipitation' and 'Location'
    with open('TravisCounty.csv') as input_file:
        tableData = csv.DictReader(input_file)
        allRowsTravis = [(row['PrecipitationSumInches'],row['Date'],'rain', 'Travis') for row in tableData]

# prepare data from New York county csv table to add to database tables 'Precipitation' and 'Location'
    with open('NewYorkCounty.csv') as input_file:
        tableData = csv.DictReader(input_file)
        allRowsNewYork = [(row['precipitation'],row['date'],'rain', 'New York') for row in tableData]

    allRowsBoth = allRowsTravis + allRowsNewYork

# make a list of tuples to go into the location table
    allLocationRows = [('Travis','Texas'),('New York','New York')]

# add the list of all the row tuples to the database tables
    conn = create_connection("weather_tracking.db")
    with conn:
        for row in allRowsBoth:
            add_record_to_precipitation_table(conn,row)
        for row in allLocationRows:
            add_record_to_location_table(conn,row)
    conn.commit()
    conn.close()

# create dataframe from database data
    df = create_dataframe()
    print(df)

# create visual

    travisCountyRecords = df[df['county'] == "Travis"]
    newYorkCountyRecords = df[df['county'] == "New York"]

    x1 = list(travisCountyRecords['date'])
    x2 = list(newYorkCountyRecords['date'])

    y1 = list(travisCountyRecords['rain fall (inches)'])
    y2 = list(newYorkCountyRecords['rain fall (inches)'])


    fig, ax = subplots()
    ax.plot(x1,y1, 'red')
    ax.plot(x2,y2, 'blue')

    ax.set_title('Avg Daily Rain Fall for June 2016')
    ax.legend(['Travis County, TX','New York County, NY'])
    ax.yaxis.set_label_text('Rain Fall (inches)')
    xticks(rotation='vertical')

    show()




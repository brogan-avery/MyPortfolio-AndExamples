"""
***************************************************
Title: Pandas Demo
Author: Brogan Avery
Created: 2020-09-17
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

from pandas import *
from numpy import *
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

    dict = {'Day_of_week' : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'Max temp' : [47,44,33,34,30,29,45], 'Min temp' : [36,30,27,30,16,12,24]}
    df1 = DataFrame(data=dict)

    print('Dataframe 1:\n',df1)

    print('\nInfo for dataframe 1:\n',df1.describe())

    dict2 = {'Day_of_week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],'Precip': [0.21, 0.01, 0, 0.01, 0.01, 0, 0], 'New Snow': [0, 0, 0, 0.1, 0.3, 0, 0]}
    df2 = DataFrame(data=dict2)

    df3 = merge(df1, df2, on = 'Day_of_week')
    print('\nJoined data frames (df1 and df2):\n',df3)

    df3.set_index('Day_of_week', inplace=True)
    print('\nChanged the primary key/index col:\n', df3)

    df3['Max temp'] = round(((df3['Max temp'] -32)* 5 / 9), 2)
    df3['Min temp'] = round(((df3['Min temp'] - 32) * 5 / 9),2)
    print('\nUpdated to Celsius:\n', df3)

    # uses the already rounded values that are in the max temp and min temp col
    df3['Avg temp'] = round(((df3['Max temp'] * df3['Min temp']) / 2),2)
    column_names = ['Max temp', 'Min temp', 'Avg temp', 'Precip', 'New Snow']
    df3 = df3.reindex(columns = column_names)
    print('\nAdded Avg column after the min column:\n', df3)

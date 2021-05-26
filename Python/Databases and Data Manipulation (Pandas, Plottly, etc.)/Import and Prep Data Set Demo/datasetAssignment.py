'''
Author: Brogan Avery
Date: 2020/09/25
Project Title: import and prep dataset
'''
from pandas import *
from numpy import *

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
    df = read_csv("steam.csv", sep=',')

    publishers = df.groupby('publisher')['positive_ratings'].sum().reset_index()

    publishers.columns = ['publisher','totalPositiveRatings']

    publishersToDelete = publishers[publishers['totalPositiveRatings']<50]

    publishersToDeleteList = []

    for publisher in publishersToDelete['publisher']:
        publishersToDeleteList.append(publisher)

    df2 = df[~df['publisher'].isin(publishersToDeleteList)]

    df2 = df2.sort_values(by='positive_ratings', ascending=False)

    print(df2.describe())

    df2 = df2.drop(columns = ['appid'])

    rowsToDrop = df2[df2['owners'] == '0-20000'].index
    df2 = df2.drop(rowsToDrop)

    print(df2)














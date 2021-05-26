'''
Author: Brogan Avery
Date: 2020/09/25
Project Title: import and prep dataset part 2
'''
from pandas import *
from numpy import *

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
# copy of code (without the print statements and squished closer together) from part one to get the df2 data frame to start the second assignment with
    df = read_csv("steam.csv", sep=',')
    publishers = df.groupby('publisher')['positive_ratings'].sum().reset_index()
    publishers.to_csv('idk2.csv')
    publishers.columns = ['publisher', 'totalPositiveRatings']
    publishersToDelete = publishers[publishers['totalPositiveRatings'] < 50]
    publishersToDeleteList = []
    for publisher in publishersToDelete['publisher']:
        publishersToDeleteList.append(publisher)
    df2 = df[~df['publisher'].isin(publishersToDeleteList)]
    df2 = df2.sort_values(by='positive_ratings', ascending=False)
    df2 = df2.drop(columns=['appid'])
    rowsToDrop = df2[df2['owners'] == '0-20000'].index
    df2 = df2.drop(rowsToDrop)

# part two (new code for this assignment)

#owners df
    ratingsByOwnerDf = df2[['owners','positive_ratings', 'negative_ratings']]
    ratingsByOwnerDf = ratingsByOwnerDf.groupby('owners').sum().reset_index()

    s = ratingsByOwnerDf['owners'].str.len().sort_values().index
    ratingsByOwnerDf = ratingsByOwnerDf.reindex(s)
    ratingsByOwnerDf = ratingsByOwnerDf.reset_index(drop=True)

    print(ratingsByOwnerDf)

    ratingsByOwnerDf['positive_ratings_percentage'] = (round((ratingsByOwnerDf.positive_ratings / (ratingsByOwnerDf.negative_ratings + ratingsByOwnerDf.positive_ratings)) * 100,0)).astype(int)
    ratingsByOwnerDf['negative_ratings_percentage'] = (round((ratingsByOwnerDf.negative_ratings / (ratingsByOwnerDf.negative_ratings + ratingsByOwnerDf.positive_ratings)) * 100,0)).astype(int)

    ratingsByOwnerDf = ratingsByOwnerDf[['owners','positive_ratings','positive_ratings_percentage','negative_ratings', 'negative_ratings_percentage']]

    print(ratingsByOwnerDf)

    ratingsByOwnerDf = ratingsByOwnerDf.sort_values(by='positive_ratings_percentage',ascending=False)

#publishers df
    ratingsByPublisherDf = df2[['publisher','positive_ratings', 'negative_ratings']]
    ratingsByPublisherDf = ratingsByPublisherDf.groupby('publisher').sum().reset_index()

    print(ratingsByPublisherDf)

    ratingsByPublisherDf['positive_ratings_percentage'] = (round((ratingsByPublisherDf.positive_ratings / (ratingsByPublisherDf.negative_ratings + ratingsByPublisherDf.positive_ratings)) * 100,0)).astype(int)
    ratingsByPublisherDf['negative_ratings_percentage'] = (round((ratingsByPublisherDf.negative_ratings / ( ratingsByPublisherDf.negative_ratings + ratingsByPublisherDf.positive_ratings)) * 100,0)).astype(int)

    ratingsByPublisherDf = ratingsByPublisherDf[['publisher','positive_ratings','positive_ratings_percentage','negative_ratings', 'negative_ratings_percentage']]

    print(ratingsByPublisherDf)

    ratingsByPublisherDf = ratingsByPublisherDf.sort_values(by='positive_ratings_percentage',ascending=False)

    print(ratingsByPublisherDf)

    ratingsByPublisherDf = ratingsByPublisherDf[ratingsByPublisherDf['positive_ratings'] > 999]

    print(ratingsByPublisherDf)

    games = df[['name', 'publisher']]

    publishers = []
    for publisher in ratingsByPublisherDf['publisher']:
        publishers.append(publisher)

    games = games[games['publisher'].isin(publishers)]

    games = games.groupby('publisher')['name'].count().reset_index()

    games = games[games['name'] > 4]

    publishers = []
    for publisher in games['publisher']:
        publishers.append(publisher)

    ratingsByPublisherDf = ratingsByPublisherDf[ratingsByPublisherDf['publisher'].isin(publishers)]

    print(ratingsByPublisherDf)




















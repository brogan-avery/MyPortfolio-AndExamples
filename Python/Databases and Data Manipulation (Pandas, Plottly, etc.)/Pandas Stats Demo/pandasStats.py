'''
Author: Brogan Avery
Date: 2020/09/20
Project Title:
'''

from pandas import *
from numpy import *
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
    df = read_csv("ign.csv", sep=',')

    print('Shape of dataframe:\n', df.shape)

    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

   # entity pk: col - empty entity means all
    print('\ntitle,genre, and release year: \n', df.loc[:,['title','genre', 'release_year']])

    print('for column scores:')

    print('     mean: ', round(df['score'].mean(),2))
    print('     max: ', df['score'].max())
    print('     standard deviation: ', round(df['score'].std(),2))

    df['score'] = df['score'] * 10
    print('\nupdated score column:\n', df['score'])

    df2 = df[df['score']>(df['score'].mean())]
    print(df2)

    print(df2['platform'].value_counts())


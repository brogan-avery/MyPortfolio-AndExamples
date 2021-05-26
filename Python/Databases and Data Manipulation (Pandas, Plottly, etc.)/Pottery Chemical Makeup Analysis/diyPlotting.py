'''
Author: Brogan Avery
Date: 2020/10/05
Project Title: DIY plotting with matplotlib
'''
from matplotlib.pyplot import *
from pandas import *
from numpy import *
from operator import truediv

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

    df0 = read_csv("xrf.csv", sep=',')

# Simple visual

    # DESCRIPTION: The dataset is a collection of ceramic pottery sherds from an archaeological site in Asia.
    # The dataset looked at 11 different periodic elements to determine how common each element is in the composition of each sherd.
    # The graph shows the total amounts of each of the 11 elements in parts per million for all sherds at the site.

    baTotal = df0['Ba'].sum()
    zrTotal = df0['Zr'].sum()
    srTotal = df0['Sr'].sum()
    rbTotal = df0['Rb'].sum()
    znTotal = df0['Zn'].sum()
    niTotal = df0['Ni'].sum()
    feTotal = df0['Fe'].sum()
    mnTotal = df0['Mn'].sum()
    tiTotal = df0['Ti'].sum()
    caTotal = df0['Ca'].sum()
    kTotal = df0['K'].sum()

    dict = {'element': ['Ba', 'Zr', 'Sr', 'Rb', 'Zn', 'Ni', 'Fe','Mn','Ti','Ca','K'],
            'elementTotal': [baTotal,zrTotal,srTotal,rbTotal,znTotal,niTotal,feTotal,mnTotal,tiTotal,caTotal,kTotal]}
    df1 = DataFrame(data=dict)

    # print(df1)

    ax = df1.plot.bar(x='element', y='elementTotal', rot=0, title ='Ceramic Sherd Elemental Composition')

    show()

# more complex visual

    # DESCRIPTION: In the more complex table, I am still looking at the elemental composition but I have grouped it by the ceramic sherds classified as utilitarian or non utilitarian to see if that has any correlation to the elements found in the sherds.
    # utilitarian pottery is the plain and basic type of containers that people use in their everyday life for cooking, water, etc. non-utilitarian is pottery that is decorated and detailed and holds some sort of intrinsic value for rituals, ceremonies, etc.

    df0 = df0.replace({'Group': {'G1': 'non-utilitarian', 'G2': 'utilitarian', 'G3': 'utilitarian', 'G4': 'utilitarian'}}) # they were broke down into further sub categories
    print(df0.groupby('Group').count())
    baTotal = df0.groupby('Group')['Ba'].sum().reset_index()
    zrTotal = df0.groupby('Group')['Zr'].sum().reset_index()
    srTotal = df0.groupby('Group')['Sr'].sum().reset_index()
    rbTotal = df0.groupby('Group')['Rb'].sum().reset_index()
    znTotal = df0.groupby('Group')['Zn'].sum().reset_index()
    niTotal = df0.groupby('Group')['Ni'].sum().reset_index()
    feTotal = df0.groupby('Group')['Fe'].sum().reset_index()
    mnTotal = df0.groupby('Group')['Mn'].sum().reset_index()
    tiTotal = df0.groupby('Group')['Ti'].sum().reset_index()
    caTotal = df0.groupby('Group')['Ca'].sum().reset_index()
    kTotal = df0.groupby('Group')['K'].sum().reset_index()

# put the element totals for utilitarian into a list
    baTotalUtl = baTotal[baTotal['Group'] == 'utilitarian']
    zrTotalUtl = zrTotal[zrTotal['Group'] == 'utilitarian']
    srTotalUtl = srTotal[srTotal['Group'] == 'utilitarian']
    rbTotalUtl = rbTotal[rbTotal['Group'] == 'utilitarian']
    znTotalUtl = znTotal[znTotal['Group'] == 'utilitarian']
    niTotalUtl = niTotal[niTotal['Group'] == 'utilitarian']
    feTotalUtl = feTotal[feTotal['Group'] == 'utilitarian']
    mnTotalUtl = mnTotal[mnTotal['Group'] == 'utilitarian']
    tiTotalUtl = tiTotal[tiTotal['Group'] == 'utilitarian']
    caTotalUtl = caTotal[caTotal['Group'] == 'utilitarian']
    kTotalUtl = kTotal[kTotal['Group'] == 'utilitarian']

    baTotalUtlList = baTotalUtl.values.tolist()
    zrTotalUtlList = zrTotalUtl.values.tolist()
    srTotalUtlList = srTotalUtl.values.tolist()
    rbTotalUtlList = rbTotalUtl.values.tolist()
    znTotalUtlList = znTotalUtl.values.tolist()
    niTotalUtlList = niTotalUtl.values.tolist()
    feTotalUtlList = feTotalUtl.values.tolist()
    mnTotalUtlList = mnTotalUtl.values.tolist()
    tiTotalUtlList = tiTotalUtl.values.tolist()
    caTotalUtlList = caTotalUtl.values.tolist()
    kTotalUtlList = kTotalUtl.values.tolist()

    allElementTotalsUtlList = []

    for e in baTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in zrTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in srTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in rbTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in znTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in niTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in feTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in mnTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in tiTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in caTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    for e in kTotalUtlList:
        allElementTotalsUtlList.append(e[1])

    # print(allElementTotalsUtlList)

# put the element totals for utilitarian into a list
    baTotalNonUtl = baTotal[baTotal['Group'] == 'non-utilitarian']
    zrTotalNonUtl = zrTotal[zrTotal['Group'] == 'non-utilitarian']
    srTotalNonUtl = srTotal[srTotal['Group'] == 'non-utilitarian']
    rbTotalNonUtl = rbTotal[rbTotal['Group'] == 'non-utilitarian']
    znTotalNonUtl = znTotal[znTotal['Group'] == 'non-utilitarian']
    niTotalNonUtl = niTotal[niTotal['Group'] == 'non-utilitarian']
    feTotalNonUtl = feTotal[feTotal['Group'] == 'non-utilitarian']
    mnTotalNonUtl = mnTotal[mnTotal['Group'] == 'non-utilitarian']
    tiTotalNonUtl = tiTotal[tiTotal['Group'] == 'non-utilitarian']
    caTotalNonUtl = caTotal[caTotal['Group'] == 'non-utilitarian']
    kTotalNonUtl = kTotal[kTotal['Group'] == 'non-utilitarian']

    baTotalNonUtlList = baTotalNonUtl.values.tolist()
    zrTotalNonUtlList = zrTotalNonUtl.values.tolist()
    srTotalNonUtlList = srTotalNonUtl.values.tolist()
    rbTotalNonUtlList = rbTotalNonUtl.values.tolist()
    znTotalNonUtlList = znTotalNonUtl.values.tolist()
    niTotalNonUtlList = niTotalNonUtl.values.tolist()
    feTotalNonUtlList = feTotalNonUtl.values.tolist()
    mnTotalNonUtlList = mnTotalNonUtl.values.tolist()
    tiTotalNonUtlList = tiTotalNonUtl.values.tolist()
    caTotalNonUtlList = caTotalNonUtl.values.tolist()
    kTotalNonUtlList = kTotalNonUtl.values.tolist()

    allElementTotalsNonUtlList = []

    for e in baTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in zrTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in srTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in rbTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in znTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in niTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in feTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in mnTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in tiTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in caTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    for e in kTotalNonUtlList:
        allElementTotalsNonUtlList.append(e[1])

    # print(allElementTotalsNonUtlList)

# get percentages to compare utilitarian and non utilitarian
    asarray(allElementTotalsUtlList)
    asarray(allElementTotalsNonUtlList)
    allElementTotalsList = add(allElementTotalsUtlList,allElementTotalsNonUtlList)

    # allElementTotalsUtlListPercentage = divide(allElementTotalsUtlList,allElementTotalsList)
    # allElementTotalsUtlListPercentage = multiply(allElementTotalsUtlListPercentage,100)

    # allElementTotalsNonUtlListPercentage = divide(allElementTotalsNonUtlList, allElementTotalsList)
    # allElementTotalsNonUtlListPercentage = multiply(allElementTotalsNonUtlListPercentage, 100)

    index = ['Ba', 'Zr', 'Sr', 'Rb', 'Zn', 'Ni', 'Fe', 'Mn', 'Ti', 'Ca', 'K']
    df2 = DataFrame({'non-utilitarian': allElementTotalsUtlList,
                       'utilitarian': allElementTotalsNonUtlList}, index=index)

    axes = df2.plot.bar(rot=0,subplots=True, title='Ceramic Sherd Elemental Composition',color=['green', 'blue'], edgecolor='red') # this is not very pretty

# move the labes
    axes[0].legend(loc=2)
    axes[1].legend(loc=2)

#removed the subplot titles since they were overlapping and not needed
    axes[0].set_title('')
    axes[1].set_title('')


# By having two graphs next to each other,
# it shows that even though the scale is different because
# one group has 135 data points and the other has 580, the data
# is still the same shape which suggests the material used to make
# both types of pottery was exactly the same.

    show()


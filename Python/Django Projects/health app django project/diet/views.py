from django.shortcuts import render
from django.http import HttpResponse
from .models import Food_items, Consumption
from datetime import date, timedelta
from pandas import *
import requests
import json
import plotly.express as px
from plotly.offline import plot

# this page may take a minute to load the more things are in the table for today..... (need to work that bug out still)
# contains inner functions because there is too much to read through for one big function. Takes the result of the inner functions and sends them in a nicer/ neater form to be rendered on webpage
def index(request):

    # query consumption table to get data for dates that = today
    # puts each col in a list
    def get_todays_info():
        today = date.today()
        todaysData = Consumption.objects.filter(date=today)

        currentDate = today.strftime("%Y-%m-%d")

        todaysTotalCals = 0  # gets the sum of the calories for all foods entered for the current date
        for entry in todaysData:
            todaysTotalCals = todaysTotalCals + entry.cals

        todaysFoods = []  # gets list of all the food items entred for current date
        for entry in todaysData:
            todaysFoods.append(entry.item)

        todaysFoodsCals = []  # gets list of calories that are associated to each item in todaysFoods list
        for entry in todaysData:
            todaysFoodsCals.append(entry.cals)

        return currentDate, todaysTotalCals, todaysFoods, todaysFoodsCals

    # calls te API "Spoontacular" to get other nutritional info on the food items eaten today based on the todaysFoods list
    # it then creates a data frame from the info in my database table and the info gathered from the api to display in a table
    def call_api():
        # makes a call to an api to get the nutrition facts for each food item entered for todays date
        url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
        querystring = {"query": food}
        headers = {
            'x-rapidapi-key': "0656d65008msh3c3913809c5f6b7p1b6e80jsn1ac0d096c06a",
            'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        pythoned_json = json.loads(response.text)
        listOfDicts = pythoned_json['items']

        if listOfDicts:
            dict = listOfDicts[0]
            print(dict)
            sugar = dict['sugar_g']
            fiber = dict['fiber_g']
            totalFat = dict['fat_total_g']
            totalCarbs = dict['carbohydrates_total_g']
            totalProtein = dict['protein_g']

            # these will be used for the df for visuals later...
            proteinList.append(totalProtein)
            carbList.append(totalCarbs)
            fatList.append(totalFat)

        # some of the items do not have results from the api so this is how the error is handled if it does not return any nutritional facts
        else:
            sugar = 'X'
            fiber = 'X'
            totalFat = 'X'
            totalCarbs = 'X'
            totalProtein = 'X'

        nutrFactsDict = {'item': todaysFoods[i], 'cals': todaysFoodsCals[i], 'sugar': sugar, 'fiber': fiber,
                         'fat': totalFat, 'carbs': totalCarbs, 'protein': totalProtein}
        return nutrFactsDict # returns one new dict each time it is called

    # creates a pie chart based on the info gotten from the api
    def create_pie_chart():
        proteinTotal = sum(proteinList)
        carbsTotal = sum(carbList)
        fatTotal = sum(fatList)

        values = [proteinTotal, carbsTotal, fatTotal]
        headers = ['Protein', 'Carbs', 'Fat']

        dict = {'headers': headers, 'values': values}
        df = DataFrame(data=dict)

        fig = px.pie(df, values='values', names='headers', title='')
        plot_div = plot(fig, output_type='div')
        return plot_div

    # gets all foods from the food item table sorted by their food group
    def get_food_groups():
        fruit = Food_items.objects.filter(group='fruit')
        veg = Food_items.objects.filter(group='veg')
        grain = Food_items.objects.filter(group='grain')
        dairy = Food_items.objects.filter(group='dairy')
        protein = Food_items.objects.filter(group='protein')
        junk = Food_items.objects.filter(group='junk food')
        misc = Food_items.objects.filter(group='misc.')
        return fruit, veg, grain, dairy, protein, junk, misc

    # if/ when the form is submitted, the data is used to create a new entry in the consumption table
    def store_form_data_to_db():
        inputSelection = request.POST
        inputDict = inputSelection.dict()
        inputValuesList = list(inputDict.values())

        selectedDate = inputValuesList[-1]
        selectedItem = inputValuesList[-2]

        # query the food item table to find the cal number for the item that was selected
        calsForSelectedItem = Food_items.objects.filter(item=selectedItem)
        calsToAdd = calsForSelectedItem[0].cals

        # add the new entry taken from the values in the form to add to the consumption table
        consumptionEntry = Consumption(item=selectedItem, cals=calsToAdd, date=selectedDate)
        consumptionEntry.save()

    # create line graph to show the history trends of consumption by daily total calories
    def plot_line_graph():
        rows = Consumption.objects.all()

        dateList = []
        calsList = []
        for row in rows:
            dateList.append(row.date)
            calsList.append(row.cals)

        dict = {'date': dateList, 'cals': calsList}
        df = DataFrame(data=dict)

        dailyTotals = df.groupby('date')['cals'].sum() #gets the total amount of calories eaten for each date there is an entry for

        dateColValues = dailyTotals.index # list of dates
        calColValues = dailyTotals.tolist() # list of daily total cals

        dict = {'date': dateColValues, 'totalCals': calColValues}
        df = DataFrame(data=dict)

        fig2 = px.line(df, x="date", y="totalCals")
        fig2.update_yaxes(title_text='Daily Cal Total')
        fig2.update_xaxes(title_text='Date')
        fig2.update_layout(font_size= 16)
        fig2.update_layout(paper_bgcolor="#daf0ce")
        fig2.update_layout(plot_bgcolor= "#ceebd9")
        fig2.update_yaxes(showgrid=False)
        plot_div2 = plot(fig2, output_type='div')
        return plot_div2

#------- main of outer function/view---------

    # this is all basically just making calls to the inner functions and assigning the return to a var
    template = "diet/index.html"

    currentDate, todaysTotalCals, todaysFoods, todaysFoodsCals = get_todays_info()

    # multiple calls to the the api to create a list made of dictionaries to display in table
    todaysFoodsNutrFacts = [] # this list were declared here so they could be global-ish to the inner functions
    proteinList = []
    carbList = []
    fatList = []
    i = 0
    for food in todaysFoods:
        nutrFactsDict = call_api()
        todaysFoodsNutrFacts.append(nutrFactsDict)
        i = i + 1

    plot_div = create_pie_chart()

    fruit, veg, grain, dairy, protein, junk, misc = get_food_groups()

    # if there was data from the form submitted, it will be transformed, processed, and stored to the consumption table
    if request.method == "POST":
        store_form_data_to_db()

    plot_div2 = plot_line_graph()

    return render(request,template,{'fruit' : fruit, 'veg': veg, 'grain' : grain, 'dairy' : dairy, 'protein' : protein, 'junk' : junk, 'misc' : misc, 'todaysTotalCals' : todaysTotalCals, 'todaysFoodsNutrFacts' : todaysFoodsNutrFacts, 'plot_div' : plot_div, 'plot_div2' : plot_div2,'currentDate' : currentDate})

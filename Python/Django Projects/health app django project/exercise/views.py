from django.shortcuts import render
from django.http import HttpResponse
from .models import Actions, Plan
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
import pandas as pd
import json

# contains inner functions because there is too much to read through for one big function. Takes the result of the inner functions and sends them in a nicer/ neater form to be rendered on webpage
def index(request):

    # when/ if the form is submitted, this function transforms the
    # Django query dictionary into a normal python dictionary.
    # it takes the values from the dictionary which are the name of the
    # plan and an array from the javascript array of objects from the hidden form.
    # The array of objects (which is just read into python as a string) is then separated into lists for the
    # values of ‘action’, ‘reps’, and ‘time’. Those lists and the name of
    # the plan are used to build a data frame which is then used to create a new entry
    # for the plans table in database based on every row in the data frame.
    def save_form_data_to_db():
        inputSelection = request.POST
        inputDict = inputSelection.dict()

        planName = inputDict['titleInForm']
        tokens = word_tokenize(inputDict['objArray'])
        arrayOfTokens = np.array(tokens)

        actionList = []
        repsList = []
        timeList = []

        i = 0
        while i < arrayOfTokens.size:
            actionList.append(arrayOfTokens[i])
            i = i + 3

        i = 1
        while i < arrayOfTokens.size:
            repsList.append(arrayOfTokens[i])
            i = i + 3

        i = 2
        while i < arrayOfTokens.size:
            timeList.append(arrayOfTokens[i])
            i = i + 3

        dict2 = {'action': actionList, 'reps': repsList, 'time': timeList}
        df = pd.DataFrame(data=dict2)

        for i in df.index:
            entry = Plan(name=planName, action=df['action'][i], reps=df['reps'][i], time=df['time'][i], order=0)
            entry.save()
        return entry #just for testing


    # creates a data frame out of all of the rows in the plans table. Used mainly to get a unique value of the plan names to display in the plan selection dropdown
    def get_all_plan_names():
        plans = Plan.objects.all()

        nameList = []
        actionList = []
        repsList = []
        timeList = []
        orderList = []
        for plan in plans:
            nameList.append(plan.name)
            actionList.append(plan.action)
            repsList.append(plan.reps)
            timeList.append(plan.time)
            orderList.append(plan.order)

        allPlansDict = {'name': nameList, 'action': actionList, 'reps': repsList, 'time': timeList, 'order': orderList}
        df = pd.DataFrame(data=allPlansDict)

        listOfPlans = df.name.unique()
        return listOfPlans

# ------- main of outer function/view---------
    template = "exercise/index.html"
    actions = Actions.objects.all()

# if the form has been submitted, calls to process it, this is needed or it will error on load if there is nothing in the form
    if request.method == "POST":
        save_form_data_to_db()

    listOfPlans = get_all_plan_names()

    return render(request,template, {'actions' : actions, 'listOfPlans' : listOfPlans})


# this will render the webpage to display the selected plan
def displayPlan(request):
    template = "exercise/displayPlan.html"

    planName = request.GET.get('plans_drop_down') # get from JavaScript param in URL. I know there is better ways to do this, but this was challenging enough to figure out with my limited JavaScript skills.

    onThisPlan = Plan.objects.filter(name=planName)

    return render(request, template, {'planName' : planName, 'onThisPlan' : onThisPlan})
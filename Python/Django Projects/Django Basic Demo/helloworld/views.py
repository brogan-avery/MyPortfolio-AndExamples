from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
import sqlite3
from sqlite3 import Error
# from .models import Test

# def index(request):
#     testData = Test.objects.all()
#     context = {'testData':testData}
#     return render(request, 'website/index.html', context)

def index(request):
    return HttpResponse('Hello,World!, from Brogan Avery on 11/1/2020')
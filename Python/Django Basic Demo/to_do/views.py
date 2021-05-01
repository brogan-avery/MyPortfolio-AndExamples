
from django.shortcuts import render
from django.http import HttpResponse
from .models import to_do_item

# Create your views here.
def index(request):
    to_do_list = to_do_item.objects.all()
    return render(request,'to_do/index.html', {"to_do_list": to_do_list})


from django.shortcuts import render
from django.http import HttpResponse
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
from pandas import *
from numpy import *
from .models import Element_levels
from .models import Temps
from .models import Scores

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.transform import dodge, factor_cmap


def index(request):
    template = "graph/index.html"

    rows = Scores.objects.all()

    regionsList = []
    scoresList = []

    for row in rows:
        regionsList.append(row.region)
        scoresList.append(row.score)

    # dict = {'region': regionsList, 'score': scoresList}
    # df = DataFrame(data=dict)

    plot = figure(x_range=regionsList,title='Happiest countries ranked', plot_width=2800,)
    plot.vbar(x=regionsList, top=scoresList,alpha=0.6, color='green')

    plot.xaxis.axis_label = "Country/Region"
    plot.yaxis.axis_label = "Scale 1(least happy) - 10(most happy)"

    plot.xaxis.major_label_orientation = "vertical"
    plot.xaxis.major_label_orientation = 1.2

    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0







    script, div = components(plot)

    return render(request, template, {"the_script": script, "the_div": div})

#FOR PLOTLY ONLY:
# def index(request):
#     template = "graph/index.html"
#     return render(request, template)

def pieChart(request):
    template = "graph/pieChart.html"

    rows = Element_levels.objects.all()

    baTotal = 0
    zrTotal = 0
    srTotal = 0
    rbTotal = 0
    znTotal = 0
    niTotal = 0
    feTotal = 0
    mnTotal = 0
    tiTotal = 0
    caTotal = 0
    kTotal = 0

    for row in rows:
        baTotal = baTotal + row.Ba
        zrTotal = zrTotal + row.Zr
        srTotal = srTotal + row.Sr
        rbTotal = rbTotal + row.Rb
        znTotal = znTotal + row.Zn
        niTotal = niTotal + row.Ni
        feTotal = feTotal + row.Fe
        mnTotal = mnTotal + row.Mn
        tiTotal = tiTotal + row.Ti
        caTotal = caTotal + row.Ca
        kTotal = kTotal + row.K

    dict = {'element': ['Ba', 'Zr', 'Sr', 'Rb', 'Zn', 'Ni', 'Fe', 'Mn', 'Ti', 'Ca', 'K'],'elementTotal': [baTotal, zrTotal, srTotal, rbTotal, znTotal, niTotal, feTotal, mnTotal, tiTotal,caTotal, kTotal]}
    df = DataFrame(data=dict)

    fig = px.pie(df, values='elementTotal', names='element', title='Element Levels')
    plot_div = plot(fig, output_type='div')

    return render(request, template, context={'plot_div': plot_div})

def lineChart(request):
    template = "graph/lineChart.html"


    rows = Temps.objects.all()

    datesList = []
    tempsList = []

    for row in rows:
        datesList.append(row.date)
        tempsList.append(row.temp)

    dict = {'date': datesList, 'temp': tempsList }
    df = DataFrame(data=dict)

    fig = px.line(df, x="date", y="temp", title='Average Global Land Temp')
    plot_div = plot(fig, output_type='div')

    return render(request,template,context={'plot_div': plot_div} )



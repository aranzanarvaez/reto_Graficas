import json
import sqlite3
from django.http import JsonResponse, QueryDict, StreamingHttpResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib import messages
from login.models import User, TopUserScores ,CountryScores, DataGame

from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.views.decorators.http import require_http_methods





@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def dashboard(request): 
    dataBase = sqlite3.connect("db.sqlite3")
    curr=dataBase.cursor()
    query = ''' SELECT level, score FROM login_datagame '''
    rows = curr.execute(query)
    datos = [['Nivel','Score']]
    for x in rows:
         datos.append([x[0],x[1]])

    datosPaises = [['Pais','Score']]
    query2 = ''' SELECT country, score FROM login_countryscores '''
    rows2 = curr.execute(query2)
    for x in rows2:
         datosPaises.append([x[0],x[1]])

    datosVidas= [['Nivel','Vidas']]
    query3 = ''' SELECT level, lives FROM login_datagame '''
    rows3 = curr.execute(query3)
    for x in rows3:
         datosVidas.append([x[0],x[1]])

    

    return render(request, 'dash.html', {"datos": datos , "datosP":datosPaises, "vidas":datosVidas})
    


# coding: utf8
from app import app
from flask import render_template, request, abort, redirect, url_for
import datetime
import pandas as pd
# from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from app import models


# engine = create_engine('mysql+pymysql://rafik:simplon@localhost/startups50')

# C'est ici qu'on demande à notre appli flask d'acheminer toutes les demandes d'URL à la racine vers la fonction index()
# A chaque fois qu'on ouvrira un navigateur pour accéder à l'indexe, c'est cette fonction qui sera appelé
# @app.route est un décorateur de la varibale app qui va encapsuler la fonction index() et acheminer les demande vers cette fonction

@app.route('/')
def index():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'index.html', date=date)

@app.route('/dashboard')
def dashboard():
    models.graphique()
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'dashboard.html', date=date)


@app.route('/formulaire_predict')
def formulaire_predict():    
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'formulaire_predict.html', date=date)

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    longitude = request.form['longitude']
    latitude = request.form['latitude']
    hma = request.form['hma']
    rooms = request.form['rooms']
    bedrooms = request.form['bedrooms']
    population = request.form['population']
    households = request.form['households']
    income = request.form['income']
    ocean_prox = request.form['ocean_prox']
    predict = models.predict(longitude, latitude, hma, rooms, bedrooms, population, households, income, ocean_prox)
    #mongoID = models.persist(rd, marketing)
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'predict.html', date=date, longitude=longitude, latitude=latitude, hma=hma, rooms=rooms, bedrooms=bedrooms, population=population, households=households,  income=income,  ocean_prox=ocean_prox, predict=predict)
    

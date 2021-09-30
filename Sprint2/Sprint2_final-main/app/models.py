# coding: utf8
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load
import matplotlib.pyplot as plt
import ssl
import pyautogui

client = MongoClient("mongodb+srv://marie:Tablesimplon06@cluster0.h2acd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client.mais
donnees = db.Housing2.find()
donnees = list(donnees)
df = pd.DataFrame(donnees)
width, height= pyautogui.size()
width = width/100
height = height/120



def graphique():

    #data = pd.read_sql_query('select * from startups50', engine)
    #data = pd.DataFrame(list(db.test2_graphique.find({'Year' : '1984', 'Country' : 'Burkina Faso'})))    
    #plt.figure()
    #plt.subplot(111)
    #plt.bar(data['Beverage Types'], data['Display Value'])
    #data.plot(kind="scatter", x="longitude", y="latitude", s=data["population"]/100, alpha=0.3, label="population", figsize=(30,20), c="median_house_value",cmap=plt.get_cmap("jet"), colorbar=True)
    #Et ici on va afficher des informations en plus : la taille d'un point = population, la couleur = revenus


    df.plot(kind="scatter", x="longitude", y="latitude", s=df["population"]/100, alpha=0.3, label="population", figsize=(width-2,height), c="median_house_value",cmap=plt.get_cmap("jet"), colorbar=True)
    plt.savefig("app/static/img/dashboard.png")
    df.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.3, figsize=(width-2,height), c="ocean_proximity",cmap=plt.get_cmap("jet"), colorbar=True)
    plt.savefig("app/static/img/dashboard2.png")
    
    return None

def predict(longitude, latitude, hma, rooms, bedrooms, population, households, income, ocean_prox):    
    model = load('app/filename.joblib')
    rooms_house=int(rooms)/int(households)
    bedrooms_rooms=int(bedrooms)/int(rooms)
    bedrooms_house=int(bedrooms)/int(households)
    pop_house=int(population)/int(households)
    house_value = model.predict([[longitude, latitude, hma, rooms, bedrooms, population, households, income, ocean_prox, rooms_house, bedrooms_rooms, bedrooms_house, pop_house]])[0]
    return house_value
	

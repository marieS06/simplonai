from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://avril:avril@localhost/sakila")


#Créer une fonction new_customer()qui va permettre
#l’insertion d’un nouveau client dans la table customer
#en demandant à un utilisateur de saisir les données,
#ainsi que son adresse pour remplir les tables address,
#city et country.Faire attention au contrainte d’intégrité

# def country():

#     country1 = input('country')
#     print(country1)
#     engine.execute('insert into country (country) values("%s");'%(country1))

# country()

# a= pd.read_sql_query("select * from country where country='nord' ", engine)
# print(a)

# def city():
#     city1= input('city')
#     country=input('country') #country_id de country1
#     engine.execute('insert into city(city,country_id) values("%s","%s");'%(city1,country))

# city()
# b=pd.read_sql_query("select * from city where city='nord' ", engine)
# print(b)

# def address():
#      addr=input('address')
#      district=input('district')
#      citys=input('cityid') # recupe
#      phone=input('phone')
#      location=input('geometrie')
#                         #ST_GeomFromText('POINT(1 -1)')
#      engine.execute('insert into address(address,district,city_id,phone,location) values("%s","%s","%s","%s",%s);'%(addr,district,citys,phone,location))
# address()


# c= pd.read_sql_query("select * from address where city_id=605 ", engine)
# print(c)

# def store():

#     stor=input('store_id')
#     first_nam=input('first_name')
#     last_nam=input('last_name')
#     emai=input('email')
#     addreid=input('address_id')

#     engine.execute('insert into customer(store_id ,first_name,last_name,email,address_id) values (%s,"%s","%s","%s","%s");'%(stor,first_nam,last_nam,emai,addreid))
# store()
#%%
# d=pd.read_sql_query("select * from customer where address_id=608", engine)
# print(d)


# Ecrire une fonction qui va afficher l’historique de location d’un client
#%%
def histoire():    
    mm = pd.read_sql_query('select c.first_name,c.last_name,r.rental_date,r.return_date,f.title from customer c join rental r on r.customer_id=c.customer_id join inventory i on i.inventory_id=r.inventory_id join film f on f.film_id=i.film_id where first_name="MARY" and last_name="SMITH"', engine)
    print(mm)
    
histoire()

#%%
# 4.D’après vous quels seraient les indicateurs graphiques les plus pertinents pour suivre l’évolution du business 
# de location de vidéos.? Avec Matplotlib et Seaborn rédiger trois fonctions qui vont vous permettre d’afficher
#  les trois graphiques permettant de suivre au mieux la rentabilité de l’affaire

import numpy as np
from numpy import arange
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


c= pd.read_sql_query("select amount from payment", engine)
d= pd.read_sql_query("select payment_date from payment ", engine)

TEST= pd.read_sql_query("select payment_date, amount from payment ", engine)
TEST['payment_date'] = pd.to_datetime(TEST['payment_date'])
TEST.dropna()
TEST = TEST.set_index('payment_date')

min_mois = TEST.resample('M').min()
max_mois = TEST.resample('M').max()
moy_mois = TEST.resample('M').mean()

plt.close()
plt.subplot(211)
plt.title('Amount per payment date (month)')
plt.plot(max_mois,'r',label='max')
plt.plot(moy_mois,'k',label='moyenne')
plt.plot(min_mois,'b',label='min')
plt.legend(loc=1)


plt.xticks(rotation=90)


plt.subplot(212)
rental_date= pd.read_sql_query("select rental_date,1 from rental", engine)
rental_date['rental_date'] = pd.to_datetime(rental_date['rental_date'])
rental_date = rental_date.set_index('rental_date')
sum_mois = rental_date.resample('M').sum()

plt.title('Amount of renting per month')
plt.plot(sum_mois,'r',label='max')
plt.xticks(rotation=90)

#%%
# plt.plot(c,d,'or')
plt.plot(d,c,'.r')
plt.title("Evolution du taux de location")
plt.ylabel("montant")
plt.xlabel("date")

plt.xticks(rotation=90)
plt.show()
#%%

plt.subplot(131)
plt.plot(c,'or')
plt.subplot(132)
plt.plot(d,'or')
plt.subplot(133)
plt.plot(rental_date,'or')
# ------------------------------------------------------------

# fig, ax = plt.subplots()
# ax.scatter(c, d)
# ax.set_xlabel( 'payment' )
# ax.set_ylabel( 'date')
# plt.show()

# -------------------------------------------------------------











# import matplotlib.pyplot as plt

# bled = pd.read_sql_query("select category_id from film_category", engine)
# # VARIABLE QUALITATIVE
# # Diagramme en secteurs
# bled.value_counts(normalize=True).plot(kind='pie')
# # Cette ligne assure que le pie chart est un cercle plutôt qu'une éllipse
# plt.axis('equal') 
# plt.show() # Affiche le graphique

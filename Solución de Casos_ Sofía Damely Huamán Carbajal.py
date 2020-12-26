
"""
Programa de Pasantía Datahack 2021
Postulante: Sofía Damely Huamán Carbajal

"""
# Caso 1: Elaborar un programa que determine la suma de dígitos de un número de hasta cinco dígitos

print("Inserte un número de hasta cinco dígitos:")
Numero=int(input())

suma=0
for i in Numero:
    suma+=int(i)
    
print(f"La suma de los dígitos del número es {suma}")

# Caso 2: Dado dos vectores , indicar si el elemento de menor valor es econtrado en el otro vector

Vector1=[]
Vector2=[]

elemento_del_vector_uno=int(input("Inserte el tamaño del primer vector:"))
elemento_del_vector_dos=int(input("Inserte el tamaño del segundo vector:"))


for i in range(0,elemento_del_vector_uno):
    ele=input()
    Vector1.append(ele)

print(Vector1)
    
for i in range(0,elemento_del_vector_dos):
    ele=input()
    Vector2.append(ele) 

print(Vector2)


if min(Vector1) in Vector2:
    print(True)
else:
    print(False)

#Caso 3: Encontrar valores repetidos en una lista
    
import random
import collections

vector=[]

for i in range(0,100):
    elemento=random.randint(0,1000)
    vector.append(elemento)

duplicados=tuple(x for x,y in collections.Counter(vector).items() if y>1)

print(duplicados)

#Caso 4: Extraer los títulos de los comics de la pagina y guardarlos en un archivo csv

from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome() 
urla= "https://xkcd.com/"
nombres=[]

for i in range(1,2403):
    url = urla +str(i)+"/"
    driver.get(url)
    get_title=driver.title
    nombres.append(get_title)

df=pd.DataFrame(nombres,columns=['Títulos de comics'])    
df.to_csv(r'C:\Users\Usuario\Downloads\comic.csv', index = False)

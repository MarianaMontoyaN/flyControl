import sqlite3
from package import Package
import random

'''
Function that creates the database and tables if they don't exist

Outputs:
    * exists: boolean value that indicates if the tables exist or not
'''
def create_db():
    conexion = sqlite3.connect("vuelos.db")
    cursor = conexion.cursor()
    exists = False

    try:
        cursor.execute("CREATE TABLE VUELO1(id INTEGER PRIMARY KEY AUTOINCREMENT, peso INT NOT NULL, precio_pesos FLOAT NOT NULL, precio_dolar FLOAT NOT NULL)")
        cursor.execute("CREATE TABLE VUELO2(id INTEGER PRIMARY KEY AUTOINCREMENT, peso INT NOT NULL, precio_pesos FLOAT NOT NULL, precio_dolar FLOAT NOT NULL)")
        cursor.execute("CREATE TABLE VUELO3(id INTEGER PRIMARY KEY AUTOINCREMENT, peso INT NOT NULL, precio_pesos FLOAT NOT NULL, precio_dolar FLOAT NOT NULL)")
    except sqlite3.OperationalError:
        print("La tablas ya existen.")
        exists = True
    else:
        print("La tablas se han creado correctamente.")

    conexion.close()

    return exists

'''
Function that adds packages to the database
'''
def add_package_db(flight, weight, price_pesos, price_dollars):

    conexion = sqlite3.connect("vuelos.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO {} VALUES (null, {}, {}, {})".format(
            flight, weight, price_pesos, price_dollars) )
    except sqlite3.IntegrityError:
        print("El paquete ya existe.")

    conexion.commit()
    conexion.close()

'''
Function that captures all the data of a flight

Outputs:
    * list_packages: array with lists with int values
'''
def show_packages(flight):

    conexion = sqlite3.connect("vuelos.db")
    cursor = conexion.cursor()  

    list_packages = cursor.execute("SELECT * FROM {}".format(flight)).fetchall() 

    conexion.close()

    return list_packages


'''
Function that adds 30 random packets to each flight
'''
def default_data(price_dollar):

    for vuelo in range(3):
        loads = [random.randint(400,500) for weight in range(30)]
        for load in loads:
            object_package = Package(load, price_dollar)
            pesos = object_package.price_pesos
            dollar = object_package.price_dollar
            add_package_db('vuelo'+str(vuelo+1), load, pesos, dollar)


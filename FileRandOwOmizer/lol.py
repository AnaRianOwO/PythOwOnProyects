import os
import subprocess
import random

with open('C:/Users/User/Documents/プログラミング/PythOwOnProyects/dist/archivo.txt', 'r', encoding='utf-8') as archivo:
    carpeta = archivo.read()

def randomizer():
    archivos = os.listdir(carpeta)
    archivo = random.choice(archivos)
    archivo = carpeta + "\\" + archivo
    if os.path.isdir(archivo) == True:
        carpet = archivo
        archivos = os.listdir(carpet)
        archivo = random.choice(archivos)
        archivo = carpet + "\\" + archivo
        if os.path.isdir(archivo) == True:
            subprocess.run("explorer " + archivo, shell=True)
    subprocess.run(archivo, shell=True)

def menu():
    randomizer()
    opcion = input("Presiona enter para seleccionar otro archivo random, oprime 0 para salir\n")
    if opcion == "0":
        exit()

while True:
    menu()
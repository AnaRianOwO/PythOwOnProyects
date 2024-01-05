import os
import random
from tkinter import filedialog
import subprocess

carpeta = filedialog.askdirectory(title="Selecciona la carpeta a seleccionar un archivo random")
archivos = os.listdir(carpeta)

def randomizer(archivos):
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
 
while True:
    randomizer(archivos)
    input = input("Presiona enter para seleccionar otro archivo random, oprime 0 para salir\n")
    if input == "0":
        exit()
    else:
        continue
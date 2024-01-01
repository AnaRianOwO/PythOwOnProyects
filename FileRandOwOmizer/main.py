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
        print(archivo)
        archivo = carpet + "\\" + archivo
    subprocess.run(archivo, shell=True)

while True:
    randomizer(archivos)
    input("Presiona enter para seleccionar otro archivo random, oprime 1 para escoger otra carpeta, oprime 0 para salir\n")
    if input == "1":
        carpeta = filedialog.askdirectory(title="Selecciona la carpeta a seleccionar un archivo random")
        archivos = os.listdir(carpeta)
        randomizer(archivos)
    if input == "0":
        exit()
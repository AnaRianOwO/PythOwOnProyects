import os
import random
from tkinter import filedialog
import subprocess

carpeta = filedialog.askdirectory(title="Selecciona la carpeta a seleccionar un archivo random")
archivos = os.listdir(carpeta)

def randomizer(archivos):
    archivo = random.choice(archivos)
    archivo = carpeta + "\\" + archivo
    print(archivo)
    subprocess.run(archivo, shell=True)

while True:
    randomizer(archivos)
    input("Presiona enter para seleccionar otro archivo random")
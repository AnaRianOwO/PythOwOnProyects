import os
import random
from tkinter import filedialog

carpetaMAIN = filedialog.askdirectory(initialdir = "/",title = "Selecciona carpeta para traer un archivo al azar")
archivos = os.listdir(carpetaMAIN)
  
def randomizer():
    randomizador = random.randint(0, len(archivos)-1)
    return archivos[randomizador]

def main(carpeta):
    archivo = randomizer(carpeta)
    if esCarpeta(randomizer):
        main(randomizer)
    print('El archivo al azar es: ' + archivo + '.')

def menu():
    print('Ahora traeremos un archivo al azar de la carpeta seleccionada')
    main(carpetaMAIN)
    opcion = input('¿Quieres traer otro archivo al azar? Presiona enter para continuar. Si no, oprime 0')
    if opcion == '0':
        print('Gracias por usar el Randomizer')
        exit()
                
while True:
    menu()
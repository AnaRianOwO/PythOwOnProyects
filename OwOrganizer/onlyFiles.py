import os
from tkinter import filedialog

def tipoArchivo (archivo):
    namae, extension = os.path.splitext(archivo)
    if extension == "" and namae != "Carpetas":
        return "Carpetas"
    else:
        extension = extension[1:]
        extension = extension.upper()
        return extension

def moverArchivo (archivo, carpeta, oldFolder):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    if os.path.exists(carpeta + "/" + archivo):
        archivo = archivo + "(1)"
    rutaCompletaFile = oldFolder + "/" + archivo
    #print(rutaCompletaFile)
    os.rename(rutaCompletaFile, carpeta + "/" + archivo)

def organizarCarpeta():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta")
    for archivo in os.listdir(carpeta):
        extension = tipoArchivo(archivo)
        folder = carpeta + "/" + extension
        moverArchivo(archivo, folder, carpeta)
    print("Archivos organizados")
    
organizarCarpeta()
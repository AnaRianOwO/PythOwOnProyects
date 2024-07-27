import tkinter as tk
from tkinter import ttk
import os
import webbrowser
from lxml import html
from tkinter import filedialog
from time import sleep

#Funciones

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

def extraerURL (archivo):
    tree = html.fromstring(archivo)
    enlaces = tree.xpath("//a/@href")
    return enlaces

def buscarURL (url):
    global indice_actual
    webbrowser.open(url)
    indice_actual += 1
    actualizarBotonAbrir()

# Opciones

def organizarCarpeta():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta")
    for archivo in os.listdir(carpeta):
        extension = tipoArchivo(archivo)
        folder = carpeta + "/" + extension
        moverArchivo(archivo, folder, carpeta)
    success.config(text="Archivos organizados")
    

def organizarMarcadores():
    global enlaces, indice_actual
    marcadores = filedialog.askopenfilename(title="Seleccionar archivo")
    with open(marcadores, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    enlaces = extraerURL(contenido)
    #print(enlaces)
    indice_actual = 0
    actualizarBotonAbrir()

def actualizarBotonAbrir():
    global indice_actual
    if indice_actual < len(enlaces):
        url_actual = enlaces[indice_actual]
        claro.config(text=f"Abrir: {url_actual}", command=lambda: buscarURL(url_actual))
        confirmacion.config(text=f"El enlace es {url_actual}. ¿Desea abrirlo?")
    else:
        confirmacion.config(text="No hay más enlaces.")


#Menú

root = tk.Tk()
root.title("OwOrganizer")
root.geometry("400x400")

estilo = ttk.Style()
estilo.configure("TButton", background="#dd7a9e", foreground="black", font=("Helvetica", 12), padding=10, relief="raised", width=25)

carpeta = ttk.Button(root, text="Organizar carpeta", command=organizarCarpeta, style="TButton")
marcadores = ttk.Button(root, text="Organizar marcadores", command=organizarMarcadores, style="TButton")
confirmacion = tk.Label(root, fg="red")
claro = ttk.Button(root, text="Abrir", style="TButton")
success = tk.Label(root, fg="green")

carpeta.pack(pady=10)
marcadores.pack(pady=50)
confirmacion.pack(pady=20)
claro.pack(padx=10, pady=10) 

success.pack()
root.mainloop()
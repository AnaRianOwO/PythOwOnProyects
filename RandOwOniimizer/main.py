from tkinter import filedialog
import json
import random

filedialog
archivoExport = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))

with open(archivoExport, 'r', encoding='utf-8') as f:
    jsonData = json.load(f)

PlanToRead = jsonData["Plan to Read"]
OnHold = jsonData["On-Hold"]
Completed = jsonData["Completed"]
Reading = jsonData["Reading"]

def randomizer():
    randomizador = random.randint(0, len(PlanToRead)-1)
    print('El manga al azar es: ' + PlanToRead[randomizador]['name'] + '')

def menu():
    print('Ahora traeremos un manga al azar de tu lista de Plan to Read')
    randomizer()
    opcion = input('¿Quieres traer otro manga al azar? Presiona enter para continuar. Si no, oprime 0')
    if opcion == '0':
        print('Gracias por usar el Randomizer')
        exit()
    
while True:
    menu()
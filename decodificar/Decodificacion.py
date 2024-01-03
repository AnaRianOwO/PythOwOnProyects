#codigo para the besto trio owo
def codificacion():
    codificacion=dict(zip(letra_normal,codigo))
    print("El mensaje codificado es: ")
    for key in (mensaje):
        print(codificacion[key],end="")

def decodificacion():
    decodificacion=dict(zip(codigo,letra_normal))
    print("El mensaje decodificado es: ")
    for key in (mensaje):
        print(decodificacion[key],end="")

letra_normal=("a", "b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A", "B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á", "É","Í","Ó","Ú","á","é","í","ó","ú"," ","_",".",",",":","-","?","!")
codigo=("=", "%","&","^",">","~","\\","[","™","£","¢","`","@","©","¬","¦","|","¥","«","»","„","×","ʼ","‹","‡","†","¶","#", "§",")","(","]","{","}","°","4","3","0","8","1","9","¿","2","5","7","6","$","+","±","\"","⁴","/",";",":","®", "÷","℅","≥","≤","¼","¾","½","?","!",".","ⁿ","¨","Ω","∑","√","∞","•")

i="yes"
while i=="yes" or i=="si":
    print("Hola mis amores uwu, ¿Qué vamos a hacer ahora?\n1.Pasar de letras normales a codigo (codificar)\n2.Pasar de codigo a letras normales(decodificar)")
    owo=int(input())
    
    if owo==1:
        print("Escribir mensaje para codificar uwu")
        mensaje=input()
        codificacion()
    elif owo==2:
        print("Escribir mensaje para decodificar uwu")
        mensaje=input()
        decodificacion()
    else:
        print("No mis amores uwu, revisen bien las opciones")

    print("\nSeguimos uwu?")
    i=input()


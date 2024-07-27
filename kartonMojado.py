#programolo

meta = 1000000
monto = 400
dias = 1
montos = []

while meta > 0:
    meta = meta - monto
    print("El monto del día "+str(dias)+" es: "+format(monto, ',d').replace(",", "."))
    dias += 1
    montos.append(monto)
    monto+=400
    
print(montos)
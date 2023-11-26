# mastodsmaticas
dias = int(input("Dias que llevas ahorrando: "))
montoDiario = 400
montoTotal = 0

for dia in range(dias):
    montoTotal += montoDiario
    montoDiario = montoDiario + 400

print("Monto total ahorrado:", montoTotal)
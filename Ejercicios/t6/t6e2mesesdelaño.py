
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero = int(input("Elige un número del 1 al 12: " ))

if numero >= 1 and numero <= 12:
    print("El mes es:", meses[numero - 1])

if (meses[numero - 1]) == "Junio":
    print("EL MEJOR MES")
else:
    print("Error")







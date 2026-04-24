
def introducecolor(color):
    if color == "Azul":
        mensaje = "Premio"
    else:
        mensaje = "Prueba otro color"
    return mensaje


for i in range(5):
    color = input("Introduce un color: ")
    mensaje = introducecolor(color)
    print(mensaje)

    if color == "Azul":
        break
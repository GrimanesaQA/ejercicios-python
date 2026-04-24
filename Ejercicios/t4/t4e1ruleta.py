
def fortunacolor(color):
    if (color == "Rojo"):
        mensaje = "Pasión y energía"
    elif (color == "Verde"):
        mensaje = "Esperanza y crecimiento"    
    elif (color == "Azul"):
        mensaje = "Calma y serenidad"
    elif (color == "Amarillo"):
        mensaje = "Felicidad y optimismo"
    elif (color == "Morado"):
        mensaje = "Sabiduría y creatividad"
    else:
        mensaje = "No hay fortuna"
    return mensaje

color = input("Elije un color: ")
mensaje = fortunacolor(color)
print(mensaje)
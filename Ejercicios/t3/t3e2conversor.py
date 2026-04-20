def convertirMoneda(cantidad_en_euros):
    dolares = cantidad_en_euros * 1.1
    libras = cantidad_en_euros * 0.87
    return dolares, libras


cantidad_euros = float(input("cantidad de euros"))

resultado = convertirMoneda(cantidad_euros)
print(resultado)
contador = 100
multiplicador = 1.25
while contador < 10000:
    contador *= multiplicador
    if contador >= 500:
        multiplicador = 1

    print(int(contador))
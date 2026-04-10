def contar(numero, limite):
    if numero > limite:
        return print("acabou.")
    print(numero)
    contar(numero + 1, limite)

contar(1, 5)


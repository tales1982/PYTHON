# Exercício 22 - Filtrando login ★★
# Mostre somente os eventos cujo type seja USER_LOGIN.

tipo_procurado = "USER_LOGIN"

with open("audit.log", "r") as arquivo:
    for linha in arquivo:
        tipo = linha.split()[0].split("=")[1]
        if tipo == tipo_procurado:
            print(linha.strip())

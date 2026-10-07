# Exercício 11 - Filtrando sucessos ★★
# Mostre somente as linhas que contêm Accepted password



target="Accepted password"

with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        if target in linha:
            print(linha.strip())
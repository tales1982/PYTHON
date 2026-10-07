# Exercício 10 - Filtrando falhas ★★
# Copie o log acima para auth.log. Mostre apenas as linhas que contêm Failed password.


target="Failed password"


with open("auth.log", "r") as f:
    for linha in f:
        if target in linha:
            print(linha.strip())
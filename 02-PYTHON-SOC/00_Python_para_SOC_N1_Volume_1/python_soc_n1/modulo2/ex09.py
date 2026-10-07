# Exercício 9 - Lendo o arquivo inteiro ★
# Agora use um for para mostrar todas as linhas de auth.log


with open("auth.log","r") as f:
    for i in f:
        print(i.strip())
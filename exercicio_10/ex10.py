import os

os.makedirs("saida", exist_ok=True)

linhas = []
for i in range(1, 6):
    texto = input(f"Digite o texto {i}: ")
    linhas.append(texto + "\n")

with open("saida/resultado.txt", "w") as f:
    f.writelines(linhas)

# Lê e imprime o conteúdo
with open("saida/resultado.txt", "r") as f:
    print(f.read())



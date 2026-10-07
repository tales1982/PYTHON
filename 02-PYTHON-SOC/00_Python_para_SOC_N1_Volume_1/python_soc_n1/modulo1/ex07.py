# Exercício 7 - Extraindo usuário e IP ★★
# A partir de Failed password for admin from 198.51.100.25, mostre a saída:
# Usuário: admin
# IP: 198.51.100.2

text="Failed password for admin from 198.51.100.25"

textSplit = text.split()


print(f"Usuario: {textSplit[3]}")
print(f"IP: {textSplit[5]}")
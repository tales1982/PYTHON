# Exercício 15 - Conte por IP ★★
# Crie um dicionário que conte quantas falhas vieram de cada IP.
# Oct 07 10:10:04 web01 sshd[1202]: Failed password for root from 203.0.113.50 port 51114 ssh2

contagen = {}
target = "Failed password"

count = 0
with open("auth.log", "r") as file:
    for l in file:
        if target in l:
            partes = l.split("from")[1].split()[0]
            contagen[partes] = contagen.get(partes, 0) + 1

print(contagen)

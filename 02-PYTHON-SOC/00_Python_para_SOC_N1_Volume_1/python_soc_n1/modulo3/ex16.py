# Exercício 16 - Mostre o campeão ★★★
# Mostre qual IP realizou mais tentativas malsucedidas. Não se preocupe ainda em fazer a
# solução mais elegante; faça funcionar.
# Oct 07 10:10:04 web01 sshd[1202]: Failed password for root from 203.0.113.50 port 51114 ssh2

contagen = {}
target = "Failed password"

with open("auth.log", "r") as file:
    for l in file:
        if target in l:
            partes = l.split("from")[1].split()[0]
            contagen[partes] = contagen.get(partes, 0) + 1

campeao = max(contagen, key=contagen.get)
print(f"Campeão: {campeao} com {contagen[campeao]} tentativas")

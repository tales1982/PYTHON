# Exercício 17 - Regra de alerta ★★★
# Mostre somente IPs que tenham 3 ou mais tentativas malsucedidas.
# === LOGS ===
# Oct 07 11:00:11 srv01 sshd: Failed password for root from 45.33.32.10 port 41004
# Oct 07 11:00:20 srv01 sshd: Accepted password for root from 45.33.32.10 port 41010

contagen = {}
target = "Failed password"
limite = 3

with open("auth.log", "r") as file:
    for l in file:
        if target in l:
            partes = l.split("from")[1].split()[0]
            contagen[partes] = contagen.get(partes, 0) + 1

for ip, total in contagen.items():
    if total >= limite:
        print(f"ALERTA: {ip} com {total} tentativas")

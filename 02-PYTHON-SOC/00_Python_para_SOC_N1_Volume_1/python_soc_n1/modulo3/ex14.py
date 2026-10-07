# Exercício 14 - Extraia todos os IPs ★★
# No auth.log anterior, para cada linha com Failed password, extraia e imprima somente o IP.
# logs = Oct 07 10:10:04 web01 sshd[1202]: Failed password for root from 203.0.113.50 port 51114 ssh2

target = "Failed password"

with open("auth.log", "r") as file:
    for linha in file:
        if target in linha:
            ip = linha.split("from")[1].split()[0]
            print(ip)

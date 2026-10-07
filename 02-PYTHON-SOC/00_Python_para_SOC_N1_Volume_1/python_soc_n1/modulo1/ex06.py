# Exercício 6 - Extraindo o IP ★★
# Usando a mesma linha, descubra em qual posição está 203.0.113.50 e mostre somente o IP.



ips = ["192.168.124.47","192.168.77.106","192.168.98.56","192.124.14.112","192.168.44.76","203.0.113.50","185.220.101.4"]
count = 0
target = "203.0.113.50"

for ip in ips:
    count+=1
    if ip == target:
        print(f"IP: {target}.")
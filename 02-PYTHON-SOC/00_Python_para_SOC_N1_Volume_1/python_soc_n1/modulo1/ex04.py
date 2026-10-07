# Exercício 4 - Procurando um IP ★
# Na mesma lista, mostre IP suspeito encontrado somente quando o IP for igual a
# 185.220.101.4.

ips = ["192.168.124.47","192.168.77.106","192.168.98.56","192.124.14.112","192.168.44.76","185.220.101.4"]
suspicious_ip = "185.220.101.4"

for ip  in ips:
    if ip == suspicious_ip:
        print(f"Foi encontrado um ip suspeito {suspicious_ip}.")
    
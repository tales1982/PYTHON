# Exercício 3 - Lista de IOCs ★
# Crie uma lista com cinco endereços IP. Use for para imprimir um IP por linha

ips = ["192.168.124.47","192.168.77.106","192.168.98.56","192.124.14.112","192.168.44.76",]
count = 0
for ip in ips:
    count=count+1
    print(f"IP{count}: {ip}")
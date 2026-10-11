# Exercício 18 - Brute force seguido de sucesso ★★★
# Descubra programaticamente se algum IP que gerou Failed password também aparece
# posteriormente em uma linha Accepted password. Mostre o IP.

failed = "Failed password"
accept = "Accepted password"
ips_falha = []

with open("auth.log", "r") as file:
    for l in file:
        if failed in l:
            ip = l.split("from")[1].split()[0]
            if ip not in ips_falha:  # evita IPs repetidos
                ips_falha.append(ip)
        elif accept in l:
            ip = l.split("from")[1].split()[0]
            if ip in ips_falha:  # já falhou antes e agora entrou
                print(f"Brute force seguido de sucesso: {ip}")

# Exercício 33 - Alerta configurável
# Crie uma variável limite = 5. O programa deve alertar qualquer IP cuja contagem seja igual
# ou superior ao limite.

limite = 5
falhas_por_ip = {}
ips_alerta = {}

with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        if "Failed password" in linha and "from " in linha:
            ip = linha.split("from ")[1].split()[0]
            falhas_por_ip[ip] = falhas_por_ip.get(ip, 0) + 1

ordenado = sorted(falhas_por_ip.items(), key=lambda x: x[1], reverse=True)

for ip, quantidade in ordenado:
    if quantidade >= limite:
        ips_alerta[ip] = quantidade

print("=" * 45)
print("        ALERTA DE FORÇA BRUTA - finance-web")
print("=" * 45)
print(f"Limite configurado: {limite} falhas")
print("-" * 45)
if ips_alerta:
    for ip, quantidade in ips_alerta.items():
        print(f"[ALERTA] {ip:<16} {quantidade:>3} falhas")
else:
    print("Nenhum IP atingiu o limite")
print("=" * 45)
print(f"IPs analisados: {len(falhas_por_ip)} | IPs em alerta: {len(ips_alerta)}")

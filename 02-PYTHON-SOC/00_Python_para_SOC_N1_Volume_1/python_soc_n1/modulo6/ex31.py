# Exercício 31 - Top IPs
# Leia um arquivo de autenticação e mostre os três IPs com maior número de falhas.

# Exercício 31 - Top IPs

ips_auth = {}

with open("auth.log", "r") as file:
    for l in file:
        if "Failed password" not in l or "from " not in l:
            continue

        ip = l.split("from ")[1].split()[0]
        ips_auth[ip] = ips_auth.get(ip, 0) + 1

# Ordenar após terminar a leitura
top3 = sorted(ips_auth.items(), key=lambda x: x[1], reverse=True)[:3]

# Mostrar os resultados
print("=" * 40)
print("     TOP 3 IPs COM MAIS FALHAS")
print("=" * 40)
print(f"{'POS':<5} {'IP':<17} {'FALHAS':>6}")
print("-" * 40)
for posicao, (ip, quantidade) in enumerate(top3, 1):
    print(f"[{posicao}]   {ip:<17} {quantidade:>6}")
print("=" * 40)
print(f"Total de IPs com falhas: {len(ips_auth)}")

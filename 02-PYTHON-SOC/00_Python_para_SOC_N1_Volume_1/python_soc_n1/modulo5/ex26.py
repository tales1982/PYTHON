# Exercício 26 - Origem suspeita ★★
# Extraia os IPs das autenticações e identifique qual IP externo aparece repetidamente

REDE_INTERNA = "10.0.0."
ips = []

with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        if "from " not in linha:
            continue
        ip = linha.split("from ")[1].split()[0]
        ips.append(ip)

print("=" * 45)
print("        ORIGEM SUSPEITA - finance-web")
print("=" * 45)
for ip in set(ips):  # o set nao deixa repetir se ja apareeceu
    quantidade = ips.count(ip)
    if quantidade > 1 and not ip.startswith(REDE_INTERNA):
        print(f"IP externo suspeito: {ip} ({quantidade} ocorrências)")
print("=" * 45)

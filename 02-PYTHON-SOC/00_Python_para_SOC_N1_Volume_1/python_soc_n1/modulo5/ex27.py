# Exercício 27 - Correlação ★★★
# Verifique se o IP com várias falhas conseguiu autenticar com sucesso.

ACCEPT_PASS = "Accepted password"
FAILED_PASS = "Failed password"
ips_failed = []
em_comum = []

with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        if "from " not in linha:
            continue
        ip = linha.split("from ")[1].split()[0]

        if FAILED_PASS in linha:
            ips_failed.append(ip)
        elif ACCEPT_PASS in linha and ips_failed.count(ip) > 1:  # noqa: SIM102
            if ip not in em_comum:
                em_comum.append(ip)

print("=" * 54)
print("        CORRELAÇÃO - finance-web")
print("=" * 54)
if em_comum:
    for ip in em_comum:
        print(f"[!] {ip} falhou {ips_failed.count(ip)}x e depois conseguiu entrar")
else:
    print("Nenhum IP com várias falhas conseguiu entrar")
print("=" * 54)

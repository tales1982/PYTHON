# Exercício 19 - Pequeno relatório ★★★
# Gere uma saída contendo: total de falhas, IPs envolvidos, quantidade por IP e IPs que também
# tiveram autenticação aceita.

TEXTO_FALHA = "Failed password"
TEXTO_SUCESSO = "Accepted password"
falhas_por_ip = {}
sucessos_apos_falha = {}
total_falhas = 0


with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        if TEXTO_FALHA in linha:
            ip_falha = linha.split("from")[1].split()[0]
            falhas_por_ip[ip_falha] = falhas_por_ip.get(ip_falha, 0) + 1
            total_falhas += 1
        elif TEXTO_SUCESSO in linha:
            ip_sucesso = linha.split("from")[1].split()[0]
            if ip_sucesso in falhas_por_ip:
                sucessos_apos_falha[ip_sucesso] = sucessos_apos_falha.get(ip_sucesso, 0) + 1

print("=" * 40)
print("      RELATÓRIO DE AUTENTICAÇÃO SSH")
print("=" * 40)
print(f"Total de falhas: {total_falhas}")
print(f"IPs envolvidos:  {len(falhas_por_ip)}")

print("\nFalhas por IP:")
for ip, quantidade in falhas_por_ip.items():
    print(f"  {ip:<16} {quantidade:>3} falha(s)")

print("\n[!] IPs com falha e depois login aceito:")
if sucessos_apos_falha:
    for ip, quantidade in sucessos_apos_falha.items():
        print(f"  {ip:<16} {quantidade:>3} login(s) aceito(s)")
else:
    print("  Nenhum")
print("=" * 40)

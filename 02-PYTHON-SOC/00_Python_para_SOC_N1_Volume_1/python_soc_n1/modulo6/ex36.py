# Exercício 36 - Função de análise
# Crie uma função que receba o nome de um arquivo de log e devolva um dicionário com a
# contagem de falhas por IP


def analizar_ips(arq):
    ips_failed = {}

    with open(arq, "r") as file:
        for l in file:
            if "[FALHA]" in l:
                ip = l.split("[FALHA]   ")[1].strip()
                ips_failed[ip] = ips_failed.get(ip, 0) + 1

    return ips_failed


def mostrar_relatorio(contagem):
    ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    print("=" * 45)
    print("        FALHAS DE LOGIN POR IP")
    print("=" * 45)
    print(f"{'POS':<5} {'IP':<17} {'FALHAS':>6}")
    print("-" * 45)

    if not ordenado:
        print("Nenhuma falha encontrada")

    for posicao, (ip, quantidade) in enumerate(ordenado, 1):
        print(f"[{posicao}]   {ip:<17} {quantidade:>6}")

    print("=" * 45)
    print(f"IPs: {len(contagem)} | Total de falhas: {sum(contagem.values())}")


ips_failed = analizar_ips("ips_extraidos.log")
mostrar_relatorio(ips_failed)

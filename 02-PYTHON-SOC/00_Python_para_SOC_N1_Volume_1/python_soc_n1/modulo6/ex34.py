# Exercício 34 - Salvar relatório
# Em vez de apenas imprimir o resultado, grave o relatório em relatorio_soc.txt.


limite = 5
falhas_por_ip = {}
usuarios = {}
invalidos = set()

# 1. Ler e analisar o arquivo de log
with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        if "Failed password" in linha and " from " in linha:

            # Contar falhas por IP
            ip = linha.split(" from ")[1].split()[0]
            falhas_por_ip[ip] = falhas_por_ip.get(ip, 0) + 1

            # Contar falhas por usuário
            usuario = linha.split(" from ")[0].split()[-1]
            usuarios[usuario] = usuarios.get(usuario, 0) + 1

            # Identificar usuários inválidos
            if "invalid user" in linha:
                invalidos.add(usuario)

# 2. Ordenar os resultados
ips_ordenados = sorted(
    falhas_por_ip.items(),
    key=lambda x: x[1],
    reverse=True
)

usuarios_ordenados = sorted(
    usuarios.items(),
    key=lambda x: x[1],
    reverse=True
)

# 3. Filtrar IPs em alerta
ips_alerta = {}

for ip, quantidade in ips_ordenados:
    if quantidade >= limite:
        ips_alerta[ip] = quantidade

# 4. Identificar usuários não marcados como inválidos
existentes = [u for u in usuarios if u not in invalidos]

# 5. Criar e salvar o relatório
with open("relatorio_soc.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("=" * 55 + "\n")
    arquivo.write("       RELATÓRIO DE SEGURANÇA - finance-web\n")
    arquivo.write("=" * 55 + "\n\n")

    # SEÇÃO 1 - IPs
    arquivo.write("1. ALERTAS DE FORÇA BRUTA SSH\n")
    arquivo.write("-" * 55 + "\n")
    arquivo.write(f"Limite configurado: {limite} falhas\n\n")

    if ips_alerta:
        for ip, quantidade in ips_alerta.items():
            arquivo.write(
                f"[ALERTA] {ip:<16} {quantidade:>3} falhas\n"
            )
    else:
        arquivo.write("Nenhum IP atingiu o limite.\n")

    arquivo.write("\n")
    arquivo.write(f"IPs analisados: {len(falhas_por_ip)}\n")
    arquivo.write(f"IPs em alerta: {len(ips_alerta)}\n")

    # SEÇÃO 2 - USUÁRIOS
    arquivo.write("\n" + "=" * 55 + "\n")
    arquivo.write("2. USUÁRIOS ATACADOS\n")
    arquivo.write("-" * 55 + "\n")
    arquivo.write(
        f"{'USUÁRIO':<15} {'TENTATIVAS':>10}   STATUS\n"
    )
    arquivo.write("-" * 55 + "\n")

    for usuario, tentativas in usuarios_ordenados:
        if usuario in invalidos:
            status = "não existe"
        else:
            status = "[!] NÃO MARCADO INVÁLIDO"

        arquivo.write(
            f"{usuario:<15} {tentativas:>10}   {status}\n"
        )

    # SEÇÃO 3 - RESUMO
    arquivo.write("\n" + "=" * 55 + "\n")
    arquivo.write("3. RESUMO DA ANÁLISE\n")
    arquivo.write("-" * 55 + "\n")

    total = sum(usuarios.values())

    arquivo.write(f"Total de tentativas: {total}\n")
    arquivo.write(f"Usuários alvo: {len(usuarios)}\n")
    arquivo.write(f"Usuários marcados inválidos: {len(invalidos)}\n")
    arquivo.write(
        f"Usuários não marcados inválidos: {len(existentes)}\n"
    )

    arquivo.write(
        f"\n[!] Prioridade de investigação: "
        f"{', '.join(existentes) if existentes else 'Nenhum'}\n"
    )

    arquivo.write("=" * 55 + "\n")

print("Análise concluída!")
print("Relatório salvo em relatorio_soc.txt")

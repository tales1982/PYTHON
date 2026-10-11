# Exercício 35 - Função de extração
# Crie uma função extrair_ip(linha) que receba uma linha de autenticação e devolva o IP.


def extrair_ip(linha):
    if "from " not in linha:
        return None
    ip = linha.split("from ")[1].split(" port")[0]
    return ip


ARQUIVO_SAIDA = "ips_extraidos.log"
total = 0

with open("auth.log", "r") as arquivo, open(ARQUIVO_SAIDA, "w", encoding="utf-8") as saida:
    for linha in arquivo:
        if "Failed password" in linha or "Accepted password" in linha:
            ip = extrair_ip(linha)
            data_hora = " ".join(linha.split()[:3])  # "Oct 08 02:15:06"
            if "Failed password" in linha:
                saida.write(f"{data_hora} [FALHA]   {ip}\n")
            else:
                saida.write(f"{data_hora} [SUCESSO] {ip}\n")
            total += 1

print(f"{total} eventos salvos em {ARQUIVO_SAIDA}")

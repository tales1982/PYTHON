# Exercício 29 - Ações pós-login ★★★
# Extraia e mostre os comandos executados via sudo após o login suspeito
# Oct 07 02:15:02 finance-web sudo: root : COMMAND=/usr/bin/cat /etc/shadow

FAILED_PASS = "Failed password"
ACCEPT_PASS = "Accepted password"
SUDO_ROOT = "sudo: root : "
COMANDO = "COMMAND="

ips_failed = []
login_suspeito = False  # flag: vira True quando o IP com várias falhas consegue entrar
ip_suspeito = ""
hora_login = ""
comandos = []

with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        hora = linha.split()[2]

        if "from " in linha:
            ip = linha.split("from ")[1].split()[0]
            if FAILED_PASS in linha:
                ips_failed.append(ip)
            elif ACCEPT_PASS in linha and ips_failed.count(ip) > 1 and not login_suspeito:
                login_suspeito = True
                ip_suspeito = ip
                hora_login = hora

        elif SUDO_ROOT in linha and login_suspeito:
            comando = linha.split(COMANDO, 1)[1].strip()
            comandos.append((hora, comando))

print("=" * 55)
print("     AÇÕES PÓS-LOGIN - comandos sudo (finance-web)")
print("=" * 55)
if login_suspeito:
    print(f"Login suspeito: {ip_suspeito} às {hora_login}")
    print("-" * 55)
    if comandos:
        for numero, (hora, comando) in enumerate(comandos, 1):
            print(f"  [{numero}] {hora}  {comando}")
    else:
        print("  Nenhum comando sudo após o login")
else:
    print("  Nenhum login suspeito encontrado")
print("=" * 55)
print(f"Total de comandos: {len(comandos)}")

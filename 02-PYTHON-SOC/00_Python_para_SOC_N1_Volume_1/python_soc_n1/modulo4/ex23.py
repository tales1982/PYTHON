# Exercício 23 - Logins falhos ★★★
# Conte quantos eventos USER_LOGIN possuem res=failed

# type=USER_LOGIN_FAILED msg=audit(1791187720.440:601): pid=2301 uid=0 auid=1002 ses=5 res=failed
# type=USER_LOGIN msg=audit(1791187650.510:599): pid=2250 uid=0 auid=1001 ses=4 res=failed

USER_L = "USER_LOGIN"
RES = "res=failed"
usuario_count = {}

with open("audit.log", "r") as file:
    for l in file:
        tipo_login = l.split()[0].split("=")[1]
        tipo_res = l.split(")")[1].split()[-1]
        if USER_L == tipo_login and RES == tipo_res:
            usuario_count[USER_L] = usuario_count.get(USER_L, 0) + 1
print("=" * 40)
print("     RELATÓRIO DE LOGINS COM FALHA")
print("=" * 40)
print(f"Eventos {USER_L} com {RES}: {usuario_count.get(USER_L, 0)}")
print("=" * 40)

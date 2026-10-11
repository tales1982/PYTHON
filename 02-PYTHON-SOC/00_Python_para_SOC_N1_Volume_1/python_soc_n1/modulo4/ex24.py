# Exercício 24 - AUIDs envolvidos ★★★
# Extraia os valores de auid dos logins falhos e mostre quais usuários numéricos aparecem.

# type=USER_CMD msg=audit(1791187745.880:602): pid=2310 uid=1000 auid=1000 ses=3 cmd="ausearch -m USER_LOGIN" res=success
# type=USER_LOGIN msg=audit(1791187790.125:603): pid=2330 uid=0 auid=1000 ses=6 res=success

AUID = "auid="
LOGUIN_FALHOS = "res=failed"
tipo = "type=USER_LOGIN"
auids = []
with open("audit.log", "r") as file:
    for linha in file:
        try:
            primeira_parte = linha.split()[0]
            ultima_parte = linha.split()[-1]
            auid = linha.split("auid=")[1].split()[0]
            if (
                LOGUIN_FALHOS == ultima_parte
                and tipo == primeira_parte
                and auid not in auids
            ):
                auids.append(auid)
        except IndexError:
            continue  # deu erro? ignora e segue

        # print(ultima_parte)
print("=" * 40)
print("    USUÁRIOS (AUID) COM LOGIN FALHO")
print("=" * 40)
if auids:
    for auid in auids:
        print(f"  auid {auid}")
else:
    print("  Nenhum")
print("=" * 40)
print(f"Total de usuários: {len(auids)}")

# Exercício 32 - Usuários atacados
# Conte quantas tentativas malsucedidas cada nome de usuário recebeu.

usuarios = {}
invalidos = set()  # usuários que o sshd marcou como "invalid user" (não existem no servidor)

with open("auth.log", "r") as file:
    for l in file:
        if "Failed password " in l:
            user = l.split(" from")[0].split()[-1]
            usuarios[user] = usuarios.get(user, 0) + 1
            if "invalid user" in l:
                invalidos.add(user)

ordenado = sorted(usuarios.items(), key=lambda x: x[1], reverse=True)

print("=" * 50)
print("          USUÁRIOS ATACADOS - finance-web")
print("=" * 50)
print(f"{'USUÁRIO':<12} {'TENTATIVAS':>10}   STATUS")
print("-" * 50)
for usuario, tentativas in ordenado:
    if usuario in invalidos:
        status = "não existe"
    else:
        status = "[!] EXISTE"
    print(f"{usuario:<12} {tentativas:>10}   {status}")
print("=" * 50)

total = sum(usuarios.values())
existentes = [u for u in usuarios if u not in invalidos]
print(f"Total de tentativas: {total}")
print(f"Usuários alvo: {len(usuarios)} ({len(existentes)} existem, {len(invalidos)} não existem)")
print(f"[!] Prioridade de investigação: {', '.join(existentes)}")

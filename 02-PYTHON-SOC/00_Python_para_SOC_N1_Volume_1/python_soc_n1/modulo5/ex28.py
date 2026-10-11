# Exercício 28 - Linha do tempo ★★★
# Mostre, na ordem, somente os eventos relacionados ao usuário root.

# Oct 07 02:16:41 finance-web sudo: root : COMMAND=/usr/bin/useradd backupsvc

print("=" * 75)
print("                 LINHA DO TEMPO - usuário root (finance-web)")
print("=" * 75)
print(f"{'HORA':<10} {'ORIGEM':<7} EVENTO")
print("-" * 75)

with open("auth.log", "r") as file:
    for l in file:
        if "root" not in l:
            continue
        campos = l.split()
        hora = campos[2]
        programa = campos[4].rstrip(":")
        evento = l.split(": ", 1)[1].strip()
        print(f"{hora:<10} {programa:<7} {evento}")

print("=" * 75)

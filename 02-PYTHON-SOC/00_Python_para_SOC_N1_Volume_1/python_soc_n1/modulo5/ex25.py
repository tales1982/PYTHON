# Exercício 25 - Triagem ★★
# Conte o total de Failed password e Accepted password

total_failed = 0
total_accepted = 0

with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        campos = linha.split()
        resultado = campos[5]  # "Failed" ou "Accepted"
        metodo = campos[6]  # "password", "publickey"...

        if resultado == "Failed" and metodo == "password":
            total_failed += 1
        elif resultado == "Accepted" and metodo == "password":
            total_accepted += 1

print("=" * 30)
print("     TRIAGEM - finance-web")
print("=" * 30)
print(f"Failed password:   {total_failed}")
print(f"Accepted password: {total_accepted}")
print("=" * 30)

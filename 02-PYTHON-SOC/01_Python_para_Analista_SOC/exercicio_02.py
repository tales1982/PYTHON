usuario = "Joao"
ip = "10.0.0.15"
porta = 22
protocolo = "SSH"
score = 6.5
eh_admin = False

print(f"usuario = {usuario} -> {type(usuario)}")

print(f"porta = {porta} -> {type(porta)}")
print(f"score = {score} -> {type(score)}")
print(f"eh_admin = {eh_admin} -> {type(eh_admin)}")
print("Conexao em " + ip + ":" + str(porta))
print(f"ip = {ip} -> {type(ip)}")
print(f"protocolo = {protocolo} -> {type(protocolo)}")
print("10" + "5")   # "105": com texto, o + junta
print(10 + 5)       # 15: com número, o + soma

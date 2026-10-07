# Exercício 12 - Contador de falhas ★★
# Conte quantas linhas contêm Failed password e mostre no final: Total de falhas: X.


target="Failed password"
count=0


with open("auth.log","r") as file:
    for line in file:
        if target in line:
            count +=1

print(f"Total de falhas: {count}")
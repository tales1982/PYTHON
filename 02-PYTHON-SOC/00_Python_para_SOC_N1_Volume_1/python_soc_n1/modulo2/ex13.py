# Exercício 13 - Falhas para root ★★
# Conte somente as tentativas de login malsucedidas contra o usuário root.

target="Failed password"
target_root="root"
count=0 

with open("auth.log","r") as file:
    for l in file:
        if target in l and target_root in l:
            count+=1
            
print(f"Total de falhas para root: {count}")
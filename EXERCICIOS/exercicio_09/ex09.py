import argparse

parser = argparse.ArgumentParser()

# Argumento obrigatório (posicional)
parser.add_argument("nome")

# Flag opcional: se -s for passado, args.saudacao = True
parser.add_argument("-s", "--saudacao", action="store_true")

# Número opcional com padrão 1
parser.add_argument("-r", "--repeticoes", type=int, default=1)

args = parser.parse_args()

# Monta a mensagem com base nos argumentos
if args.saudacao:
    mensagem = f"Olá, {args.nome}! Seja muito bem-vindo(a)!"
else:
    mensagem = f"Olá, {args.nome}"

# Repete a mensagem o número de vezes definido
for _ in range(args.repeticoes):
    print(mensagem)



""" 
Criou o leitor → ArgumentParser() é o objeto que sabe ler o terminal
Disse o que esperar → add_argument("nome") registra que virá um valor chamado nome
Fez a leitura → parse_args() lê o que foi digitado e guarda em args
Depois disso, args.nome tem o valor que o usuário digitou ao rodar o script:
 """

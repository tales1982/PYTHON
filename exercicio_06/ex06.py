def dividir(a, b):
    if(b == 0):
        print("Erro: divisao por zero")
        return None
    return a / b

print(dividir(10, 2))
print(dividir(10, 0))


""" 
None significa:

ausência de valor
variável ainda não definida
função sem retorno
resultado inexistente
placeholder temporário durante o código
 """
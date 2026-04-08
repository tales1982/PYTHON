def dividir(a, b):
    if(b == 0):
        print("Erro: divisao por zero")
        return None
    return a / b

print(dividir(10, 2))
print(dividir(10, 0))


""" **Exercicio:**
Crie um arquivo `ex06.py` com uma funcao `dividir(a, b)` que:
- Tenta dividir `a` por `b`
- Se `b` for zero, imprime `"Erro: divisao por zero"` e retorna `None`
- Se funcionar, retorna o resultado

Teste com valores normais e com `b = 0`. """
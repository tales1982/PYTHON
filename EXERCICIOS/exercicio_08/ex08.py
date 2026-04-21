
visitados = set()

visitados.add("https://site.com")
visitados.add("https://site.com/pagina1")
visitados.add("https://site.com")
visitados.add("https://site.com/pagina2")

print(visitados)
print(f"Total de URLs únicas: {len(visitados)}")

url = "https://site.com/pagina1"

if(url in visitados):
    print(url)


""" 
O set() em Python é uma coleção de elementos únicos (sem repetição) e sem ordem definida.

Exemplo simples
numeros = {1, 2, 2, 3, 4}

print(numeros)
resultado: {1, 2, 3, 4}
 """


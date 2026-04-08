url = "https://site.com/imagens/foto.JPG?v=123"

result = url.split("/")
image = result[-1]
cleanerImage = image.split("?")
realAddress = cleanerImage[0].lower()

print(realAddress)

isJpg = realAddress.endswith(".jpg")
print(isJpg)



""" Manipulacao de Strings

**Conceito:** trabalhar com textos: dividir, limpar, transformar.

**Exercicio:**
Crie um arquivo `ex07.py` que:

Dada esta URL:
```
https://site.com/imagens/foto.JPG?v=123
```

1. Pegue apenas o nome do arquivo (`foto.JPG`)
2. Remova os parametros (`?v=123`)
3. Transforme em minusculo (`foto.jpg`)
4. Verifique se termina com `.jpg`

**Dica:**
```python
url = "https://site.com/imagens/foto.JPG?v=123"
partes = url.split("/")
print(partes[-1])   # pega o ultimo pedaco
 """
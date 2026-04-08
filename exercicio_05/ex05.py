EXTENSOES_VALIDAS = [".jpg", ".png", ".gif", ".bmp"]

def verificar_extensao(arquivo):
    for ext in EXTENSOES_VALIDAS:
        if arquivo.endswith(ext):
            return "valida"
    return "invalida"

print(verificar_extensao("foto.jpg"))
print(verificar_extensao("imagem.png"))
print(verificar_extensao("animacao.gif"))
print(verificar_extensao("documento.pdf"))

""" 
**Exercicio:**
Crie um arquivo `ex05.py` com uma funcao `verificar_extensao(arquivo)` que:
- Recebe o nome de um arquivo (ex: `"foto.jpg"`)
- Retorna `"valida"` se a extensao for `.jpg`, `.png`, `.gif` ou `.bmp`
- Retorna `"invalida"` caso contrario

Teste com pelo menos 4 arquivos diferentes. """
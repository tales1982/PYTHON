EXTENSOES_VALIDAS = (".jpg", ".png", ".gif", ".bmp")

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
Lista ([]) é mutável: você pode adicionar, remover ou alterar elementos depois de criada.
Tupla (()) é imutável: depois de criada, seus elementos não podem ser modificados.
 """
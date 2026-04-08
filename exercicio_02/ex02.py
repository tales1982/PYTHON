extencoes = [".jpeg", ".jpg", ".png", ".webp"]

for ext in extencoes:
    print(ext)

if (".gif" in extencoes):
    print("A extensao .gif esta na lista")
else:
    print("A extensao .gif NAO esta na lista")


""" 
**Exercicio:**
Crie um arquivo `ex02.py` com:
- Uma **lista** com 5 extensoes de imagem (`.jpg`, `.png`, etc)
- Imprima cada extensao usando um loop `for`
- Depois verifique se `.gif` esta na lista usando `in`
"""
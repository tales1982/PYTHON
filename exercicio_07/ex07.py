url = "https://site.com/imagens/foto.JPG?v=123"

result = url.split("/")
image = result[-1]
cleanerImage = image.split("?")
realAddress = cleanerImage[0].lower()

print(realAddress)

isJpg = realAddress.endswith(".jpg")
print(isJpg)


''' O método endswith() verifica se uma string termina com um determinado texto'''
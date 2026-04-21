from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Meu Site</h1>
    <a href="https://google.com">Google</a>
    <a href="https://github.com">Github</a>
    <img src="foto.jpg">
    <img src="logo.png">
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# texto do h1
print(soup.h1.text)

# links href
for link in soup.find_all("a"):
    print(link["href"])

# imagens src
for img in soup.find_all("img"):
    print(img["src"])


""" 
import requests
from bs4 import BeautifulSoup

url = input("Digite o endereço do site: ")

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # texto do h1
    if soup.h1:
        print("H1:", soup.h1.text)

    # links href
    print("\nLinks encontrados:")
    for link in soup.find_all("a"):
        print(link.get("href"))

    # imagens src
    print("\nImagens encontradas:")
    for img in soup.find_all("img"):
        print(img.get("src"))

else:
    print("Erro ao acessar o site:", response.status_code)
 """
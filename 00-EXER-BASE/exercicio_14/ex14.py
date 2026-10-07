import argparse
import requests
from bs4 import BeautifulSoup
import os

# 1 - Parse do endereco do site
parser = argparse.ArgumentParser()
parser.add_argument("nome")
arg = parser.parse_args()

try:
    # 2 - request do site
    response = requests.get(arg.nome, timeout=10)
    response.raise_for_status()
    html = response.text

    # 3 - BeautifulSoup para encontra as tags
    soup = BeautifulSoup(html, "html.parser")

    # 4 - Cria a pasta e salva os dados pra futuro controle
    os.makedirs("saida", exist_ok=True)

    linhas = []

    visited = set()
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href not in visited:
            visited.add(href)
            linhas.append(href + "\n")

    with open("saida/links.txt", "w") as f:
        f.writelines(linhas)

    # Lê e imprime o conteúdo
    with open("saida/links.txt", "r") as f:
        print(f.read())

except requests.exceptions.ConnectionError:
    print(f"Erro: não foi possível conectar ao site '{arg.nome}'")
except requests.exceptions.Timeout:
    print(f"Erro: o site '{arg.nome}' demorou demais para responder")
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except OSError as e:
    print(f"Erro ao salvar arquivo: {e}")


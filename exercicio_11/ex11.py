import requests

response = requests.get("https://httpbin.org/get")

if response.status_code == 200:
    print(response.text[:300])
else:
    print("Erro ao carregar a pagina:", response.status_code)

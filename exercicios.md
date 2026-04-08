# Exercicios Python - Spider

Exercicios baseados no que estudamos para construir o spider.
Faca um por um, na ordem. Nao pule etapas.

---

## 1. Variaveis

**Conceito:** guardar valores em caixinhas com nome.

**Exercicio:**
Crie um arquivo `ex01.py` e declare as seguintes variaveis:
- Seu nome
- Sua idade
- Se voce gosta de programar (verdadeiro ou falso)
- A URL do seu site favorito

Depois imprima todas elas com `print()`.

**Exemplo de saida esperada:**
```
Tales
25
True
https://google.com
```

---

## 2. Listas e Tuplas

**Conceito:** guardar varios valores em uma unica variavel.

**Exercicio:**
Crie um arquivo `ex02.py` com:
- Uma **lista** com 5 extensoes de imagem (`.jpg`, `.png`, etc)
- Imprima cada extensao usando um loop `for`
- Depois verifique se `.gif` esta na lista usando `in`

**Dica:**
```python
extensoes = [".jpg", ".png"]
for ext in extensoes:
    print(ext)
```

---

## 3. Dicionarios

**Conceito:** guardar pares de chave e valor.

**Exercicio:**
Crie um arquivo `ex03.py` com um dicionario que representa um usuario:
- `nome`
- `email`
- `ativo` (True ou False)

Imprima cada campo separadamente acessando pelas chaves.

**Dica:**
```python
usuario = {"nome": "Tales"}
print(usuario["nome"])
```

---

## 4. Funcoes

**Conceito:** blocos de codigo reutilizaveis com nome.

**Exercicio:**
Crie um arquivo `ex04.py` com uma funcao chamada `saudacao` que:
- Recebe um nome como parametro
- Retorna a string `"Ola, [nome]! Bem-vindo."`

Chame a funcao 3 vezes com nomes diferentes e imprima o resultado.

**Dica:**
```python
def saudacao(nome):
    return "Ola, " + nome

print(saudacao("Tales"))
```

---

## 5. Condicoes (if / else)

**Conceito:** executar codigo diferente dependendo de uma condicao.

**Exercicio:**
Crie um arquivo `ex05.py` com uma funcao `verificar_extensao(arquivo)` que:
- Recebe o nome de um arquivo (ex: `"foto.jpg"`)
- Retorna `"valida"` se a extensao for `.jpg`, `.png`, `.gif` ou `.bmp`
- Retorna `"invalida"` caso contrario

Teste com pelo menos 4 arquivos diferentes.

---

## 6. Try / Except

**Conceito:** tratar erros sem travar o programa.

**Exercicio:**
Crie um arquivo `ex06.py` com uma funcao `dividir(a, b)` que:
- Tenta dividir `a` por `b`
- Se `b` for zero, imprime `"Erro: divisao por zero"` e retorna `None`
- Se funcionar, retorna o resultado

Teste com valores normais e com `b = 0`.

---

## 7. Manipulacao de Strings

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
```

---

## 8. Set (conjunto)

**Conceito:** lista que nao aceita duplicatas.

**Exercicio:**
Crie um arquivo `ex08.py` que:
- Cria um `set()` chamado `visitados`
- Adiciona estas URLs:
  - `https://site.com`
  - `https://site.com/pagina1`
  - `https://site.com`  (repetida de proposito)
  - `https://site.com/pagina2`
- Imprime o set e mostra quantas URLs unicas existem
- Verifica se `https://site.com/pagina1` esta no set

---

## 9. Leitura de Argumentos (argparse)

**Conceito:** receber dados do usuario pelo terminal.

**Exercicio:**
Crie um arquivo `ex09.py` que aceita os seguintes argumentos:
- `nome` — obrigatorio
- `-s` ou `--saudacao` — opcional, ativa uma saudacao especial
- `-r` ou `--repeticoes` — numero de vezes para imprimir (padrao: 1)

Exemplos de uso:
```bash
python3 ex09.py Tales
python3 ex09.py Tales -s
python3 ex09.py Tales -r 3
```

---

## 10. Manipulacao de Arquivos

**Conceito:** criar pastas e salvar arquivos no disco.

**Exercicio:**
Crie um arquivo `ex10.py` que:
1. Cria uma pasta chamada `saida/`
2. Dentro dela, cria um arquivo `resultado.txt`
3. Escreve 5 linhas de texto no arquivo
4. Le o arquivo de volta e imprime o conteudo

**Dica:**
```python
import os
os.makedirs("saida", exist_ok=True)

with open("saida/resultado.txt", "w") as f:
    f.write("linha 1\n")
```

---

## 11. Requisicao HTTP

**Conceito:** buscar o conteudo de uma pagina web.

**Exercicio:**
Crie um arquivo `ex11.py` que:
1. Faz uma requisicao para `https://httpbin.org/get`
2. Imprime o status code da resposta
3. Se for 200, imprime os primeiros 300 caracteres do conteudo
4. Se falhar, imprime uma mensagem de erro

**Dica:**
```python
import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)
```

---

## 12. Parsing de HTML (BeautifulSoup)

**Conceito:** ler e extrair informacoes de um HTML.

**Exercicio:**
Crie um arquivo `ex12.py` com este HTML salvo numa variavel:

```python
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
```

Use BeautifulSoup para:
1. Imprimir o texto do `<h1>`
2. Imprimir todos os links (`href`) encontrados
3. Imprimir todos os `src` das imagens

---

## 13. Funcao Recursiva

**Conceito:** uma funcao que chama a si mesma.

**Exercicio:**
Crie um arquivo `ex13.py` com uma funcao `contar(numero, limite)` que:
- Imprime o numero atual
- Chama a si mesma com `numero + 1`
- Para quando `numero` chegar ao `limite`

Exemplo de saida para `contar(1, 5)`:
```
1
2
3
4
5
```

**Dica:** sempre tenha uma condicao de parada para nao entrar em loop infinito.

---

## 14. Desafio Final

**Conceito:** juntar tudo que aprendeu.

**Exercicio:**
Crie um arquivo `ex14.py` que:

1. Recebe uma URL pelo terminal (`argparse`)
2. Faz a requisicao HTTP para essa URL
3. Usa BeautifulSoup para encontrar todas as tags `<a>`
4. Imprime todos os links encontrados
5. Salva esses links em um arquivo `links.txt` dentro de uma pasta `saida/`
6. Usa `set()` para nao salvar links repetidos
7. Trata erros com `try/except`

Este exercicio e uma versao simplificada do spider que construimos.

---

## Como estudar

1. Faca os exercicios em ordem
2. Nao copie — tente escrever voce mesmo
3. Se travar, releia a explicacao do conceito
4. Teste com valores diferentes para entender o comportamento
5. So va para o proximo quando o atual estiver funcionando

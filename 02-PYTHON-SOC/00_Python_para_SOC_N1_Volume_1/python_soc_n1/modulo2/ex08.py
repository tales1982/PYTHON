# Exercício 8 - Lendo a primeira linha ★
# Crie um arquivo auth.log com três linhas de texto. Faça um programa que leia e mostre
# somente a primeira linha


with open("auth.log", "+r") as arquivo:
    linha = arquivo.readline()
    print(linha)
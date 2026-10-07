# Exercício 5 - Separando um log ★
# Use split() na linha abaixo e imprima cada pedaço separadamente.

text = "Oct 07 10:14:32 server sshd Failed password for root from 203.0.113.50"

textSplit = text.split()

for i in textSplit:
    print(i)

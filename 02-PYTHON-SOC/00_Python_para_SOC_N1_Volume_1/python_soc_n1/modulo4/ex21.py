# Exercício 21 - Timestamp e serial ★★
# Da primeira linha, extraia:
# Horário: 1791187488.870
# Serial: 595.
# type=CONFIG_CHANGE msg=audit(1791187488.870:595): auid=1000 ses=3 subj=unconfined


with open("audit.log", "r") as arquivo:
    linha = arquivo.readline()

dentro_parenteses = linha.split("(")[1].split(")")[0]   # "1791187488.870:595"
horario, serial = dentro_parenteses.split(":")

print(f"Horário: {horario}")
print(f"Serial: {serial}")

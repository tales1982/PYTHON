# Exercício 20 - Extraindo type ★★
# Da primeira linha, extraia somente CONFIG_CHANGE.

# type=USER_LOGIN msg=audit(1791187522.901:597): pid=2210 uid=0 auid=1001 ses=4 res=failed



with open("audit.log", "r") as file:
    l = file.readline()
    type_l = l.split()[0].split("=")[1]
    print(type_l)

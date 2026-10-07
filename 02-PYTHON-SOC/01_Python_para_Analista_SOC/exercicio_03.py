score = float(input("Score do alerta (0-10): "))

if score < 0 or score > 10:
    print("Score inválido!")
elif score >= 9:
    print("CRÍTICA - acionar resposta a incidente agora!")
elif score >= 7:
    print("ALTA - investigar em até 1 hora")
elif score >= 4:
    print("MÉDIA - investigar em até 8 horas")
elif score > 0:
    print("BAIXA - investigar em até 12 horas")
else:
    print("NENHUMA - sem ação necessária")

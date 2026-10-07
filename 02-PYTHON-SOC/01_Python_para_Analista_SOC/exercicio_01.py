analista = "Tales"
alerta = "Tentativa de login falhou"

id_alerta = 1001
origem = "192.168.1.50"
destino = "servidor-web01"
descricao = "Múltiplas falhas de login"


print("=== SOC - Painel de Alertas ===")
print(f"Novo alerta: {alerta}")
print("========================================")
print(f"ALERTA #{id_alerta}")
print(f"Origen      : {origem}")
print(f"Destino     : {destino}")
print(f"Descrisao   : {descricao}")
print(f"Analista de plantão: {analista}")
print("========================================")
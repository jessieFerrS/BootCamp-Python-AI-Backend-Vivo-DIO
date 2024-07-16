
def recomendar_plano(consumo):
    """ Recomenda plano de internet de acordo com o consumo """
    if consumo <= 10:
        return f'Plano Essencial Fibra - 50Mbps'
    elif 10 < consumo <= 20:
        return f'Plano Prata Fibra - 100Mbps'
    return f'Plano Premium Fibra - 300Mbps'

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))

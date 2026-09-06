'''
Programa desenvolvido para calcular o consumo elétrico de aparelhos domésticos de forma inteligente com o objetivo de ajudar usuários a estimar o gasto mensal de energia elétrica usando dados simples.
'''

# Entrada

aparelho = input('Aparelho: ') # O usuário informa o aparelho cujo gasto deseja calcular
potencia = float(input('Potência (W): ')) # A potência deve ser informada usando números
horasDia = float(input('Tempo médio de uso diário (horas): ')) # O tempo deve ser informado usando números

# Processamento

consumoMensal = (potencia * horasDia * 30) / 1000 # Fórmula realizará o cálculo com os números informados pelo usuário

# Saída

print('O aparelho ',aparelho,' possui consumo médio mensal de ',consumoMensal,'kWh/mês.') # Texto corrido que exibirá o resultado do cálculo para o usuário

'''
Sistema de desconto progressivo para uma loja. Solicitar ao usuário o valor da compra e aplicar o desconto de acordo com a tabela abaixo:
- Até R$ 200,00: 5% de desconto
- De R$ 200,01 a R$ 300,00: 10% de desconto
- Acima de R$ 300,00: 15% de desconto
Após, o programa deve exibir o valor do desconto aplicado e o valor final da compra após o desconto.
'''
valor_compra = float(input("Digite o valor da compra: R$ ")) # O usuário informa o valor da compra em R$
# Processamento do desconto progressivo
if valor_compra <= 200:
    desconto = valor_compra * 0.05
elif valor_compra <= 300:
    desconto = valor_compra * 0.10
else:
    desconto = valor_compra * 0.15
# Cálculo do valor final da compra após o desconto
valor_final = valor_compra - desconto
# Exibição dos resultados
print(f"Valor do desconto aplicado: R$ {desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")
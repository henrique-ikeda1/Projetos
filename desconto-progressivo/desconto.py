'''
Sistema de desconto progressivo para uma loja. 
'''
valor_compra = float(input("Digite o valor da compra: R$ ")) # O usuário informa o valor da compra em R$
# Processamento do desconto progressivo
if valor_compra < 200:
    desconto = valor_compra * 0.05
elif valor_compra >= 200 and valor_compra < 300:
    desconto = valor_compra * 0.10
else:
    desconto = valor_compra * 0.15
# Cálculo do valor final da compra após o desconto
valor_final = valor_compra - desconto
# Exibição dos resultados
print("Valor do desconto aplicado: R$ ",desconto)
print("Valor final da compra: R$ ",valor_final)
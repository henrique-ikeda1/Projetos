"""
Programa desenvolvido para pesquisa de satisfação a ser realizada com 50 pessoas.
Os entrevistados devem informar nome e idade, em seguida responder o grau de satisfação com o atendimento prestado (1-EXCELENTE, 2-BOM, 3-RUIM).
Ao final, o programa deve contabilizar a quantidade de respostas 1-EXCELENTE e 3-RUIM.
Realizar entrevista com 10 pessoas para validar o programa.
"""

# CONSTANTE

NUM_ENTREVISTADOS = 10 # Para o programa final, altere para 50

# CONTADORES

excelente = 0
ruim = 0

# ESTRUTURA DO PROGRAMA

## REPETIÇÃO FOR

for i in range(1, NUM_ENTREVISTADOS + 1): # Estrutura de repetição, onde i depende da contagem CONSTANTE + 1
    print(f"\nEntrevistado {i}") # String formatada, ou f-string, que pula a primeira linha e insere o número do entrevistado de acordo com a fórmula CONSTANTE + 1.
    
    nome = input("Digite o nome: ") # String para atribuir valor à variável nome.
    
    idade = int(input("Digite a idade: ")) # String de atribuição de valor à variável idade.
    
## REPETIÇÃO WHILE

    while True: # A estrutura aqui está indicando que deve seguir para a próxima iteração caso a condição seja verdadeira.
        opiniao = int(input("Opinião sobre o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): ")) # String de atribuição de valor à variável opiniao.
        
        if opiniao in (1, 2, 3): # Condição para respostas válidas
            break # Ação tomada se for resposta válida
        else: 
            print("Opção inválida! Digite 1, 2 ou 3.") # Ação tomada se a resposta for inválida
    
    if opiniao == 1:
        excelente += 1 # Condição para contagem de respostas 1
    elif opiniao == 3:
        ruim += 1 # Condição para contagem de respostas 3

# RESPOSTAS CONTABILIZADAS

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}") # Mostra o total de respostas 1
print(f"Quantidade de respostas RUIM: {ruim}") # Mostra o total de respostas 3

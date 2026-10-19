"""
Sistema de controle de água.
"""

# Importação das bibliotecas
from colorama import Fore, Style, init # Biblioteca externa para colorir o texto no terminal
import random # Biblioteca interna para gerar números aleatórios
import time # Biblioteca interna para manipulação de tempo
import os # Biblioteca interna para interagir com o sistema operacional

# Inicialização do colorama
init(autoreset=True)

# Lista de níveis do reservatório
niveis_reservatorio = [
    {"nível": 1, "mensagem": "Muito baixo (CRÍTICO)", "cor": Fore.RED},
    {"nível": 2, "mensagem": "Baixo", "cor": Fore.YELLOW},
    {"nível": 3, "mensagem": "Médio", "cor": Fore.GREEN},
    {"nível": 4, "mensagem": "Alto", "cor": Fore.CYAN},
    {"nível": 5, "mensagem": "Muito alto (ALERTA)", "cor": Fore.BLUE}
]

# Funções do programa

def definir_cor(nivel): # Define a cor conforme o nível
    for item in niveis_reservatorio:
        if item["nível"] == nivel:
            return item["cor"]
    return Fore.WHITE  # Cor padrão caso o nível não seja encontrado

def retornar_mensagem(nivel): # Define a mensagem conforme o nível
    for item in niveis_reservatorio:
        if item["nível"] == nivel:
            return item["mensagem"]
    return "Nível desconhecido"  # Mensagem padrão caso o nível não seja encontrado

def mostrar_situacao(nivel): # Mostra a situação do reservatório com a cor e mensagem apropriadas
    cor = definir_cor(nivel)
    mensagem = retornar_mensagem(nivel)
    print(f"{cor}Nível do reservatório: {nivel} - {mensagem}{Style.RESET_ALL}") # Resetando a cor após a mensagem

def sortear_nivel(): # Sorteia um nível do reservatório
    item_sorteado = random.choice(niveis_reservatorio)  # Sorteia um item da lista de níveis
    return item_sorteado["nível"]  # Retorna o nível sorteado

def limpar_tela(): # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')  # Comando para Windows ('cls') ou Unix/Linux ('clear')

def simular_monitoramento(quantidade_leituras=10, intervalo=5.5): # Simula o monitoramento do reservatório
    nivel_anterior = None

    for leitura in range(1, quantidade_leituras + 1):
        nivel = sortear_nivel()  # Sorteia um nível do reservatório
        while nivel == nivel_anterior:  
            nivel = sortear_nivel() # Garante que o nível sorteado seja diferente do anterior

        nivel_anterior = nivel  # Atualiza o nível anterior para a próxima iteração

        limpar_tela()  # Limpa a tela antes de mostrar a nova leitura
        print("=== MONITORAMENTEO DO RESERVATÓRIO DE ÁGUA ===\n")
        print(f"Leitura {leitura} de {quantidade_leituras}\n")
        mostrar_situacao(nivel)  # Exibe a situação do reservatório com a cor e mensagem apropriadas

        time.sleep(intervalo)  # Aguarda o intervalo definido antes da próxima leitura

print(Style.RESET_ALL + "\nMonitoramento concluído.\n") # Resetando o estilo padrão após o monitoramento

# Ponto de entrada do programa
if __name__ == "__main__":
    simular_monitoramento()  # Inicia a simulação do monitoramento do reservatório
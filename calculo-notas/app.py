"""
SISTEMA DE CÁLCULO DE NOTAS
"""

# Sistema de cálculo de notas para estudantes. Este aplicativo permite que os usuários insiram suas notas e calculem a média final, além de fornecer feedback sobre o desempenho acadêmico.

MEDIA_MINIMA = 6.0
PESO_ATIVIDADES = 0.50
PESO_PROVA = 0.25
PESO_TRABALHO = 0.25
TOTAL_ATIVIDADES = 5
MINIMO_ATIVIDADES = 3

# Validação do registro de entrega e da nota de uma avaliação.

def validar_avaliacao(avaliacao, nome):    
    if not isinstance(avaliacao, dict):
        raise ValueError(f"{nome} deve ser um registro de avaliação.")    
    if not isinstance(avaliacao.get("entregue"), bool):
        raise ValueError(f"Informe se {nome} foi entregue.")
    
    nota = avaliacao.get("nota")

    if not avaliacao["entregue"]:
        if nota is not None:
            raise ValueError(
                f"{nome} não entregue deve ter nota None."
            )
        
        return
    if (
        not isinstance(nota, (int, float))
        or isinstance(nota, bool)
        or not 0 <= nota <= 10
    ):
        
        raise ValueError(
            f"A nota de {nome} deve estar entre 0 e 10."
        )

# Retorno da nota; avaliação não entregue vale zero.

def nota_efetiva(avaliacao):  
    return avaliacao["nota"] if avaliacao["entregue"] else 0

# Contagem de quantas atividades foram efetivamente entregues.

def contar_atividades_entregues(atividades):
    return sum(atividade["entregue"] for atividade in atividades)

# Validação dos dados de todas as avaliações.

def validar_dados(prova, trabalho, atividades):    
    if len(atividades) != TOTAL_ATIVIDADES:
        raise ValueError("Devem ser cadastradas exatamente 5 atividades.")
    validar_avaliacao(prova, "prova")
    validar_avaliacao(trabalho, "trabalho")
    for indice, atividade in enumerate(atividades, start=1):
        validar_avaliacao(atividade, f"atividade {indice}")

# Cálculo da média ponderada inicial ou final.

def calcular_media(prova, trabalho, atividades):   
    validar_dados(prova, trabalho, atividades)
    soma_atividades = sum(
        nota_efetiva(atividade) for atividade in atividades
    )
    return (
        soma_atividades * (PESO_ATIVIDADES / TOTAL_ATIVIDADES)
        + nota_efetiva(prova) * PESO_PROVA
        + nota_efetiva(trabalho) * PESO_TRABALHO
    )

# Verificação dos critérios para realizar recuperação.

def verificar_elegibilidade(prova, trabalho, atividades):    
    nota_prova = nota_efetiva(prova)
    nota_trabalho = nota_efetiva(trabalho)
    quantidade = contar_atividades_entregues(atividades)

    if nota_prova == 0 and nota_trabalho == 0:
        return False, "Prova e trabalho estão zerados."

    if quantidade < MINIMO_ATIVIDADES:
        return False, "Menos de 3 atividades foram entregues."

    return True, "Critérios de recuperação atendidos."

# Substituição da menor nota ou, se forem iguais e não zeradas, substitui ambas pela nota de recuperação.

def aplicar_recuperacao(prova, trabalho, nota_recuperacao):

    if (
        not isinstance(nota_recuperacao, (int, float))
        or isinstance(nota_recuperacao, bool)
        or not 0 <= nota_recuperacao <= 10
    ):
        raise ValueError(
            "A nota de recuperação deve estar entre 0 e 10."
        )

    nota_prova = nota_efetiva(prova)
    nota_trabalho = nota_efetiva(trabalho)

    if nota_prova == 0 and nota_trabalho == 0:
        raise ValueError(
            "Recuperação não permitida: as duas notas estão zeradas."
        )
    if nota_prova == nota_trabalho: # Notas iguais e não zeradas: recuperação vale 50%.
        nota_prova = nota_recuperacao
        nota_trabalho = nota_recuperacao
    elif nota_prova < nota_trabalho: # Substitui somente a prova.
        nota_prova = nota_recuperacao
    else: # Substitui somente o trabalho.
        nota_trabalho = nota_recuperacao
    return nota_prova, nota_trabalho

# Cálculo das médias, verificação da elegibilidade e informe do resultado.

def calcular_resultado_final(
    prova, trabalho, atividades, nota_recuperacao=None
):    
    validar_dados(prova, trabalho, atividades)

    media_inicial = calcular_media(prova, trabalho, atividades)
    quantidade = contar_atividades_entregues(atividades)

    nota_prova = nota_efetiva(prova)
    nota_trabalho = nota_efetiva(trabalho)

    resultado = {
        "media_inicial": media_inicial,
        "media_final": None,
        "situacao": None,
        "motivo": None,
        "prova_entregue": prova["entregue"],
        "trabalho_entregue": trabalho["entregue"],
        "atividades_entregues": quantidade,
    }

    # Reprovação automática se as duas avaliações estão zeradas.
    if nota_prova == 0 and nota_trabalho == 0:
        resultado.update({
            "media_final": media_inicial,
            "situacao": "Reprovado",
            "motivo": "Prova e trabalho estão zerados."
        })
        return resultado

    # Menos de três atividades impede aprovação e recuperação.
    if quantidade < MINIMO_ATIVIDADES:
        resultado.update({
            "media_final": media_inicial,
            "situacao": "Reprovado",
            "motivo": "Menos de 3 atividades foram entregues."
        })
        return resultado

    # Aprovação direta.
    if media_inicial >= MEDIA_MINIMA:
        resultado.update({
            "media_final": media_inicial,
            "situacao": "Aprovado",
            "motivo": "Média mínima alcançada."
        })
        return resultado

    # Média insuficiente: verificar recuperação.
    elegivel, motivo = verificar_elegibilidade(
        prova, trabalho, atividades
    )

    if not elegivel:
        resultado.update({
            "media_final": media_inicial,
            "situacao": "Reprovado",
            "motivo": motivo
        })
        return resultado

    # Ainda não foi informada a nota da recuperação.
    if nota_recuperacao is None:
        resultado.update({
            "situacao": "Em recuperação",
            "motivo": motivo
        })
        return resultado

    nova_prova, novo_trabalho = aplicar_recuperacao(
        prova, trabalho, nota_recuperacao
    )

    # Calcula a média final sem alterar o registro original.
    atividades_com_nota = sum(
        nota_efetiva(atividade) for atividade in atividades
    )

    media_final = (
        atividades_com_nota * (PESO_ATIVIDADES / TOTAL_ATIVIDADES)
        + nova_prova * PESO_PROVA
        + novo_trabalho * PESO_TRABALHO
    )

    resultado.update({
        "media_final": media_final,
        "situacao": (
            "Aprovado" if media_final >= MEDIA_MINIMA else "Reprovado"
        ),
        "motivo": "Resultado calculado após a recuperação."
    })

    return resultado

# Exemplo de funcionamento do sistema de cálculo de notas.

prova = {"entregue": True, "nota": 4.0}
trabalho = {"entregue": True, "nota": 7.0}

atividades = [
    {"entregue": True, "nota": 8.0},
    {"entregue": True, "nota": 7.0},
    {"entregue": True, "nota": 6.0},
    {"entregue": False, "nota": None},
    {"entregue": False, "nota": None},
]

resultado = calcular_resultado_final(
    prova, trabalho, atividades, nota_recuperacao=8.0
)

print(f"Média inicial: {resultado['media_inicial']:.2f}")
print(f"Média final: {resultado['media_final']:.2f}")
print(f"Situação: {resultado['situacao']}")
print(f"Motivo: {resultado['motivo']}")
print(f"Prova entregue: {resultado['prova_entregue']}")
print(f"Trabalho entregue: {resultado['trabalho_entregue']}")
print(f"Atividades entregues: {resultado['atividades_entregues']}")
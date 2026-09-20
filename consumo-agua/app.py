"""
Projeto: Consumo de Água
Este projeto tem como objetivo monitorar e analisar o consumo de água de diferentes moradores e tipos de imóveis, fornecendo insights valiosos para uma campanha de conscientização ambiental.
"""
# Entrada de dados
tipo_imovel = input("Digite o tipo de imóvel (casa, apartamento, etc.): ") # O usuário deve informar o tipo de imóvel para que o sistema possa aplicar as regras de consumo adequadas. São esperados tipos como 'Casa', 'Apartamento'e 'Comercial', e o sistema irá processar o consumo de água com base nesse tipo.
consumo_agua = float(input("Digite o consumo de água em m³: ")) # O usuário deve informar o consumo de água em metros cúbicos (m³) para que o sistema possa avaliar se o consumo está dentro dos padrões esperados para o tipo de imóvel informado. O valor deve ser um número positivo, representando a quantidade de água consumida.
# Processamento de dados
if tipo_imovel == "Comercial":
    print("Tarifa comercial aplicada. Consulte o plano corporativo.") # Se o tipo de imóvel informado for 'Comercial', o sistema aplicará uma tarifa específica para estabelecimentos comerciais e sugerirá que o usuário consulte o plano corporativo para obter informações detalhadas sobre tarifas e políticas de consumo de água para empresas.
elif tipo_imovel == "Apartamento" and consumo_agua < 10:
    print("Consumo econômico – excelente controle de água!") # Se o tipo de imóvel for 'Apartamento' e o consumo de água for inferior a 10 m³, o sistema reconhecerá que o usuário está mantendo um consumo econômico, indicando um excelente controle de uso de água e incentivando a continuidade dessas práticas sustentáveis.
elif (tipo_imovel == "Apartamento" or tipo_imovel == "Casa") and consumo_agua <= 25:
    print("Consumo moderado – dentro do padrão residencial.") # Se o tipo de imóvel for 'Apartamento' ou 'Casa' e o consumo de água estiver entre 10 m³ e 25 m³, o sistema indicará que o consumo está dentro do padrão residencial, sugerindo que o usuário continue monitorando seu uso de água para manter a eficiência e sustentabilidade.
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.") # Se o consumo de água informado for superior a 25 m³, independentemente do tipo de imóvel, o sistema alertará o usuário sobre o consumo excessivo, recomendando a adoção de medidas de economia e a verificação de possíveis vazamentos para reduzir o desperdício de água e promover práticas mais sustentáveis.
'''
Sistema de verificação de temperatura do laboratório.
'''
# Este primeiro exercício lida com estruturas aninhadas
temperatura = float(input("Informe  a temperatura atual em °C: "))
if temperatura < 0:
    print("Temperatura abaixo de zero! Cuidado com o congelamento.")
else:
    if temperatura < 15:
        print("Frio intenso no labnoratório.")
    else:
        if temperatura < 25:
            print("Temperatura agradável.")
        else:
            print("Temperatura alta! Ligar sistema de refrigeração.")
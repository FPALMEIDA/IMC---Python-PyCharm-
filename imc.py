    # MÓDULO IMC

import estado_imc as calcular

peso = 0
altura = 0.0
nome = ""

print()
print("Olá, favor inserir os dados solicitados para calcular o IMC!")

nome = input("\nQual é o nome do paciente? ")

erro = True
while erro:
    try:
        peso = int(input("Qual é o peso do paciente? "))
        erro = False
    except:
        print("Valor do peso está incorreto!")


erro = True
while erro:
    try:
        altura = float(input("Qual é a altura do paciente? "))
        erro = False
    except:
        print("Valor da altura está incorreto!")


calcular.calcular_imc(peso, altura)

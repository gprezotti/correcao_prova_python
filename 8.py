def calcula_imc(peso, altura):
  # Calcular o IMC
  imc = peso / (altura ** 2)
  
  # Informa o IMC
  if imc < 17:
    print("Muito abaixo do peso")
  elif imc < 18.5:
    print("Abaixo do peso")
  elif imc < 25:
    print("Peso normal")
  elif imc < 30:
    print("Sobrepeso")
  elif imc < 35:
    print("Obesidade Grau I")
  elif imc < 40:
    print("Obesidade Grau II")
  else:
    print("Obesidade Grau III")
    

calcula_imc(77, 1.80)

'''
Meu código da prova tem o 'imc >= x' em todos os 'elif', o que não é necessário pois se torna óbvio que o imc será maior
que 'x' se ele não atender os requisitos da condicional anterior.

Exemplo:
if imc < 17:
  print("Muito abaixo do peso")
elif imc >= 17 and imc < 18.5:
  print("Abaixo do peso")

Nesse caso torna-se claro que se a primeira condicional não for atendida e a segunda for, o imc será maior que 17, sem 
ter que especificar.
'''
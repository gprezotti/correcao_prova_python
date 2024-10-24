alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))
if alpha > 0.1:
  print('Valor inválido para alpha')
else:
  if x < 0:
    print(alpha * x)
  else:
    print(x)
    

'''
Essa questão não tem muito o que comentar por eu ter acertado e estar pedindo um teste de mesa.

Não é possível especificar uma saída obtida, porém ao fazer o teste do mesa percebe-se que todas saídas obtidas são 
iguais as saídas esperadas, portando o código é válido para o que se propõe fazer.
'''
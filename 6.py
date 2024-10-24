# Alternativa A
def soma_diagonal_principal_a(matriz):
  somaA = 0
  for i in range(len(matriz)):
    somaA += matriz[i][i]
  return somaA



# Alternativa B
def soma_diagonal_principal_b(matriz):
  somaB = 0
  for i in range(len(matriz)):
    somaB += matriz[i][-i]
  return somaB



# Alternativa C
def soma_diagonal_principal_c(matriz):
  somaC = 0
  for linha in matriz:
    for elemento in linha:
      somaC += elemento
  return somaC



# Alternativa D
def soma_diagonal_principal_d(matriz):
  somaD = 0
  for i in range(len(matriz)):
    somaD += matriz[i][len(matriz) - i - 1]
  return somaD



# Alternativa E
def soma_diagonal_principal_e(matriz):
  somaE = 0
  for i in range(len(matriz)):
    somaE += matriz[len(matriz) - i - 1][i]
  return somaE


print(soma_diagonal_principal_a([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]))
print(soma_diagonal_principal_b([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]))
print(soma_diagonal_principal_c([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]))
print(soma_diagonal_principal_d([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]))
print(soma_diagonal_principal_e([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]))

'''
Também não tenho muito o que comentar nessa questão pois também acertei.

Meu raciocínio:
Dado "matriz[i][j]", para acessar os elementos da diagonal principal, i e j devem ser iguais, portanto nada melhor do que
utilizar a mesma letra para representá-los, garantindo assim que os números sempre serão iguais.
Garantido isso basta somar o elemento "matriz[i][i]" um com o outro.

Porém achei curioso o fato de todas alternativas (exceto a alternativa C) retornarem o mesmo valor, podendo assim ter
mais de uma alternativa correta.

Saída obtida da alternativa A: 60
Saída obtida da alternativa B: 60
Saída obtida da alternativa C: 300
Saída obtida da alternativa D: 60
Saída obtida da alternativa E: 60
Alternativa marcada: a
Alternativa correta: a
'''
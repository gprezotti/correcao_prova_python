from timeit import timeit
from memory_profiler import profile

lista_grande = list(range(1000000))
lista_com_duplicata = lista_grande + [1]


# Solução 1
def tem_duplicados_sol_1(lista):
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] == lista[j]:
        return True
  return False
tempo1 = timeit(lambda: tem_duplicados_sol_1(lista_com_duplicata))

@profile
def memoria_tem_duplicados_sol_1(lista):
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] == lista[j]:
        return True
  return False


# Solução 2
def tem_duplicados_sol_2(lista):
  lista_ordenada = sorted(lista)
  for i in range(len(lista_ordenada) - 1):
    if lista_ordenada[i] == lista_ordenada[i + 1]:
      return True
  return False
tempo2 = timeit(lambda: tem_duplicados_sol_2(lista_com_duplicata))

@profile
def memoria_tem_duplicados_sol_2(lista):
  lista_ordenada = sorted(lista)
  for i in range(len(lista_ordenada) - 1):
    if lista_ordenada[i] == lista_ordenada[i + 1]:
      return True
  return False

# Solução 3
def tem_duplicados_sol_3(lista):
  elementos_vistos = set()
  for elemento in lista:
    if elemento in elementos_vistos:
      return True
    elementos_vistos.add(elemento)
  return False
tempo3 = timeit(lambda: tem_duplicados_sol_3(lista_com_duplicata))

@profile
def memoria_tem_duplicados_sol_3(lista):
  elementos_vistos = set()
  for elemento in lista:
    if elemento in elementos_vistos:
      return True
    elementos_vistos.add(elemento)
  return False



print("### Solução 1 ###")
print(f"{tempo1} segundo")
memoria_tem_duplicados_sol_1(lista_com_duplicata)
print(tem_duplicados_sol_1(lista_com_duplicata))


print("\n### Solução 2 ###")
print(f"{tempo2} segundo")
memoria_tem_duplicados_sol_2(lista_com_duplicata)
print(tem_duplicados_sol_2(lista_com_duplicata))


print("\n### Solução 3 ###")
print(f"{tempo3} segundo")
memoria_tem_duplicados_sol_3(lista_com_duplicata)
print(tem_duplicados_sol_3(lista_com_duplicata))


'''
Nesse caso ao utilizar a biblioteca "timeit" fica claro que a solução 3 é mais eficiente em tempo.

Ordem por tempo (mais rápido para o mais lento):
1°) Solução 3
2°) Solução 2
3°) Solução 1

E utilizando a biblioteca "memory_profiler" fica claro que a solução 1 é a mais eficiente em espaço.

Ordem por espaço (menor para o maior):
1°) Solução 1
2°) Solução 2
3°) Solução 3

Saída obtida da solução 1: True
Saída obtida da solução 2: True
Saída obtida da solução 2: True
Alternativa marcada: b - Abordagem 2 é mais eficiente em tempo, mas consome mais espaço
Alternativa correta: c - Abordagem 3 é mais eficiente em tempo, mas consome mais espaço
                     d - Abordagem 1 é mais eficiente em espaço, mas menos eficiente em tempo
'''
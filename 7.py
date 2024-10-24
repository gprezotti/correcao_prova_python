# Código A
lista = [x for x in range(5)]
print(lista)


# Código B
listaB = list(range(5))
print(listaB)


# Código C
listaC = []
i = 0
while i < 5:
  listaC.append(i)
  i += 1
print(listaC)

'''
Não sabia que colocando somente "list(range(5))" formava uma lista com os cinco primeiros número começando em zero,
igual a lista formada nos outros casos.

Na hora da prova achei que o Código B não formaria uma lista, e sim retornaria um possível erro ou somente não ia 
"printar" nada.

Saída obtida Código A: [0, 1, 2, 3, 4]
Saída obtida Código B: [0, 1, 2, 3, 4]
Saída obtida Código C: [0, 1, 2, 3, 4]
Alternativa marcada: c - Apenas Código A e Código C
Alternativa correta: d - Todos os códigos A, B e C
'''
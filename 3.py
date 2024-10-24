def func(n):
  if n == 0:
    return 1
  else:
    return n * func(n - 1)
  
print(func(3))

'''
Achei que o código ia ficar "chamando" infinitamente a função "func(n)" pelo fato dela estar insirida dentro dela
mesma. Porém não é o que ocorre e a função dá um resultado correto.

Utilizando o código como exemplo:
Pensei que a função seria chamada pela primeira vez com n = 6, depois com n = 5, após com n = 4, infinitamente, 
gerando assim um erro de recursão infinita.

return n * func(n - 1)
return n * func((n - 1) - 1)
return n * func(((n - 1) - 1) - 1)
...

Saída obtida: 6
Alternativa marcada: e - Erro de Recursão Infinita
Alternativa correta: b - 6
'''
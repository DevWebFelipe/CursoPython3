"""
  args - Argumentos não nomeados
  * - *args (empacotamento e desenpacotamento)

"""

# Lembre-se de desampacotamento

x, y, * resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
  return x + y

def soma2(*args):
  total = 0
  print(type(args), args)

  for numero in args:
    total += numero

  return total

print(soma2(1,2,3,4,5,6,7))

print(1)

numeros = 1, 2, 3, 4, 5, 6, 7
outra_soma = soma2(*numeros)
print(outra_soma)

print(sum(numeros))
print(sum((1, 2, 3, 4)))
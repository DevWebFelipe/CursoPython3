"""
  For + Range
  range -> range(start, stop, step)

"""

# Na iteração, o último número não vai ser incluído, porque sempre vai partir de índice 0
numeros = range(10) # quero números de 0 a 10 (índice começa em 0)
print(numeros)
for numero in numeros:
  print(numero)

print()

numeros = range(5, 10) # quero números de 5 a 10 (índice começa em 0, então fica 5, 6, 7, 8, 9)
print(numeros)
for numero in numeros:
  print(numero)

print()

numeros = range(0, 10, 2) # quero números de 0 a 10 e pula de 2 em 2, um exemplo de aplicação, seria pegar os múltiplos de algum número
print(numeros)
for numero in numeros:
  print(numero)
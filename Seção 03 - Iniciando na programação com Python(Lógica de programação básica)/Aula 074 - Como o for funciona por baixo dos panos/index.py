"""
  Iterável -> str, range, etc (__iter__)
  Iterador -> quem sabe entregar um valor por vez
  next -> me entregue o próximo valor
  iter -> me entregue seu iterador

"""

texto_1 = 'Felipe' # iterável
iterador = iter(texto_1) # iterator

# for letra in texto:
while True:
  try:
    print(next(iterador))
  except StopIteration:
    break # o FOR faz examente o que ta aqui


print()

texto = 'Felipe'
numeros = range(0, 100, 8) # múltiplos de 8 de 0 a 100

for numero in numeros:
  print(numero)

print()
texto = 'Felipe'.__iter__()
print(texto)
print()
texto = iter('Felipe')
print(texto)
print()
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(next(texto))
print(next(texto))
print(next(texto))
print(texto.__next__())
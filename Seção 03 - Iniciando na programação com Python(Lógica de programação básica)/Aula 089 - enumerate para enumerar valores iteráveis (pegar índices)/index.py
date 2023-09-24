lista = ['item1', 'item2', 'item3']
lista.append('item4')

lista_enumerada = enumerate(lista)

print(lista)
print(lista_enumerada)

print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada))

for item in lista_enumerada:
  print('Não vai passar aqui, porque ali em cima já foi até o ultimo item da lista')
  print(item)

print() # dessa forma, passando o enumerate direto no for, não vai ter o problema que aconteceu ali em cima, porque dessa maneira, vai estar sempre recomeçando o enumerate
for item in enumerate(lista):
  indice, valor = item
  print(item)
  print(indice, valor)

print()
for indice, valor in enumerate(lista):
  print(indice, valor)

print()
for item in enumerate(lista):
  print('FOR da tupla')
  for valor in item:
    print(f'\t{valor}\n') # \n Adiciona uma quebra de linha, \t adiciona um tab

print()
for indice, valor in enumerate(lista):
  print(indice, valor, lista[indice])

print()
print(list(enumerate(lista, start=2))) # vai começar do indice 2, mas vai mostrar todos os itens da lista
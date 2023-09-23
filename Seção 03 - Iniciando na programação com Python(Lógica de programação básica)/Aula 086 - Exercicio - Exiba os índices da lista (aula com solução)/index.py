"""
  Exercício
  Exiba os índices da lista

"""

""" assim é como eu fiz """
lista = ['item 1', 'item 2', 'item 3']
indice = 0

for item_lista in lista:
  print(f'Valor no índice {indice} = {item_lista}')
  indice +=1

print()

""" essa é a solução do professor """
lista = ['Felipe', 'Giulia', 'Isis']
lista.append('Item 1')
indices = range(len(lista))

print(indices)

for indice in indices:
  print(indice, lista[indice], type(lista[indice]))

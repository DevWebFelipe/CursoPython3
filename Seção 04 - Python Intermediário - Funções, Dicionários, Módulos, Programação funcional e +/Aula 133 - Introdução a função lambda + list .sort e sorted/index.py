# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

def ordena(item):
  print(item)
  print()
  
  return item['nome']

def exibir_lista(lista):
  print(lista)
  print()

def exibir_item_lista(lista):
  for item in lista:
    print(item)
    
  print()

lista = [1, 35, 65, 85, 45, 10, 9]
lista2 = [1, 35, 65, 85, 45, 10, 9]

exibir_lista(lista)

lista.sort() # ordena a lista
exibir_lista(lista)

lista.sort(reverse=True) # ordena a lista inversamente
exibir_lista(lista)

exibir_lista(lista2)

lista2_ordenada = sorted(lista2) # faz uma cópia rasa da lista original e ordena a cópia
exibir_lista(lista2_ordenada)

lista_dicionario = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]

lista_dicionario.sort(key=ordena)
exibir_lista(lista_dicionario)
exibir_item_lista(lista_dicionario)

lista_dicionario2 = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]

exibir_lista(lista_dicionario2)

lista_dicionario2.sort(key=lambda item: item['sobrenome'])
exibir_lista(lista_dicionario2)

exibir_item_lista(lista_dicionario2)

l1 = sorted(lista_dicionario2, key=lambda item: item['sobrenome'])
l2 = sorted(lista_dicionario2, key=lambda item: item['nome'])

exibir_lista(l1)
exibir_item_lista(l1)

exibir_lista(l2)
exibir_item_lista(l2)
"""
  Listas em Python
  Tipo list - Mutável
  Suporta vários valores de qualquer tipo
  Conhecimentos reutilizáveis - índices e fatiamento
  Métodos úteis:
      append, insert, pop, del, clear, extend, +
  Create Read Update   Delete
  Criar, ler, alterar, apagar = lista[i] (CRUD)

"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2] # excluiu o item dois, todos os índices a direita foram movidos para a esquerda
print(lista) 
print(lista[2])
lista.append(50) # adicionou um novo índice no final da lista
lista.pop()  # deletou um o ultimo indice da lista
lista.append(60) # adicionou um novo índice no final da lista
lista.append(70) # adicionou um novo índice no final da lista
print(lista)
ultimo_valor = lista.pop(3) # removeu o indice 3 da lista (60)
print(lista, 'Removido,', ultimo_valor)

""" Meus exemplos """

lista_integer = [1, 2, 3]
lista_string = ['A', 'B', 'C']
lista_mista = []

item_lista_integer = 0
item_lista_string = 0

for item_lista_integer in lista_integer:
  lista_mista.append(item_lista_integer)

for item_lista_string in lista_string:
  lista_mista.append(item_lista_string)

print()
print(f'{lista_integer = }')
print(f'{lista_string = }')
print(f'{lista_mista = }')

lista_deletados = []
lista_deletados.append(lista_mista.pop(0)) # deletei o primeiro, ao deletar, o pop retorna o item deletado, então você pode salvá-lo
lista_deletados.append(lista_mista.pop()) # deletei o ultimo
print()
print(f'{lista_mista = }')
print(f'{lista_deletados = }')
print()

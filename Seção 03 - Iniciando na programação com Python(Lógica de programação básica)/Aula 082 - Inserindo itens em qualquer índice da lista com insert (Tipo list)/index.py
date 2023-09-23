"""
  Listas em Python
  Tipo list - Mutável
  Suporta vários valores de qualquer tipo
  Conhecimentos reutilizáveis - índices e fatiamento
  Métodos úteis:
      append - Adiciona um item ao final
      insert - Adiciona um item no índice escolhido
      pop - Remove do final ou do índice escolhido
      del - apaga um índice
      clear - limpa a lista
      extend - estende a lista
      + - concatena listas
  Create Read Update   Delete
  Criar, ler, alterar, apagar = lista[i] (CRUD)

"""

#       -4  -3  -2  -1
#        0   1   2   3
lista = [10, 20, 30, 40]
print('Começou a lista --', lista)

lista.append('Felipe')
print()
print('Adicionei o nome "Felipe" --', lista)

nome = lista.pop()
print()
print('Excluí o nome "Felipe" --', lista)

lista.append(1233)
print()
print('Adicionei o item "1233" --', lista)

del lista[-1] # deleta por índice, nesse caso, índice invertido, lembrando que começa de 0 -> 3 e invertido fica -4 -> -1
print()
print('Deletei o item "1233" --', lista)

lista.insert(2, 'novo valor') # índice onde vou inserir e valor que será inserido
print()
print('Adicionei um "novo valor" no meio da lista --', lista)

lista.clear()
print()
print('Limpei a lista inteira --', lista)

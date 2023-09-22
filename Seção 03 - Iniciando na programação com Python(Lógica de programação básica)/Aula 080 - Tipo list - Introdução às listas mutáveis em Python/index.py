"""
  Listas em Python
  Tipo list - Mutável
  Suporta vários valores de qualquer tipo
  Conhecimentos reutilizáveis - índices e fatiamento
  Métodos úteis: append, insert, pop, del, clear, extend, +

"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
print()

""" Meus exemplos """

minha_lista_string = ['café', 'leite', 'pão', 'ovo']
minha_lista_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
minha_lista_tudo_misturado = [123.5, 58, 'teste', ['outra', 'lista'], False]

print(minha_lista_string)
print(f'{minha_lista_string[1].upper() = }')
print()
print(minha_lista_integer)
print(f'{float(minha_lista_integer[0]) = }')
print()
print(minha_lista_tudo_misturado)
print(f'{minha_lista_tudo_misturado[3] = }')
print()


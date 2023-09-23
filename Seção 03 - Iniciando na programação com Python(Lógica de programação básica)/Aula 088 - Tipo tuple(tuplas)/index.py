# Tupla é uma lista imutável
# Ou seja, nela não são usados APPEND, POP entre outros

nomes = ['item1', 'item2', 'item3']
nomes_tuple = 'item1', 'item2', 'item3'
nomes_tuple_forma1 = ('item1', 'item2', 'item3')
nomes_tuple_forma2 = tuple(nomes)
nomes_list = list(nomes_tuple)
nomes[1] = 'outroItem'

print(nomes[1])
print(nomes_tuple, type(nomes_tuple))
print(nomes_tuple_forma1, type(nomes_tuple_forma1))
print(nomes_tuple_forma2, type(nomes_tuple_forma2))
print(nomes_list, type(nomes_list))
print(nomes, type(nomes))
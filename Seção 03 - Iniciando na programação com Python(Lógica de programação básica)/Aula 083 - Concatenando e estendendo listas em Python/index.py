lista_a = [1, 2, 3]
print(lista_a)

lista_b = [4, 5, 6]
print(lista_b)

lista_c = lista_a + lista_b
print(lista_c)

lista_d = lista_a.extend(lista_b) # a lista estendida aqui, será a lista_a
print(lista_d)
print(lista_a)
import pprint

def mostrar(valor):
    pprint.pprint(valor, sort_dicts=False,  width=40)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
mostrar(lista)
print()

# montar a lista acima com list comprehension

nova_lista_passo1 = [
    x
    for x in range(3)
]
mostrar(nova_lista_passo1)
print()

nova_lista_passo2 = [
    x
    for x in range(3)
    for y in range(3)
]
mostrar(nova_lista_passo2)
print()

nova_lista_passo3 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
mostrar(nova_lista_passo3)
print()

# uma lista com outra lista a cada item do for que varre o x
nova_lista = [
    [x for y in range(3)]
    for x in range(3)    
]
mostrar(nova_lista)
print()

nova_lista = [
    [(x, y)  for y in range(3)]
    for x in range(3)    
]
mostrar(nova_lista)
print()

# assim é possível fazer algo do tipo, para cada item de uma lista, adicionar alguma coisa
nova_lista = [
    [letra for letra in 'Felipe']
    for x in range(3)    
]
mostrar(nova_lista)
print()
# Yield from

def gen1():
    yield 1
    yield 2
    yield 3
    print('Finalizou gen1')

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6
    print('Finalizou gen2')

gen_unido = gen2()

for numero in gen_unido:
    print(numero)

print()

def gen3(gen):
    if gen is not None:
        yield from gen() # se eu não executar ele aqui, tenho que executar na passagem do argumento

    yield 7
    yield 8
    yield 9
    print('Finalizou gen3')

gen_unido2 = gen3(gen2) # aqui to passando o argumento, não executei, porque ta sendo executado dentro do método gen3

for numero in gen_unido2:
    print(numero)

print()
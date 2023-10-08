def generator(n = 0):
    yield 1 # Pausou a função e guarda o valor que tiver aqui no NEXT, quando chamar NEXT, ele vai entregar o valor que estiver aqui
    print('Continua....')
    yield 2
    print('Continua....')
    yield 3
    print('Continua....')
    yield 4
    print('Continua....')
    return 'ACABOU'

gen = generator(n = 0)
gen_for = generator(n = 0)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print()
print('Agora com FOR')
print()

for numero in gen_for:
    print(numero)

print()

def generator_dinamica(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen_while = generator_dinamica()
for numero in gen_while:
    print(numero)

print()

gen_while_dinamico = generator_dinamica(5, 12)
for numero in gen_while_dinamico:
    print(numero)

print()
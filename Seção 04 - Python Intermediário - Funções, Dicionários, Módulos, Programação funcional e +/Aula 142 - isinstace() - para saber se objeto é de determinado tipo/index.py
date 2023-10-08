# isintance = para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Felipe'}
]

for item in lista:
    if isinstance(item, set):
        print(f'{item} -> é um SET')

    if isinstance(item, tuple):
        print(f'{item} -> é uma TUPLA')

    if isinstance(item, list):
        print(f'{item} -> é uma LISTA')

    if isinstance(item, str):
        print(f'{item} -> é uma STRING')

    if isinstance(item, (int, float)):
        print(f'{item} -> é um NUMÉRICO')

    if isinstance(item, int):
        print(f'{item} -> é um INTEGER')

    if isinstance(item, float): # aqui 0 e 1 é booleano e também é um numérico
        print(f'{item} -> é um PONTO FLUTUANTE')

    if isinstance(item, bool):
        print(f'{item} -> é um BOOLEANO')

    if isinstance(item, dict):
        print(f'{item} -> é um DICIONÁRIO')

    print()

print()
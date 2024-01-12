def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res + 10
    return aninhada

def funca_antes_decorar(a,b,c):
    print(a,b,c)
    return decoradora

@funca_antes_decorar(1, 2, 3)
def soma(x, y):
    return x + y

multiplica = decoradora(lambda x, y: x * y)
dez_vezes_cinco = multiplica(10, 5)
print(dez_vezes_cinco)

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
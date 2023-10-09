# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

print('Inicio programa....')
print()
variavel = input('Digite um numero: ')

if (not variavel.isdigit()):
    raise ValueError('Erro no valor informado')

print()
print('Fim programa....')
print()

# Abaixo, exemplos do professor

def valida_se_dividendo_zero(d):
    if d == 0:
        raise ZeroDivisionError('Divisão por zero não existe')
    
    return True

def valida_se_inteiro(*args):
    for argumento in args:
        tipo_valor = type(argumento)
        if not isinstance(argumento, (float, int)):
            raise TypeError(f'"{argumento}" deve ser um do tipo número. '
                            f'Tipo recebido: "{tipo_valor.__name__}"'
            )

    return True


def divide(n, d):
    valida_se_dividendo_zero(d)
    valida_se_inteiro(n, d)
    return n / d

print(divide(8, '15'))
print()
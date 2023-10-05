def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return (x + y) # criando uma função lambda para essa função

print(
    executa(
        lambda x, y: x + y, # função lambda, passei o soma como função anonima
        2, 4), # valores dos argumentos x e y
    #executa(soma, 2, 3), # passei o soma normal, como um argumento, como esse argumento é uma função que espera dois parametros, eu passe o 2 e o 3, que vão nos *args
    #soma(5, 5)
)

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return (numero * multiplicador)
#     return multiplica

#duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
# aqui vamos ter dois lambda
# 1º recebe um argumento M que é o multiplicador
# o retorno da primeira função é outra função, que também pode ser uma função anonima(lambda)
# então o 2º vai ser uma função anonima(lambda) que também vai receber um argumento que será o N
# a 2ª função anonima(lambda) vai retornar o argumento M multiplicado pelo argumento N

print(duplica(2))


print(
    executa(
        lambda *args: sum(args), # declaração da função anonima
        1, 2, 3, 4, 5, 6, 8, 9, 7 # valores dos argumentos
    )
)
# ITERABLE -> Guarda os valores sequencialmente
# ITERATOR -> Entrega sempre o próximo valor, 1 valor por vez, a única coisa que o ITERATOR sabe é o próximo valor, ele não consegue acessar o valor anterior, não consegue saber o tamanho, nada, apenas sabe qual o próximo valor em ordem
# o FOR basicamente usa o ITERATOR para poder 'varrer' uma lista, de forma a encerrar o laço depois de varrer o ultimo registro da lista

# para eu ter um iterator, tenho que ter dentro do meu iterável, um obejto __iter__
# depois, preciso que algumém acesso através do iter() o meu iterável, assim, terei um iterator

iterable = ['Eu', 'Tenho', '__iter__']
#iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable) # tem __iter__ e __next__

# Gerators -> Funções que sabem pausar
# Iterator -> Classe que tem que ter método next e método iter

# todo generator é um iterator, pois pode-se navegar nele, pedir next, fazer for etc, mas o iterator não é um generator

lista = [n for n in range(10000)]
generator = (n for n in range(10000)) # se eu quero uma lista com muitos objetos ou objetos muito grandes, algo assim, e não vou usar tudo ao mesmo tempo, então posso usar o generator (só trocar o colchetes para parentese) e vou ter uma lista que consigo iterar sobre ela sem ocupar todo o espaço da memória do computador
print(lista)
print()
print(generator)
print()
for teste in generator:
    print(teste)
    if teste == 10:
        break

print()

# eu também poderia gerar listas menores

# NECESSÁRIO MUITA ATENÇÃO, O GENERATOR1 É UM ITERATOR CERTO? ENTÃO ELE SÓ CONHECE O NEXT CORRETO? ELE NÃO SABE QUEM VEIO ANTES, E QUEM VEM DEPOIS DO PRÓXIMO, NÃO SABE O TAMANHO TOTAL NEM NADA
# ENTÃO, TEM QUE FICAR ATENTO, POIS A PRÓXIMA ITERAÇÃO SOBRE ESSE GENERATOR1, CONTINUARÁ DE ONDE PAROU A ITERAÇÃO ANTERIOR

lista_teste = []
for teste in generator:
    lista_teste.append(teste)
    if teste == 20:
        break

print(lista_teste)
print()

# Para o generator, também sabemos que não tem como saber o tamanho máximo, porém, tem uma coisa que podemos fazer, podemos importar a biblioteca sys, e usar o método size of para saber o tamanho em byts, assim, podemos que a Generator1 mesmo tendo o mesmo tamanho(em índices) que GENERATOR, ela ocupa menos da metade do espaço na memória

# Outro detalhe muito interessante, se eu aumentar a capacidade em ambas as listas, a variável lista vai aumentar seu tamanho em byts, pois ela já salva na memória, mas a variável generator não, isso porque ela não salva os dados na memória do computador, então ficará sempre com o tamanho inicial

# Por isso genarator é uma função que sabe pausar, ele está parado na primeira execução, só irá trazer o próximo valor, quando for dado next()

# Já a vantagem da lista, é que como já está na memória, eu posso acessar qualquer índice, acessar o tamanho com LEN, enfim, pode-se trabalhar em cima desses dados

import sys
print(f'{sys.getsizeof(lista) = }')
print(f'{sys.getsizeof(generator) = }')
print()

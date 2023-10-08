# ITERABLE -> Guarda os valores sequencialmente
# ITERATOR -> Entrega sempre o próximo valor, 1 valor por vez, a única coisa que o ITERATOR sabe é o próximo valor, ele não consegue acessar o valor anterior, não consegue saber o tamanho, nada, apenas sabe qual o próximo valor em ordem
# o FOR basicamente usa o ITERATOR para poder 'varrer' uma lista, de forma a encerrar o laço depois de varrer o ultimo registro da lista

# para eu ter um iterator, tenho que ter dentro do meu iterável, um obejto __iter__
# depois, preciso que algumém acesso através do iter() o meu iterável, assim, terei um iterator

iterable = ['Eu', 'Tenho', '__iter__']
#iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable) # tem __iter__ e __next__

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print()

# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

print(list(range(10))) # essa forma, é uma lista meio que automatica que o Python criou
print()

lista = []

for numero in range(10): # essa forma é uma lista 'manual' que estamos inserindo item a item e podemos 
# inserir uma lógica no meio do caminho, por exemplo, para inserir apenas os numeros pares 
# ou algo do tipo
    lista.append(numero)
print(lista)
print()

# Agora vamos usar list comprehension

# na esquerda do for, tem que colocar o que será inserido na lista, nesse caso, vou inserir NUMERO
lista = [numero for numero in range(10)]
print(lista)
print()

lista = [
    numero * 2 # determina o que será inserido na lista
    for numero in range(10) # determina as repetições
]
print(lista)
print()

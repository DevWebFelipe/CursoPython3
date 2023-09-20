"""
Iterando strings com while

"""

nome = 'Felipe Texeira' # Strings são iteráveis, como arrays, podem ser 'varridas'
qtd_caracteres = len(nome)
contador = 0

while contador < qtd_caracteres:
  print(nome[contador])
  contador += 1

print()

contador = qtd_caracteres - 1 # índice começa de zero, então vai ter 1 unidade a menos de índice
# que quantidade de caracteres
while contador >= 0:
  print(nome[contador])
  contador -= 1

print()

contador = 0
nova_string = ''
while contador < qtd_caracteres:
  nova_string += nome[contador] + '*'
  contador += 1

print(nova_string[0:len(nova_string) - 1])

print()

contador = 0
nova_string = ''
while contador < qtd_caracteres:
  nova_string += '*' + nome[contador]
  contador += 1

print(nova_string)
print()
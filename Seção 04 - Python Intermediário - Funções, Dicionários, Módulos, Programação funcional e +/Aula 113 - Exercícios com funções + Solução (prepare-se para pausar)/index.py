# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Minha solução
def multiplicador(*args):
  total = 1
  for numero in args:
    total *= numero
  return total

total = multiplicador(2, 5, 6, 8)
print(total)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# Minha solução
def numero_par(numero):
  return numero % 2 == 0

print(f'{numero_par(7) = }')
print(f'{numero_par(12) = }')

# solução professor

def numero_par(numero):
  multiplo_de_dois = numero % 2 == 0
  
  if multiplo_de_dois:
    return f'{numero} é par'
  
  return f'{numero} é ímpar' 
"""
  if multiplo_de_dois:
    return f'{numero} é par'
  else:
    return f'{numero} é ímpar' 
"""

print(numero_par(7))
print(numero_par(12))
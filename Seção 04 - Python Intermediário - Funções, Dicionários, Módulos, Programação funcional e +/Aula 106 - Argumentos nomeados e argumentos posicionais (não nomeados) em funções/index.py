"""
  Argumentos nomeados e não nomeados em funções Python
  Argumento nomeado tem nome com sinal de igual
  Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma(x, y, z):
  print(f'{x = } + y = {y} + z = {z}', '|', 'x + y + z = ', x + y + z)

print(soma(5, 9, 9)) # essa função não ta retornando nada, então vai retornar None
print()
soma(1, 2, 5) # depende da ordem
soma(2, 5, 1) # depende da ordem
soma(y=2, z=5, x=1) # independe da ordem
soma(2, 5, z=1)



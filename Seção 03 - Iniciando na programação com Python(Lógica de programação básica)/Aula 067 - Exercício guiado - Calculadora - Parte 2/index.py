""" Calculadora com while """

while True:
  numero_1 = input('Digite um número: ')
  numero_2 = input('Digite outro número: ')
  operacao = input('Digite a operacao (+-/*): ')

  numeros_validos = None

  try:
    numero_1_float = float(numero_1)
    numero_2_float = float(numero_2)
    numeros_validos = True
  except:
  #except Exception as error:
  #  print(error)
    numeros_validos = None

  if numeros_validos is None:
    print('Os números não são válidos! Verifique.')
    print()
    continue

  operadores_permitidos = '+-/*'

  if operacao not in operadores_permitidos:
    print('Operacao inválida!')
    print()
    continue

  if len(operacao) > 1:
    print('Informe apenas uma operação!')
    print()
    continue

  

  # .lower -> joga tudo pra minúsculo
  # .startswith -> verifica se a string começa com uma determinada letra
  # .endwith -> verifica se a string termina com uma determinada letra
  if input('Quer sair? [s]im: ').lower().startswith('s'):
    break

  print()
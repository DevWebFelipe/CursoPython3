"""
  Introdução ao try/except
  try -> tentar executar o código
  except -> ocorreu algum erro ao tentar executar

"""

numero_a_ser_dobrado_str = input('Deternmie um numero a ser dobrado: ')

print(numero_a_ser_dobrado_str.isdigit()) # tem várias funções aqui que podem ser usadas, a 'isdigir' retorna
# um boolean, validando se foram digitados apenas números no campo

try: # tratamento de erro
  numero_a_ser_dobrado_float = float(numero_a_ser_dobrado_str)
  print('STR:', numero_a_ser_dobrado_str)
  print('FLOAT', numero_a_ser_dobrado_float)
  print(f'O dobro de {numero_a_ser_dobrado_str} é {(float(numero_a_ser_dobrado_float) * 2):.2f}')
except:
  print('Valor informado não é um número inteiro válido!')

# com o método acima dentro do print, da pra fazer um if
if numero_a_ser_dobrado_str.isdigit():
  numero_a_ser_dobrado_float = float(numero_a_ser_dobrado_str)
  print(f'O dobro de {numero_a_ser_dobrado_str} é {(float(numero_a_ser_dobrado_float) * 2):.2f}')
else:
  print('Valor informado não é um número inteiro válido!')
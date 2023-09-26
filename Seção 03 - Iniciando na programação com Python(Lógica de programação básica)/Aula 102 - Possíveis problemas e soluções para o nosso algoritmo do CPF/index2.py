import re
import sys # aqui tem um exit igual no delphi

cpf_recebido = input('Dgite seu CPF: ')

cpf_tratado = re.sub(
  r'[^0-9]', 
  '',
  cpf_recebido
)

# (cpf_tratado[0] * len(cpf_tratado)
# isso aqui, me diz se o primeiro caractere é repetido em toda a string
# ou seja 11111, 22222, 33333, 55555

if cpf_tratado == (cpf_tratado[0] * len(cpf_tratado)):
  print(f'"{cpf_tratado}" isso não é um CPF')
  sys.exit() # tem que dar import no sys

nove_digitos = cpf_tratado[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
  resultado_digito_1 += (int(digito) * contador_regressivo_1)
  contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10 ) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
  resultado_digito_2 += (int(digito) * contador_regressivo_2)
  contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado == cpf_tratado:
  print(f'{cpf_tratado} é válido!')
else:
  print(f'{cpf_tratado} é inválido!')
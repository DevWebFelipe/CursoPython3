import re

cpf_recebido = '091.502.259-10'\
  .replace('.', '')\
  .replace('-', '')
print(f'{cpf_recebido = }')
print()

"""
  Sobre o cpf_recebido1 abaixo

  Parametro 1 (
    r -> Expressões regulares, tem que usar dar um import re para poder usar
    re.sub -> vou usar para substituir alguma coisa
    r'' -> Expressão regular que vou usar para substituir
    r'[0-9]' -> tudo que for de 0 a 9
    r'[^0-9]' -> (^) o circunflexo é como se fosse um NOT, então, tudo que não for de 0 a 9
  )

  Parametro 2 (
    '' -> vou substituir o que ta atender o parametro 1 pelo que tiver no parametro dois
  )

  Parametro 3 (
    '091.502.259-10' -> String onde vou aplicar minha expressão regular
  )
"""
cpf_recebido1 = re.sub(
  r'[^0-9]', 
  '',
  '091.502 agora posso ter qualquer coisa aqui no meio .259-10'
)
print(f'{cpf_recebido1 = }')
print()

nove_digitos = cpf_recebido1[:9]
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

if cpf_gerado == cpf_recebido1:
  print(f'{cpf_recebido1} é válido!')
else:
  print(f'{cpf_recebido1} é inválido!')
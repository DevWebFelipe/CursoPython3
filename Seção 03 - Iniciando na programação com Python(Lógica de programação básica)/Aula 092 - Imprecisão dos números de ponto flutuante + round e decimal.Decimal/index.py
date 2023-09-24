"""
  Imprecisão de ponto flutuante
  Double-precision floating-point format IEEE 754
  https://en.wikipedia.org/wiki/Double-precision_floating-point_format
  https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

"""

import decimal

numero_1 = 0.1 # decimal.Decima('0.1') fazendo dessa forma, também vai corrigir o 0.799999
numero_2 = 0.7 # 0.1 gera uma parada complicada, gera na verdade 0.9999 ficando 0.799999, é confuso
numero_3 = numero_1 + numero_2
print(f'{numero_3 = }')
print(f'{numero_3 = :.2f}')
print(f'{round(numero_3, 1) = }') #  igual o Delphi, valor que vai arredondar e quantidade de casas que vai arredondar
print(f'{round(numero_3, 2) = }') #  igual o Delphi, valor que vai arredondar e quantidade de casas que vai arredondar
print(f'{decimal.Decimal(numero_3) = }')
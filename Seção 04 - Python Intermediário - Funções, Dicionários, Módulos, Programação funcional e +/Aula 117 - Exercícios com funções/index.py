# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplica_valor(valor):
  def valor_multiplicado(qtd_mult):
    return valor * qtd_mult
  return valor_multiplicado

valor_duplicado = multiplica_valor(5)
valor_triplicado = multiplica_valor(5)
valor_quadruplicado = multiplica_valor(5)

for i in [2, 3, 4]:
  print(f'{valor_duplicado(i) = }')
"""
  Operação ternária (condicional de uma linha)
  <valor> if <> condicao else <outro valor>

"""

print('Valor' if True else 'Outro valor')
print('Valor' if False else 'Outro valor' if False else 'Fim') # melhor não usar, fica complexo, mas da pra fazer
print()

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'

print(variavel)
print()

digito = 9
novo_digito = 0 if digito > 9 else digito
novo_digito2 = digito if digito <= 9 else 0

print(novo_digito)
print(novo_digito2)


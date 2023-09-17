"""
  Flag(Bandeira) - Marca um local
  None = não valor
  is e is not = é ou não é(tipo, valor, identidade)
  id = identidade

  condicao = False

  if condicao:
    print('Faça algo')
  else:
    print('Não faça algo')
"""

v1 = 'a'
v2 = 'a'
print(f'ID {v1=} -> {id(v1)}') # retorna a identidade dessa variável que está na meória
print(f'ID {v2=} -> {id(v2)}') # nesse caso, ambas as variáveis tem o mesmo 'VALOR', então o python otimiza isso
# gravando elas no mesmo indereço de memória, logo, terão o mesmo id

v2 = 'b'
print(f'ID {v2=} -> {id(v2)}') # quando eu altero o valor da variável, aí ele salva em um endereço de memória
# diferente, gerando um novo ID

# é através desse ID que o Python busca os valores que estão armazenados na memória e retorna o valor
# correspondente a esse ID, por isso variáveis com mesmo valores, podem ter o mesmo ID, irão retornar
# a mesma coisa, logo, não é preciso ocupar a memória com dois valores iguais
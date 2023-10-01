import index

pessoa = index.pessoa

# VALUES -> Retorna um dict_values, que é uma 'lista'(porém, não funciona como lista, caso queira usar como lista, tem que usar 'coersão' ou seja, converter para lista, ou tupla etc) com os valores que tem dentro do dicionário

print(f'{pessoa.values() = }')
print(f'{type(pessoa.values()) = }')
print(f'{list(pessoa.values()) = }')
print(f'{list(pessoa.values())[0] = }')
print(f'{list(pessoa.values())[1] = }')
print(f'{type(list(pessoa.values())) = }')
print()

# É possível também iterar sobre PESSOA, por padrão, vai retornar as chaves, mas posso passar o que quero retornar, nesse caso, values

for valor in pessoa.values():
  print(valor)
import index

pessoa = index.pessoa

# GET -> Pode ser usado para saber se uma determianda chave existe ou não dentro de um dicionário, também pode retornar um valor como default caso a chave não exista dentro do dicionário

print(pessoa.get('nome')) # retorna o valor da chave NOME
print(pessoa.get('fone')) # retorna NONE caso a chave IDADE não exista dentro do dicionário PESSOA
print(pessoa.get('fone', 0)) # retorna 0 caso a chave IDADE não exista dentro do dicionário PESSOA


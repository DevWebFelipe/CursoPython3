import index

pessoa = index.pessoa

# UPDATE -> Atualiza um dicionário com outro dicionário, vai atualizar conforme as chaves que encontrar, não precisa passar um dicionário em uma variável, pode ser feito direto também, caso seja passado uma chave no update que não existe no dicionário base, essa chave será criada, caso no dicionário base exista uma chave que não tem no update, não será mexido na chave do dicionário base

print(f'{pessoa = }')
print()

pessoa_att = {
    'nome': 'Giulia Gabrielle',
    'sobrenome': 'Breis Texeira',
    'idade': 25,
    'idade': 27,
    'idade': 23, 
    'altura': 1.48,
}

print(f'{pessoa_att = }')
print()
pessoa.update(pessoa_att)

print(f'{pessoa = }')
print()

pessoa.update({
  'nome': 'Isis Gabrille',
  'sobrenome': 'Texeira',
  'nova_chave': 'novo valor'
})

print(f'{pessoa = }')
print()

# Além das formas acima, também pode-se utilizar argumentos nomeados

pessoa.update(nome='Novo nome', idade=30, teste='novo_campo')
print(f'{pessoa = }')
print()

# outra forma de fazer, pode ser copm tuplas ou listas

var_tupla = (('nome', 'tupla'), ('idade', 8), ('teste2', 'outro_valor')) # sempre deixar uma virgula sobrando em tuplas quando tiver APENAS 1 ITEM
# var_lista = [('nome', 'lista'), ('idade', 8), ('teste2', 'com lista')]
var_lista = [['nome', 'lista'], ['idade', 8], ['teste2', 'com lista']]

pessoa.update(var_tupla)
print(pessoa)
print()

pessoa.update(var_lista)
print(pessoa)
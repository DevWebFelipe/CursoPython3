""" EU TO USANDO DESSA FORMA, MAS SEI QUE NÃO É COMENTÁRIO, PORÉM FICA MAIS FÁCIL DE FAZER AS ANOTAÇÕES
  Operadores in e not in
  Strings são iteráveis (quer dizer que é como um array, da pra navegar entre cada índice)
  0 1 2 3 4 5 - índice positivo da string FELIPE
  f e l i p e
 -6-5-4-3-2-1 - índice negativo da string FELIPE

"""

nome = 'Felipe'
print(nome[0], nome[5], nome[-6], nome[-1], sep='   ') # acessa-se o índice da mesma maneira que no delphi
print(nome[1], nome[4], nome[-5], nome[-2], sep='   ')
print(nome[2], nome[3], nome[-4], nome[-3], sep='   ')
print(nome[3], nome[2], nome[-3], nome[-4], sep='   ')
print(nome[4], nome[1], nome[-2], nome[-5], sep='   ')
print(nome[5], nome[0], nome[-1], nome[-6], sep='   ')

print(15 * '-')
print('á' in nome) # aqui já verifica se a letra á está entre as letras da string FELIPE
print('Fe' in nome) # é igual ao Pos do delphi
print('li' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'"{encontrar}" está em "{nome}"')
else:
  print(f'"{encontrar}" não está em "{nome}"')

print(15 * '-')
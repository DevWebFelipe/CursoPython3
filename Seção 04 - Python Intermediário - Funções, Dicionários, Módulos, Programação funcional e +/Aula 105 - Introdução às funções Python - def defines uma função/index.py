"""
  Introdução às funções (def) em Python
  Funções são trechos de código usados para 
  replicar determinada ação ao longo do seu código.
  Elas podem receber valores para parâmetros (argumentos) 
  e retornar um valor específico.
  Por padrão, funções Python retornam None (nada).

"""

def Imprimir():
  print('Executado dentro da função 1')
  print('Executado dentro da função 2')
  print('Executado dentro da função 3')
  print('Executado dentro da função 4')

Imprimir()

def Imrprimir_2():
  return 'teste'

print(Imrprimir_2())
print(Imrprimir_2())
print(Imrprimir_2())
print(Imrprimir_2())
print(Imrprimir_2())

print()

def Imprimir_3(a, b, c):
  print(f'{a = }')
  print(f'{b = }')
  print(f'{c = }')

parametro_a = 'Uma coisa'
parametro_b = 'Outra coisa'
parametro_c = 'Ainda outra coisa'

Imprimir_3(parametro_a, parametro_b, parametro_c)
Imprimir_3('A', 'B', 'C')

def saudacao(nome=''): # só pra lembrar, str vazia conta como False assim como Int 0
  if nome:
    print(f'Olá! {nome}!')
  else:
    print('Nenhum nome informado')

print()
saudacao('Felipe')
saudacao('Isis')
saudacao('Giulia')
saudacao()
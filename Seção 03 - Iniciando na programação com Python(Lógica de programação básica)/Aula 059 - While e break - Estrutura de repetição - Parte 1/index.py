"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

"""

condicao = True
integer = 0
while condicao:
  integer = integer + 1
  print(integer)
  if integer > 10:
    condicao = False

while True:
  nome = input('Qual seu nome? ')  
  print(f'Seu nome é {nome}')
  if nome.lower() == 'sair':
    break
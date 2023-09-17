"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_digitado = input('Digite um numero inteiro: ')

try:
  numero_digitado = int(numero_digitado)
  if (numero_digitado % 2 == 0):
    print(f'O número "{numero_digitado}" é um número par')
  else:
    print(f'O número "{numero_digitado}" é um número ímpar')
except:
  print('O número digitado não é um número inteiro válido!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_digitada = input('Digite a hora(apenas a hora, sem os minutos): ')

try:
  hora_digitada = int(hora_digitada)
  if (hora_digitada > 24) or (hora_digitada < 0):
    input('Hora digitada fora do período válido de 24h')
  else:
    if (hora_digitada >= 0) and (hora_digitada <= 11):
      print('Bom dia!')
    elif (hora_digitada >= 12) and (hora_digitada <= 17):
      print('Boa tarde!')
    else:
      print('Boa noite!')
except:
  print('O número digitado não é uma hora válida!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_digitado = input('Qual seu primeiro nome? ')
tamanho_nome = len(nome_digitado)
nome_curto = (tamanho_nome <= 4)
nome_normal = (tamanho_nome >= 5) and (tamanho_nome <= 6)

if nome_curto:
  print('Seu nome é curto')
elif nome_normal:
  print('Seu nome é normal')
else:
  print('Seu nome é muito grande')
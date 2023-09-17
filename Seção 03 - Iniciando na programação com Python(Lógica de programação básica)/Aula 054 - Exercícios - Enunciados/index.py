"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_digitado = input('Digite um numero inteiro: ')

try:
  numero_digitado = int(numero_digitado) # dava pra ter usadoo numero_digitado.isdigit() e resolver com IF ao invés de TRY
  if (numero_digitado % 2 == 0):
    print(f'O número "{numero_digitado}" é um número par')
  else:
    print(f'O número "{numero_digitado}" é um número ímpar')
except:
  print('O número digitado não é um número inteiro válido!')

"""
Solução professor


# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

"""
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
Solução professor

entrada = input('Digite a hora em números inteiros: ')

try:
  hora = int(entrada)

  if hora >= 0 and hora <= 11:
    print('Bom dia')
  elif hora >= 12 and hora <= 17:
    print('Bom tarde')
  elif hora >= 18 and hora <= 23:
    print('Bom noite')
  else:
    print('Não conheço essa hora')
except:
  print('Por favor, digite apenas números inteiros')
"""
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

"""
Solução do professor

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
  if tamanho_nome <= 4:
    print('Seu nome é curto')
  elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
  else:
    print('Seu nome é muito grande')
else:
  print('Digite mais de uma letra.')
"""
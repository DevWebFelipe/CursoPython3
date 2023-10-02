# Exercício - sistema de perguntas e respostas

import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

indice_pergunta = 0

def get_pergunta(indice):
  return perguntas[indice]['Pergunta']

def get_resposta_opcoes(indice):
  opcoes = ''

  for valor in perguntas[indice]['Opções']:
    opcoes += ', ' + valor

  return 'Resposta : ' + opcoes[2:] + ' = '


def get_opcoes(indice):
  return perguntas[indice]['Opções']

def get_resposta(indice):
  return perguntas[indice]['Resposta']

def continuar():
  return (input('Deseja continuar? [S] [N] ').lower() == 's')

def acabou_as_perguntas():
  return len(perguntas) - 1 == indice_pergunta

while True:
  finalizar = False
  os.system('cls')
  
  print(get_pergunta(indice_pergunta))
  print()

  while True:
    resposta = input(get_resposta_opcoes(indice_pergunta))
    print()

    if resposta not in get_opcoes(indice_pergunta):
      print(f'{resposta = } não é uma das opções disponíveis, tente novamente!')

      continue
    elif resposta == get_resposta(indice_pergunta):
      print('Parabéns, você acertou')
      print()
      
      if acabou_as_perguntas():
        finalizar = True
        break
      else: 
        finalizar = not continuar()
        break
    else:
      print('Que pena, você errou, mas tente novamente')
      continue
  
  if finalizar:
    break

  indice_pergunta += 1
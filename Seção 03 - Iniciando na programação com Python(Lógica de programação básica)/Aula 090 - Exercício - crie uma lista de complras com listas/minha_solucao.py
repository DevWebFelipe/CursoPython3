"""
  Faça uma lista de compras com listas
  Ousuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
  Não permita que o programa quebre com erros de índices inexistentes na lista

"""

import os

lista_compras = []

while True:
  print('O que deseja fazer?')
  opcao = input('[i]nserir [a]pagar [l]istar [f]inalizar ').lower()
  print()

  if opcao == 'l':
    if len(lista_compras) == 0:
      os.system('cls')

      print('Lista de compras vazia')
      print()

      continue
    else:
      os.system('cls')

      for indice_item, nome_item in enumerate(lista_compras):
        print(f'{indice_item} - {nome_item}')

      print()
      continue
  elif opcao == 'f':
    if len(lista_compras) == 0:
      print('A lista de compras está vazia')
      confirmacao = input('Deseja realmente finalizar? [s]im [n]ão ').lower()

      if confirmacao == 's':
        os.system('cls')
        break
      else:
        os.system('cls')
        continue
    else:
      os.system('cls')

      for indice_item, nome_item in enumerate(lista_compras):
        print(f'{indice_item} - {nome_item}')

      print()
      break
  elif opcao == 'i':
    adicionar_item = input('Qual item deseja adicionar? ').lower()
    lista_compras.append(adicionar_item)

    os.system('cls')

    continue
  elif opcao == 'a':
    os.system('cls')

    for indice_item, nome_item in enumerate(lista_compras):
      print(f'{indice_item} - {nome_item}')

    print()
    apagar_item = input('Digite o número do item que deseja apagar: ')
    try:
      item_apagado = lista_compras.pop(int(apagar_item))
      os.system('cls')

      print(f'Item apagado: {item_apagado}')
      print()

      continue
    except:
      os.system('cls')

      print('item não encontrado')
      print()

      continue
  else:
    os.system('cls')

    print('Não consegui encontrar um comando correspondente')
    print()

    continue

print('Lista de compras finalizada')
"""
  Operadores de comparação (relacionais)
  OP     Significado      Exemplo(True)   Exemplo(False)
  >      Maior            5 > 2           2 > 5
  >=     Maior ou igual   5 >= 5          2 >= 5
  <      Menor            2 < 5           5 < 2
  <=     Menor ou igual   2 <= 5          5 <= 2
  ==     Igual            'a' == 'a'      'a' == 'b'
  !=     Diferente        'a' != 'b'      'b' != 'b'

"""

"""
  SHELL INTERATIVO: Comando python -i ...localizar caminho do arquivo que vai ser executado
  Aí basta digitar variável por variável que será dado o resultado dela, sem precisar colocar
  vários print()
  PS: Caso seja alterado algo no arquivo, precisa sair e entrar de novo no SHELL ou importar 
  o módulo de novo

  PS: Comando sair = quit() ou exit()

"""

maior = 5 > 2
maior_ou_igual = 5 >= 5
menor = 2 < 5
menor_ou_igual = 2 <= 5
igual = 'a' == 'a'
diferente = 'a' != 'b'

print(f'{maior=}')
print(f'{maior_ou_igual=}')
print(f'{menor=}')
print(f'{menor_ou_igual=}')
print(f'{igual=}')
print(f'{diferente=}')
print()

maior = 2 > 5
maior_ou_igual = 2 >= 5
menor = 5 < 2
menor_ou_igual = 5 <= 2
igual = 'a' == 'b'
diferente = 'b' != 'b'

print(f'{maior=}')
print(f'{maior_ou_igual=}')
print(f'{menor=}')
print(f'{menor_ou_igual=}')
print(f'{igual=}')
print(f'{diferente=}')
print()

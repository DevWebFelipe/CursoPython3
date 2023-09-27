"""
  Escopo de funções em Python
  Escopo significa o local onde aquele código pode atingir.
  Existe o escopo global e local.
  O escopo global é o escopo onde todo o código é alcançavel.
  O escopo local é o escopo onde apenas nomes do mesmo local
  podem ser alcançados.

"""

variavel_externa = 'Fora da função'
varivel_nome_repetido = 'Fora da função'
variavel_nome_repetido_global = 'Começou fora da função'

def escopo():
  varivel_nome_repetido = 'Dentro da função'
  global variavel_nome_repetido_global
  variavel_nome_repetido_global = 'Editou dentro da função'
  # se aqui dentro eu declarar uma variavel com mesmo nome de uma variavel fora do escopo, a função vai respeitar a variável que estiver dentro do escopo
  def outra_funcao():
    global variavel_nome_repetido_global
    variavel_nome_repetido_global = 'Editou de novo dentro de outra função'
    variavel_interna_funcao_interna = 'Função dentro de outra função'
    varivel_nome_repetido = 'Função dentro de outra função'
    print(f'{variavel_interna=}')
    print(f'{variavel_interna_funcao_interna=}')
    print(f'{varivel_nome_repetido=}')
    print(f'{variavel_nome_repetido_global=}')

  variavel_interna = 'Dentro da função'
  print(f'{variavel_nome_repetido_global=}')
  print(f'{variavel_interna=}')
  print(f'{variavel_externa=}')
  print(f'{variavel_antes_chamada_funcao=}')
  print(f'{varivel_nome_repetido=}')
  print()

  outra_funcao() # a função dentro de outra função, a de nivel mais interno acessa as variaveis da função de nivel mais externo, porém o inverso não acontece

# a variável externa tem sempre que ser definida em cima da chamada da função

variavel_nome_repetido_global = 'Saiu das funções'
variavel_antes_chamada_funcao = 'Fora da função, depois da função e antes da chamada da função'
escopo()
print()
print(f'{varivel_nome_repetido =}')
print(f'{variavel_nome_repetido_global=}')
"""
  Operadores de atribuição
  =    Atribui o valor simples
  +=   Atribui o valor + valor já atribuído
  -=   Atribui o valor - valor já atribuído
  *=   Atribui o valor * valor já atribuído, cuidar com 1 x 1
  /=   Atribui o valor / valor já atribuído, retorna fracionado
  //=  Atribui o valor / valor já atribuído, retorna sempre inteiro
  **=  Atribui o valor elevado ao quadrado, cuidar com 1, que pode dar loop infinito
  %=   Atribui o módulo do próprio número

  Todos esses exemplos, fiz com WHILE, mas porque estava na aula de While, pode ser feito
  com qualquer coisa, alguns, nem fazia sentido fazer com WHILE, como o de módulo por
  exemplo, mas só queria deixar registrado

"""

atribuicao_simples = 0
atribuicao_adicao = 0
atribuicao_subtracao = 10
atribuicao_multiplicacao = 1 # CUIDADO! não pode começar por 0, porque vai dar sempre zero e pode dar loop infinito
atribuicao_multiplicacao_dupla = 2 # CUIDADO! tem que começar por 2, porque eleva ao quadrado, pode dar loop infinito
atribuicao_divisao = 50 # CUIDADO! dependendo do valor, pode dar uma fração gigante e estourar a memória do PC
atribuicao_divisao_dupla = 50 # Vai sempre arredondaro para inteiro
atribuicao_modulo = 20 # resto

while atribuicao_simples < 10:
  string = str(atribuicao_simples)
  
  atribuicao_simples = atribuicao_simples + 1
  print(f'{atribuicao_simples = }') # posso colocar espaços no =(que vai trazer o nome da variável mais o valor) pra formatar melhor

  string = string + '1'
  print(f'{string = }')

print()
while atribuicao_adicao < 10:
  string = str(atribuicao_adicao)
  atribuicao_adicao += 1
  
  print(f'{atribuicao_adicao = }')
  string += '1'
  
  print(f'{string = }')

print()
while atribuicao_subtracao > 0:
  atribuicao_subtracao -= 1
  print(f'{atribuicao_subtracao = }') # Com esse não da de tratar String

print()
while atribuicao_multiplicacao < 20:
  string = atribuicao_multiplicacao
  
  atribuicao_multiplicacao *= 2
  print(f'{atribuicao_multiplicacao = }')
  
  string *= '1'
  print(f'{string = }')

print()
while atribuicao_multiplicacao_dupla < 100:
  atribuicao_multiplicacao_dupla **= 2
  print(f'{atribuicao_multiplicacao_dupla = }') # Com esse não da de tratar String

print()
while atribuicao_divisao > 1:
  atribuicao_divisao /= 5
  print(f'{atribuicao_divisao = }') # Com esse não da de tratar String

print()
while atribuicao_divisao_dupla > 1:
  atribuicao_divisao_dupla //= 5
  print(f'{atribuicao_divisao_dupla = }') # Com esse não da de tratar String

print()
while atribuicao_modulo > 1:
  atribuicao_modulo %= 2
  print(f'{atribuicao_modulo = }') # Com esse não da de tratar String
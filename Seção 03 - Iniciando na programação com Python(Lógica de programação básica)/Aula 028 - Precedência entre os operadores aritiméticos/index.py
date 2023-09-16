""" 
  Regras matemáticas

  1º - (n + n)     Parêntesis (de dentro para fora)
  2º - **          Expoentes
  3º - * / // %    Multiplicações e Divisões (da esquerda para a direita)
  4º - + -         Somas e Subtrações (da esquerda para a direita)

"""

#       1 +   1    + 5
conta = 1 + 1 ** 5 + 5     # 7 - vai calcular de acordo com as regras matemáticas
print('Conta 1:', conta)

#          2    **   10
conta = (1 + 1) ** (5 + 5) # 1024 - vai somar 1 + 1, depois 5 + 5 depois elevará 2 a 10 potência
print('Conta 2:', conta)

#       (1 +      1     ) **   10
conta = (1 + (0.7 + 0.3)) ** (5 + 5) # 1024 - vai somar 0.7 + 0.3, depois 1 + 1, depois 5 + 5 depois elevará 2 a 10 potência
print('Conta 3:', conta) # como usei ponto flutuante no 0.7 e 0.3 o resultado será dado em ponto flutuante

#       (1 +         1     ) **   10
conta = (1 + int(0.7 + 0.3)) ** (5 + 5) # 1024 - vai somar 0.7 + 0.3, depois 1 + 1, depois 5 + 5 depois elevará 2 a 10 potência
print('Conta 4:', conta) # usei ponto flutuante, mas converti para inteiro, então o resultado será dado em inteiro

#       1 +    1    + 5
conta = 1 + (1 ** 5 + 5)   # 7 - vai calcular de acordo com as regras matemáticas o que está em parêntese, depois somará 1 no final
print('Conta 5:', conta)

#        1 +   1     + 5  
conta = (1 + 1 ** 5) + 5   # 7 - vai calcular de acordo com as regras matemáticas o que está em parêntese, depois somará 1 no final
print('Conta 6:', conta)

#       1 +    1     + 5
conta = 1 + (1 ** 5) + 5   # 7 - vai elevar 1 na 5 potência, depois somar 1 e o 5
print('Conta 7:', conta)

#       1 + (     1      ** 5) + 5
conta = 1 + ((0.5 + 0.5) ** 5) + 5   # 7 - vai somar 0.5 + 0.5, depois elevar 1 na 5 potência, depois somar 1 e o 5
print('Conta 8:', conta) # como usei ponto flutuante no 0.5, o resultado será em ponto flutuante
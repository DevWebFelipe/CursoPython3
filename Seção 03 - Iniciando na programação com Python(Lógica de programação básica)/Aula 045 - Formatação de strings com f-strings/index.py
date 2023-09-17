"""
  Formatação básica de strings
  s - string
  d - int
  f - float
  .<número de dígitos>f
  x ou X - Hexadecimal
  (Caractere)(><^)(quantidade)
  > - Esquerda
  < - Direita
  ^ - Centro
  = - Força o número a aparecer antes dos zeros
  Sinal - + ou -
  Ex.: 0>-100,.1f
  Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # essa função é um LPAD, preenche no lado esquerdo com a quantidade de caracteres que mandar
print(f'{variavel:_<10}') # aqui vai preencher no lado direito, não é todos os caracteres que da certo
print(f'{variavel:-^10}') # aqui nas laterais, mantendo a variável no centro
print(f'{1000000.32131313:,.2f}') # formata o numero com ponto e virgula
print(f'{1000000.32131313:+,.2f}') # o + ali, é pra aparecer + se positivo, e - se negativo
print(f'{-1000000.32131313:+,.2f}') # o + ali, é pra aparecer + se positivo, e - se negativo
print(f'{-1000000.32131313:,.2f}') # - se negativo, sempre vai mostrar 
print(f'{10000.321321:.1f}') # formata o numero apenas com ponto
print(f'{10000.321321:0>+10.1f}') # preenche com zeros a esquerda até completar 10 caracteres
print(f'{10000.321321:0=+10.1f}') # preenche com zeros a esquerda até completar 10 caracteres
print(f'{10000.321321:0<10.1f}') # preenche com zeros a direita até completar 10 caracteres
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')
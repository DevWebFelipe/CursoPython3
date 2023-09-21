frase = ('O Python é uma linguagem de programação'\
         'multiparadigma. '\
         'Python foi criado por Guido van Rossum' )# .lower # jogando tudo pra minusculo

print(frase)
print(frase.lower().count('python')) # conta quantas vezes uma determinada string apareceu dentro de outra string

i = 0
maior_quantidade = 0
letra_mais_apareceu = ''

while i < len(frase):
  letra_atual = frase[i]

  if letra_atual == ' ':
    i += 1
    continue

  vezes_letra_apareceu = frase.count(letra_atual)
  
  if maior_quantidade < vezes_letra_apareceu:
    maior_quantidade = vezes_letra_apareceu 
    letra_mais_apareceu = letra_atual 

  i += 1

  
print('Letra que mais apareceu: '
  f'"{letra_mais_apareceu}" {maior_quantidade} vezes'  
)
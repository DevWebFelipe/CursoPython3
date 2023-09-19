"""
  https://docs.python.org/pt-br/3/library/stdtypes.html
  Imutáveis que vimos: str, int, float, bool

"""

# o que é tipo built-in(imutáveis)? são tipos imbutidos, no caso, tipos que já vem dentro do python
# não é preciso instalar, configurar nada, eles já vem com o python
# tipos imutáveis: STR, INT, FLOAT, BOOL

string = 'Felipe Texeira'
outra_variavel = f'{string[:3]}ABC{string[4:]}' # 'Fel'

# string[3] = 'ABC' # em um array, até daria certo, mas não com dados imutáveis, nesse caso, string
print(string[3])
print(outra_variavel)
print(string)

print(string[2:].capitalize()) # Retorna a string com a primeira letra maiúscula e as demais minúsculas
print(string.upper()) # Retorna tudo maiúsculo
print(string.lower()) # Retorna tudo minúsculas
print(string.count('e')) # Conta a quantidade de um determinado caractere
print(string.find('li')) # Retorna a posição onde uma determinada string se encontra
print(string.replace('e', 'E')) # Troca uma string por outra
print(string.zfill(20)) # Preenche com zeros a esquerda
print(string.split(' ')) # Quebra no caracter passado e trnasforma em um array, igual o SplitString do Delphi


# Existem muitos métodos, da pra procurar na documentação
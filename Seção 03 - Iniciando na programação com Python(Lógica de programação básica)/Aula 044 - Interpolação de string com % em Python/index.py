"""
  Interpolação básica de strings
  's' - string
  'd' e 'i' - int
  'f' - float
  'x' e 'X' = Hexadecimal (ABCDEF0123456789)

"""

nome = 'Felipe'
preco = 1000.95897643

# a Interpolação vai vir aqui, no final da string, adiciona-se um percent
# depois passa-se as variáveis que irão subistituir os % dentro da STRING
# Importa: vai ser substituído na ordem que foi colocado dentro da STRING
# Pode-se formatar um valor FLOAT para definir como o valor de ser mostrado
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco) # Só precisa do parênteses, se tiver mais de uma variável
# %s -> no lugar do nome, foi usado 'S' por ser a letra do tipo de valor, no caso, STRING, basta ver a tabela lá em cima
# %f -> no lugar do valor, foi usado 'F' por ser a letra do tipo de valor, no caso, FLOAT, basta ver a tabela lá em cima

print(variavel)
print(40*'-')

# Hexadecimal
# aqui temos um exempo de inteiro que é representado pela letra d
# tempos também um exemplo para completar com zeros á esquerda tipo o LPAD do firebird
# coloco o 0 e a quantidade de casas que quero que ele complete
# x -> Transforma em um hexadecimal minusculo
# X -> Transforma em um hexadecimal maiusculo
print('O hexadecimal de %d é %06x' % (15, 15))
print('O hexadecimal de %d é %08X' % (35, 35))
print(40*'-')
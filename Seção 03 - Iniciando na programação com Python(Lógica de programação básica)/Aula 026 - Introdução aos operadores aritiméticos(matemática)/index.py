adicao = 15 + 20
print('Adição:', adicao)

subtracao = 5 - 19
print('Subtração:', subtracao)

multiplicacao = 3 * 9
print('Multiplicação:', multiplicacao)

divisao = 11 / 3.5 # traz a divisão completa
print('Divisão:', divisao)

divisao_inteira = 11 // 3.5 # pode trazer como ponto flutuante, mas sempre vai truncar
print('Divisão inteira:', divisao_inteira)

divisao_inteira = 11 // 3 # vai trazer como inteiro, mas vai truncar o valor flutuante, retorna sempre apenas o inteiro
print('Divisão inteira:', divisao_inteira)

exponenciacao = 4 ** 3 # 4 * 4 * 4 =  64
print('Exponenciação:', exponenciacao)

modulo = 11 % 4 # resto da divisão, no delphi é o mod, divide enquanto puder dividir, retorna o que não for divisível
# 11 / 4 = 2 e sobra 3 que não é divisível por 4
print('Módulo:', modulo)

valor_1 = 10
valor_2 = 7
print('Valor 1 é divisível por valor 2?', ((valor_1 % valor_2) == 0))
print('Valor 1 é par?', (((valor_1 % 2) ) == 0))
print('Valor 2 é impar?', (((valor_2 % 2) ) == 0))

valor_3 = 10
valor_4 = 2
print('Valor 3 é divisível por valor 4?', ((valor_3 % valor_4) == 0))
print('Valor 3 é par?', (((valor_3 % 2) ) == 0))
print('Valor 4 é impar?', (((valor_4 % 2) ) == 0))
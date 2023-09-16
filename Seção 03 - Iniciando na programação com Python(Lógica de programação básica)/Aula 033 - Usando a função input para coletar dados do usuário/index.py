nome_usuario = input('Qual seu nome? ')
print(f'O nome digitado foi: {nome_usuario}')

valor1 = input('Digite o valor 1: ')
valor2 = input('Digite o valor 2: ')

# o correto seria validar o valor digitado antes de fazer o cálculo
soma_valor1_valor2 = float(valor1) + float(valor2)

print(f'A soma dos valores digitados é: {valor1 + valor2}') # vai concatenar porque é str
print(f'A soma dos valores digitados é: {soma_valor1_valor2}') # com o casting feito, agora vai somar

# caso queira pegar o valor da variável e também o nome da variável, basta usar o sinal de =
print(f'A soma dos valores digitados é: {soma_valor1_valor2=}')
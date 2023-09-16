# variáveis são usadas para salvar algo na memória do computador
# PEP8: inicie variáveis com letras maiúsculas, pode usar números e underline
# o sinal de = é o separador de atribuição. Ele é usado para atribuir
# um valor a um nome(variável)
# Uso: nome_variavel = expressão

nome_completo = 'Felipe Texeira'
print(nome_completo)

var_int = bool('') # isso aqui não se deve fazer, variáveis tem que ter nome sujestivo, e receber um valor que condiza com sua finalidade
print(var_int)

idade = 30
maior_idade = idade >= 18
print(maior_idade)

valor_1 = 5
valor_2 = 10
soma_valor1_valor2 = valor_1 + valor_2
print('Resultado soma', soma_valor1_valor2, sep=': ')
print(valor_2 + valor_1)
print(valor_2 / valor_1)
print(valor_2 - valor_1)
print(valor_2 * valor_1)

print('Nome:', nome_completo, 'Idade:', idade)
print('É maior de idade?', maior_idade)
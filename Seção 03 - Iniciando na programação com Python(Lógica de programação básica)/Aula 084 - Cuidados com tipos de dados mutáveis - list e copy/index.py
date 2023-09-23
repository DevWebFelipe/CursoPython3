"""
  Cuidados com dados mutáveis
  = - copiado o valor (imutáveis)
  = - aponta para o mesmo valor na memória (mutável)

"""

nome = 'Felipe'
noutra_variavel = nome
nome = 'Giulia'

print(nome)
print(noutra_variavel)
print()

lista_a = ['Felipe', 'Giulia', 1, True, 1.5]
lista_b = lista_a # As duas variáveis estão apontando para o mesmo endereço de memória, ou seja a mesma lista, é igual no Delphi
lista_c = lista_a.copy() # agora sim estou trabalhando com duas listas, incialmente a lista_c será igual a lista_a, mas a partir daqui, as duas serão independentes

lista_a[0] = 'Isis'
print(f'{lista_b = }')

print(f'{lista_c = }')
lista_c.append('novo valor')
print(f'{lista_c = }')
print(f'{lista_a = }')
print(f'{lista_b = }')
# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista1 = ['Felipe', 'Giulia', 'Isis']
lista2 = ['Felipe', 'Giulia', 1, 2, 3, 'Isis']
tupla = 'Python', 'é', 'Legal'

a, b, c = lista1
print(lista1)

primeiro, segundo, *_, ultimo = lista2
print(primeiro, segundo, ultimo)

primeiro, segundo, *_, penultimo, ultimo = lista2
print(primeiro, segundo, penultimo, ultimo)

for nome in lista2:
  print(nome, end=' ')

print()
print()
print(['Felipe', 'Giulia', 1, 2, 3, 'Isis'])
print('Felipe', 'Giulia', 1, 2, 3, 'Isis')
print(*lista2)
print(*tupla)


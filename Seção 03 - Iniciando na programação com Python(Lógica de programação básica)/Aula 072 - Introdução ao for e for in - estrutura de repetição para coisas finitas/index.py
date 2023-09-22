""" Exemplo com for """

texto = 'Python'

for letra in texto:
  print(letra)

print()

novo_texto = ''
for letra in texto:
  novo_texto += f'*{letra}'

print(novo_texto[1:]) # ta pegando só do caractere indice 1 pra frente
print()
""" Exemplo com while """

texto = 'Felipe'
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
  print(texto[i], i)
  i += 1

print()
""" Exemplo professor """

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
  senha_digitada = input(f'Sua senha ({repeticoes} x): ')

  repeticoes += 1

print('Aquele laço acima pode ter repetições infinitas')
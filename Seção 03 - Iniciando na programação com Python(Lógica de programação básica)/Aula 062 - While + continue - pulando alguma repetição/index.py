contador = 0
contador_1 = 0

while contador < 10:
  contador += 1
  contador_1 = 0

  if contador % 2 == 0: # números pares, não vai mostrar
    continue # não executa o resto do código, volta pro inicio do laço, igual no Delphi

  while contador_1 <= 5:
    contador_1 += 1

    if contador == 5:
      print(f'{contador} dentro do 2º laço')
      break

    if contador_1 == 3:
      break

    if contador_1 % 2 != 0: # diferente de 0
      continue

    print(f'{contador_1 = } dentro do while secundário')

  if contador == 3:
    continue # não vai mostrar o 3

  print(contador)

  if contador == 4:
    break # termina imediatamente o laço, igual no Delphi

print()
print('Acabou o laço')
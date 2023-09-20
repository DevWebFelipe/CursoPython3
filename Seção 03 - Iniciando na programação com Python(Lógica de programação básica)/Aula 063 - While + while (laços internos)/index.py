qtd_linhas = 5
qtd_colunas = 5

linha = 1
# esse eu fiz
while linha <= qtd_linhas:
  coluna = 1
  coluna_string = ''

  while coluna <= qtd_colunas:
    coluna_string += f'{coluna = } '
    coluna +=1

  print(f'{linha = } {coluna_string}')
  linha += 1

print()

qtd_linhas = 5
qtd_colunas = 5
linha = 1
# exemplo professor
while linha <= qtd_linhas:
  coluna = 1

  while coluna <= qtd_colunas:
    print(f'{coluna = } {coluna = }')
    coluna +=1

  linha += 1

print()
print('Saiu do laço')
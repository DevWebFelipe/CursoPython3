"""
  split e join com list e str
  split - divide uma string (list)
  join - une uma string

"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split() # sem passar nada, quebra nos espaços
print(lista_palavras)

nomes = '  Felipe   ,   Giulia   ,   Isis  '
lista_nomes_st = nomes.split(',')
print(type(lista_nomes_st), ' -> ', lista_nomes_st) # vai quebrar nas virgulas, é igual o SplitString do delphi
lista_nomes_ct = []

print()
print('Entrou do for')
print()
for i, nome in enumerate(lista_nomes_st):
  print('|' + lista_nomes_st[i] + '|') 
  print('|' + lista_nomes_st[i].strip() + '|') # remove os espaços no começo e no fim da str igual o Trim do delphi
  print('|' + lista_nomes_st[i].rstrip() + '|') # remove os espaços a direita
  print('|' + lista_nomes_st[i].lstrip() + '|') # remove os espaços a esquerda
  lista_nomes_ct.append(lista_nomes_st[i].strip());

print()
print('Acabou o for')
print()
print('Antes : ', lista_nomes_st)
print('Depois: ', lista_nomes_ct)
print()

separador = ' '
junta_nomes = separador.join(lista_nomes_ct) # Junta 2 strings, pega o separador e a cada posição da lista_nomes_ct adiciona a string do separador
print(type(junta_nomes), ' -> ', junta_nomes)

junta_nomes = ', '.join(lista_nomes_ct) 
print(type(junta_nomes), ' -> ', junta_nomes)
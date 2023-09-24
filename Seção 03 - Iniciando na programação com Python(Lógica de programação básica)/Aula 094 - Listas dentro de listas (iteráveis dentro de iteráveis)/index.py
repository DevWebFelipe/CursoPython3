salas = [
#   0         1        2
  ['Lista1', 'Nome1', 'Nome2'], # 0
#   0         1
  ['Lista2', 'Nome1', ['outra', 'lista']], # 1
#   0         1        2        3
  ['Lista3', 'Nome1', 'Nome2', 'Nome3'], # 2
#   0         1        2
  ('Tuple1', 'Nome1', 'Nome2'), # 3
  'item sem lista' # 4
]

print(salas)
print(salas[1])
print(salas[0])
print(salas[2])
print(salas[0][0])
print(salas[1][0])
print(salas[1][2])
print(salas[1][2][0])
print(salas[2][0])
print()
print()

print('Iterando sobre uma lista com outras listas') # fiz só pra praticar

for lista_nv1 in salas:
  if type(lista_nv1) == list:
    for lista_nv2 in lista_nv1:
      if type(lista_nv2) == list:
        for lista_nv3 in lista_nv2:
          print(f'     {lista_nv3 = }')
      else:
        print(f'   {lista_nv2 = }')
  elif type(lista_nv1) == tuple:
    for tuple_nv1 in lista_nv1:
      print(f'   {tuple_nv1 = }')
  else:
    print(f' {lista_nv1 = }')
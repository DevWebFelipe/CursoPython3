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

print()
print(salas)
print()
print(*salas)
print()
print(*salas, end='\n')
print()
print(*salas, sep='\n')
print()
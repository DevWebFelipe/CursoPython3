"""
  Flag(Bandeira) - Marca um local
  None = não valor
  is e is not = é ou não é(tipo, valor, identidade)
  id = identidade

"""

condicao = True
passou_no_if = None # Valor nenhum

if condicao:
  passou_no_if = True
  print('Faça algo')
else:
  print('Não faça algo')

if passou_no_if is None:
  print('Não passou no if')

if passou_no_if is not None:
  print('Passou no if')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

print(30 * '-')

condicao = False
passou_no_if = None # Valor nenhum

if condicao:
  passou_no_if = True
  print('Faça algo')
else:
  print('Não faça algo')

if passou_no_if is None:
  print('Não passou no if')

if passou_no_if is not None:
  print('Passou no if')
  
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)


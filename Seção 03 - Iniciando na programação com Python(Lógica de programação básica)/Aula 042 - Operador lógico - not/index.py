"""
  Operador lógico "not"
  usado para inverter expressões
  not True = False
  not False = True

"""

string = input('Senha: ')

# é igual usar (not edtTeste.Text.Trim.IsEmpty) do delphi
if not string:
  print('Não existe valor')
else:
  print('Existe valor')
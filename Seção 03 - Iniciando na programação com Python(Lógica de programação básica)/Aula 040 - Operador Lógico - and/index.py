"""
  Operadores lógicos
  and (e) or (ou) not (não)
  and - Todas as condições precisam ser verdadeiras
  se qualeur valor for considerado falso, a expressão inteira 
  será avaliada naquele valor
  São considerados falsy (que já vimos):

  0 -> Zero (int)
  0.0 -> Zero (float)
  '' -> Vazio (string)
  False -> Falso (boolean)

  Também existe o tipó None que é usado para representar um não valor

"""

entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
  print('Entrar')
else:  
  print('Sair')

print()
print(True and True)
print(True and True and 1)
print(True and True and bool(0))
print(True and bool('') and 0)

import importlib # essa lib permite que o mesmo módulo seja importado mais de uma vez

#      PASTA   MODULO ALIAS APELIDO
import modulos.modulo as    modulo # dessa maneira, por padrão, o modulo será importado apenas uma vez em todo projeto

from modulos import modulo
from modulos.modulo import * 
from modulos.modulo import variavel

print(modulo.variavel)
print()
print(variavel)
print()
print(modulo.soma(5,17))
print()

for i in range(10):
    print(i)
    import modulos.modulo # enquanto singleton, vai importar uma unica vez em todo o sistema

print()

for i in range(10):
    print(i)
    importlib.reload(modulos.modulo) # dessa forma, posso reimportar/recarregar o modulo

print('Fim')
print()

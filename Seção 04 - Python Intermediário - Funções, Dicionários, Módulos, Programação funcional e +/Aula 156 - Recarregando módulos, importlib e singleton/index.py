
import importlib # essa lib permite que o mesmo módulo seja importado mais de uma vez

import modulo # dessa maneira, por padrão, o modulo será importado apenas uma vez em todo projeto

print(modulo.variavel)
print()

for i in range(10):
    print(i)
    import modulo # enquanto singleton, vai importar uma unica vez em todo o sistema

print()

for i in range(10):
    print(i)
    importlib.reload(modulo) # dessa forma, posso reimportar/recarregar o modulo

print('Fim')
print()
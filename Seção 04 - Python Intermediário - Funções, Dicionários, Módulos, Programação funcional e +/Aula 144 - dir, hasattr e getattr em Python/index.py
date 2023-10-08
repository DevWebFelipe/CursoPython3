# dir, hasattr e getattr em Python

# dir -> Lista todos os métodos de alguma coisa

import pprint

string = 'Felipe'
lista_metodo = ['upper', 'errado']

print(pprint.pprint(dir(string))) # -> Listou todos os métodos da variável STRING
print()
print(pprint.pprint(hasattr(string, 'upper'))) # -> Verifica se existe o método UPPER na minha variável
print()
print(pprint.pprint(getattr(string, lista_metodo[0]))) # -> Busca um determinado atributo
print()

for metodo in lista_metodo:
    if hasattr(string, metodo):
        print('Existe um método UPPER dentro da variável STRING')
        print(getattr(string, metodo)())
    else:
        print('Método chamado, não existe na variável STRING')

print()
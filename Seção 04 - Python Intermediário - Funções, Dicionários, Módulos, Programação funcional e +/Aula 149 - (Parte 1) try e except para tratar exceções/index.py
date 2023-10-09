# Try, except, else e finally

try:
    ...
finally:
    ...

try:
    ...
except:
    ...

a = 18
b = 0
# c = a / b

try:
#    a = 18
#    b = 0
    print('Até aqui tudo bem')

    c = a / b[0]

    print('Divisão feita com sucesso')
except ZeroDivisionError:
    print('Erro ao dividir por zero')
except NameError:
    print('Variável não definida')
except (TypeError, IndexError):
    print('Tipo de varável errado ou indice acessado incorretamente')
except Exception:
    print('Erro não tratado')

print()
print()
print('Executou todo o código')
print()
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
except ZeroDivisionError as e:
    print(e)
    print(e.__class__.__name__)
except NameError:
    print('Variável não definida')
except (TypeError, IndexError) as error: # Melhor dividir em duas, mas vamos fazer uma pra ficar de exemplo
    print('ERROR:', error)
    print('NOME:', error.__class__.__name__)
except Exception:
    print('Erro não tratado')

print()
print()
print('Executou todo o código')
print()
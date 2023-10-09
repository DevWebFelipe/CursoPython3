try:
    ...
finally:
    ...

try:
    ...
except:
    ...

#######################################################################################
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
#######################################################################################

try:
    print('Dentro do Try')
finally:
    print('Dentro do Finally') # é igual o delphi, não vi nada de diferente nas ultimas aulas que trataram de try, mas to seguindo o curso e registrando os a exemplos

print()

# ISSO É DIFERENTE, NO DELPHI NÃO DA DE USAR TRY -> EXECPT -> FINALLY (nunca vi pelo menos)
# TERIA QUE USAR DOIS BLOCOS, TRY FINALLY E DENTRO DELE UM TRY EXCEPT

try:
    print('Abrir um arquivo qualquer')
    print()
    
    #8/0
    
    print('Executou todo o processo corretamente')
    print()
except ZeroDivisionError as e:
    print('Divisão por zero não é permitida')
    print(f'{e.__class__.__name__} : {e}')
    print()
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else: # isso aqui também é novo, mas com o finally, não consegui aidna entender uma situação em que seria necessário o else
    print('O código rodou sem erros')
    print()
finally:
    print('Fechar o arquivo que tentou abrir')
    print()

# TRY FINNALY -> Não da de tratar erro e o que tiver no bloco do FINALLY sempre vai rodar
# TRY EXCEPT -> Da pra tratar erro, podese usar vários EXCEPT para tratar diferentes tipos de errop
# TRY EXCEPT ELSE -> Trata o erro e caso não ocorra erro roda o que tiver no ELSE
# TRY EXCEPT FINNALY -> Trata o erro e roda o que tiver no FINALLY
# TRY EXCEPT ELSE FINALLY -> Trata o erro, roda o que tiver no ELSE caso não de erro e roda o que tiver no FINALLY
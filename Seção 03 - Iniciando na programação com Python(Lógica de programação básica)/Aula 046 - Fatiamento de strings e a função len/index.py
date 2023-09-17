"""
  Fatiamento de strings
  012345678
  Olá mundo
 -987654321
  Fatiamento [i:f:p] [::]
  Obs.: a função len retorna a qtd 
  de caracteres da str

"""#                  0123
#           01234567891111 
variavel = 'Felipe Texeira'
print(variavel[4:9]) # tem que cuidar com a posição final, pporque ela não é cluída
# nesse caso, vai pegar da posição 4 até a posição 8, não inclui a posição 9
# de resto, é o quase igual a função COPY do delphi
# caso queira pegar até a ultima posição, no caso, o resto todo da string, basta não 
# indicar uma posição final
print(variavel[4:])
print(variavel[:6])
print(variavel[0:6])
print(len(variavel[4:])) # LEN conta a quantidae de caracteres igual o LENGTH do delphi
print(len(variavel[:6]))
print(len(variavel[0:6]))

print(variavel[0:len(variavel):1]) # esse ultimo 'parametro' determina de quantos em quantos
# vai pular na hora de pegar os carateres
print(variavel[0:len(variavel):2]) # aqui no caso, só vai pegar os caracteres de posição 
# par porque ta pegando de 2 em 2
print(variavel[0:len(variavel):3])
print(variavel[::-1]) # Nesse caso, vai inverter a string, porque ta pegando todos os caracteres
# porém na posição negativa, ou seja, de trás pra frente
print(variavel[-9::-1]) # aqui, inverti só o primeiro nome
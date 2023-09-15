"""
  Python = Linguagem de programação
  Tipo de tipagem = Dinâmica/Forte
  str -> string -> texto
  Strings são textos que estão dentro de aspas
"""

print(1234)

# Aspas simples (aqui posso usar aspas duplas dentro do argumento como parte da minha string)
print('Felipe Texeira')
print('Felipe "Texeira"')

# Aspas duplas (aqui posso usar aspas simples dentro do argumento como parte da minha string)
print("Felipe"" Texeira")
print("Felipe Texeira")
print("Felipe 'Texeira'")

# Os dois abaixo normalmente nunca serão usados
# Escape (serve para que as aspas não quebre a string, uma vez que elas são os delimitadores de um argumento do tipo string)
print("Felipe \"Texeira\"")

# r (serve para mostrar as barras(escapes))
print(r"Felipe \"Texeira\"")
print('Explícito', 'é', 'melhor " do que implícito')

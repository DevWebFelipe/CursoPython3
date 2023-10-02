import index

pessoa = index.pessoa

# POPITEM -> Igual o POP porém, deleta a última chave do dicionário, o retorno também muda em relação ao POP, pois aqui, o retorno será uma tupla que vai conter chave e valor da chave que fora deletada

print(pessoa)
print()

ultima_chave = pessoa.popitem()
print(ultima_chave)

print()
print(pessoa)
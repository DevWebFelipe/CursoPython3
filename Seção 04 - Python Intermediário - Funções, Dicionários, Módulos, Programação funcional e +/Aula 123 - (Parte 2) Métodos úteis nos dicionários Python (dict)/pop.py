import index

pessoa = index.pessoa

# POP -> Apaga uma chave, tipo o DEL, mas tem uma coisa a mais, ele retorna o valor da chave que foi deletada

print(pessoa)
print()

nome = pessoa.pop('nome')
print(nome)

print()
print(pessoa)
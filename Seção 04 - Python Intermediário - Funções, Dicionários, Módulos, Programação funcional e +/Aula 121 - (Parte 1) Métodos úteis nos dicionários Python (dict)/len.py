import index

pessoa = index.pessoa

# LEN -> Vai retornar a quantidade de chaves que tem dentro do dicionário
# Métodos que tem __NomeMetodo__ são chamados de Dunder, nesse caso DunderLen

print(f'{len(pessoa) = }') # Normalmente, se usa dessa forma, mas as duas funcionam
print(f'{pessoa.__len__() = }')
print()
# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(f'{s1 = }')
print(f'{s2 = }')
print()
print(f'{s1 | s2 = } -> "|" une sem repetir')
print()
print(f'{s1 & s2 = } -> "&" mostra só o que existe nos 2')
print()
print(f'{s1 - s2 = } -> "-" apenas o que existe no SET da esquerda e não existe no SET da direita')
print()
print(f'{s1 ^ s2 = } -> "^" apenas os itens que estão apenas em um ou outro')
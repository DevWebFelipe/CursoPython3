# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Felipe') # ADD string, adiciona a string inteira
s1.add('Giulia')
s1.update('Isis') # UPDATE string, itera sobre a string, adicionando cada indice separadamente
s1.update(('Isis',)) # UPDATE string, para não iterar, tem que passar como tupla, lembrando que sempre tem que ter pelo menos 1 virgula, então caso tenha só um indice, vai ficar sobrando 1 virgula
print(s1)

s1.clear()
print()
print(s1)

s1.add(1)
s1.add('Felipe')
s1.update(('Isis', 1, 3, 'Felipe', 3, 5, 6, 8))
print(s1)
print()

s1.discard(1)
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
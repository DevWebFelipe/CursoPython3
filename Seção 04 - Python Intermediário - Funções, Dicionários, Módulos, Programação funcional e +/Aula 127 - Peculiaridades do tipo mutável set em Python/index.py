# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Felipe')

# são parecidos com dicionários, porém não tem par com chave e valor, eles possuem apenas o valor

#s1 = set()  # vazio
#s1 = {'Felipe', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

valores_repetidos = {1, 1, 2, 2, 2, 3, 4, 5, 5}
print(valores_repetidos)
print()

l1 = [1, 1, 2, 2, 2, 3, 4, 5, 5]
print(l1)
print()

s1 = set(l1)
print(s1)
print()

l2 = list(s1)
print(l2)
print()

# SET não garante ordem, ou seja, pode ser que as coisas fiquem em uma ordem diferente da que você quer, tem que ficar atento a isso

s2 = set('Felipe')
print(s2)
print('F' in s2)
print('f' in s2)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy)

dic_1 = {
  'chave1': '1',
  'chave2': '2',
  'chave_l1': ['l1', 'l2'],
}

dic_2 = dic_1 # Isso aqui não faz cópia, só diz que ambas as variáveis estão apontando para o mesmo endereço na memória, então se eu alterar algo no DICIONARIO_1 altera também no DICIONARIO_2

print(f'{dic_1 = }')
print(f'{dic_2 = }')
print()

dic_1['chave1'] = 'dic_1'
dic_2['chave2'] = 'dic_2'

print(f'{dic_1 = }')
print(f'{dic_2 = }')
print()

dic_3 = dic_1.copy() # Isso é chamada cópia rasa, agora, o dic_1 não afetará dic_3 e dic_3 não afeta dic_1, mas essa cópia, só compia os valores imutáveis, ou seja, se tiver uma lista dentro do dicionário ou outro dicionário, isso não vai ser copiado, vai continular linkado no dicionário base

print(f'{dic_1 = }')
print(f'{dic_2 = }')
print(f'{dic_3 = }')
print()

dic_1['chave2'] = 'dic_1'
dic_2['chave1'] = 'dic_2'
dic_1['chave_l1'][0] = 'dic_1'
dic_3['chave1'] = 'dic_3'
dic_3['chave2'] = 'dic_3'

print(f'{dic_1 = }')
print(f'{dic_2 = }')
print(f'{dic_3 = }')
print()


import copy

dic_4 = copy.deepcopy(dic_1) # Para uma cópia completa, é necessário importar o módulo copy e fazer uma DEEP COPY, aí será copiado todos os valores mutáveis e imutáveis

print(f'{dic_1 = }')
print(f'{dic_2 = }')
print(f'{dic_3 = }')
print()

dic_1['chave2'] = 'dic_1'
dic_2['chave1'] = 'dic_2'
dic_1['chave_l1'][0] = 'dic_1'
dic_4['chave1'] = 'dic_4'
dic_4['chave2'] = 'dic_4'
dic_4['chave_l1'][0] = 'dic_4'

print(f'{dic_1 = }')
print(f'{dic_2 = }')
print(f'{dic_3 = }')
print(f'{dic_4 = }')
print()
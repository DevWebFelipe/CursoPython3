# Métodos úteis dos dicionários em Python
# len        - quantas chaves
# keys       - iterável com as chaves
# values     - iterável com os valores
# items      - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy       - retorna uma cópia rasa (shallow copy)
# get        - obtém uma chave
# pop        - Apaga um item com a chave especificada (del)
# popitem    - Apaga o último item adicionado
# update     - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Texeira',
    'idade': 25,
    'idade': 27,
    'idade': 28, # Chaves iguais não vai dar erro, mas só vai exibir o valor da ultima chave, é como se estivesse sobrepondo o valor das chaves anteriores
    'altura': 1.75,
}
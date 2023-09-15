# recebe um argumento, ou mais de um se separado por virgula, e imprime na  tela
# ctrl + c vai copiar a linha toda se não tiver nada selecionado, ctrl + v vai colar a linha copiada
# aqui estamos usando argumentos não nomeados
print(12, 34, '55')
print('teste')
print('5' + '5')
print(5 + 5)
print(12, 34, 'teste', 5 + 5, '5' + '5')

# aqui vamos usar um argumento nomeado, que seria um separador diferente do padrão, que é espaço
print(12, 34, '55', sep=";")
print(12, 34, '55', sep='-')

# aqui, vamos usar um argumento nomeado, que seria o end, vai adicionar o que eu quiser no final dos argumentos
# detalhe, para manter a quera de linha, precisa conter \n (em windows mais antigos, precisa ser \r\n)
print(12, 34, '55', end=" concatenou ")
print(12, 34, '55', end=' concatenou ')
print(12, 34, '55', end='\r\n quebrou antes ')
print(12, 34, '55', end=" concatenou ")
print(12, 34, '55', end=" quebrou depois \n")
print(12, 34, '55', end=" concatenou")
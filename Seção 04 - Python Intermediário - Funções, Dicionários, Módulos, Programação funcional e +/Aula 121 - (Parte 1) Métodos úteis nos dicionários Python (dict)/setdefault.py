import index

pessoa = index.pessoa

# SETDEFAULT -> Bastante parecido com GET, pois vai retornar um valor 'PADRÃO' caso não encontre a chave buscada, porém, ele cria a chave dentro do dicionário caso ela não exista, o GET não faz isso, o valor que vai setar como default, só vai ser usado se a chave que foi passada não existir, do contrário, vai usar o valor que já está no dicionário para a chave informada

print(pessoa)
pessoa.setdefault('idade', 'Não vai fazer nada, pois a chave já existe')
pessoa.setdefault('sexo', 'Não informado')
print(pessoa)
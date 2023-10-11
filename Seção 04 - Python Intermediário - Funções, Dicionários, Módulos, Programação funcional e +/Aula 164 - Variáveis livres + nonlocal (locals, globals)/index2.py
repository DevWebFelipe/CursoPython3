
# não tem relação com essa aula, mas vou deixar os dois aqui, no segundo, estou 'formatando' a impressão, quebrando a lista e 
# separando cada item com quebra de linha
print(globals())
print()
print(*globals(), sep='\n')
print()


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_contatenar):
        nonlocal valor_final # dessa forma, to dizendo que não quero a variavel VALOR_FINAL de dentro desse escopo, então vai pegar a do escopo acima, nesse caso, a do escopo da função CONCATENAR, dessa forma, a cada chamada do método, irá concatenar o que já tinha anteiormente com o que está sendo passado agora, isspo porque a função vai ficar 'lembrando' qual o ultimo valor da variável
        valor_final += valor_a_contatenar

        return valor_final

    return interna

c = concatenar('a -> ')
print(c('A'))
print(c('B'))
print(c('C'))
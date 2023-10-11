
# Exercício - Adiando execução de funções
def soma(x, y): # a declaração da função é chamado de assinatura da função
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def decorar_funcao(y): # aqui eu to salvando em memória a funçaõ que estou recebendo
        return funcao(x, y)
    
    return decorar_funcao # aí eu retorno a função que eu savei, não a execução dela


soma_com_cinco = criar_funcao(soma, 5) # aqui eu passo o valor de Y, que está sendo salvo na memória na função dentro do escopo
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(7)) # aqui estou passando o valor de x e executando a função que retorna de CRIAR_FUNCAO, onde o y já está salvo na memória
print()
print(multiplica_por_dez(10))
print()
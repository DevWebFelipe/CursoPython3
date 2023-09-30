"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia') # aqui salvou a primeira função, nela foi salvo BOM DIA como valor da variável SAUDACAO
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Felipe', 'Giulia', 'Isis']:
    print(falar_bom_dia(nome)) # aqui, é a função interna que está no return da função externa, então o valor que to passando, é para o parametro da função interna NOME
    print(falar_boa_noite(nome)) # como já estava salvo o SAUDACAO lá em cima qunado salvei na variável FALAR_BOA_NOITE, agora vai executar a função interna
    # tendo como valor do parametro SAUDACAO o BOA NOITE e o valor do parametro NOME sendo o indice do array
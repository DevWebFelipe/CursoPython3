# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

######### essa é a função decoradora, ela decora/armazena uma outra função, para ser executada 'mais tarde'
# a finalidade dela, é receber uma função, criar uma função interna para que eu tenha uma CLOSURE ali dentro
# e essa função interna não será executada até que eu peça para ela ser executada, ela será retornada sem 
# execução
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Decorou a função')
        for arg in args:
            is_string(arg)

        # posso ter código antes
        resultado = func(*args, **kwargs)
        # posso ter código depois
        print('Função decorada')
        return resultado
    
    return interna
#########

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str): # aqui to vendo se o tipo do param é texto(str)
        raise TypeError('parâmetro deve ser do tipo TEXTO') # caso não seja, vou criar um erro para parar

inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida = inverte_string_checando_parametro('Felipe')
print(invertida)
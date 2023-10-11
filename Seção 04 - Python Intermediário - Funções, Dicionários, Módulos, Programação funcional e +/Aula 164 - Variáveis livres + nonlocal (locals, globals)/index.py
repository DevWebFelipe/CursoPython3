# Variáveis livres + nonlocal

def fora(x):
    a=x
    def dentro():
        print(locals()) # mostra as variáveis acessíveis localmente
        print()
        print(dentro.__code__.co_freevars) # mostra as variáveis livres
        print()

        return a # A é uma variavel livre, porque ela não está definida dentro do escopo da 
                 # função DENTRO, então, no caso, na função DENTRO, a variável A é uma variável livre

    return dentro

dentro1 = fora(20)
dentro2 = fora(10)

print(dentro1())
#print(dentro2())
# Posso determinar o que vai estar disponivel na iumportação de tudo

import outro_modulo

__all__ = [
    'variavel',
]

print('Arquivo MODULO.PY importado/atualizado')
variavel = 'Var do arquivo MODULO.PY'

def soma(x, y):
    return x + y

print(outro_modulo.de_onde_vem())
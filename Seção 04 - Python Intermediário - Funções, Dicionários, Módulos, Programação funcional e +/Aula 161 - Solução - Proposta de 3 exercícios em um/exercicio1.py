from util import copiar_tudo, listar_resultado, valor_sobre_percentual, produtos

novos_produtos = copiar_tudo(produtos)

for produto in novos_produtos:
    produto['preco'] += valor_sobre_percentual(produto['preco'], 10)

"""
    SOLUÇÃO DO PROFESSOR: usou list comprehension

    novos_produtos = [
        {**p, 'preco': round(p['preco'] * 1.1, 2)}
        for p in copy.deepcopy(produtos)
    ]

    pritn(*produtos, sep='\n')
    pritn()
    pritn(*novos_produtos, sep='\n')
"""

listar_resultado(novos_produtos, 'Preço alterado')
from util import copiar_tudo, listar_resultado, produtos

novos_produtos = copiar_tudo(produtos)

novos_produtos_ordenados_por_preco = sorted(
    novos_produtos,
    key= lambda p: p['preco'], 
)

"""
    SOLUÇÃO DO PROFESSOR: usou list comprehension

    novos_produtos_ordenados_por_preco = sorted(
        copy.deepcopy(novos_produtos),
        key= lambda p: p['preco'], 
    )

    pritn(*produtos, sep='\n')
    pritn()
    pritn(*novos_produtos_ordenados_por_preco, sep='\n')
"""

listar_resultado(novos_produtos_ordenados_por_preco, 'Ordenado por preço')
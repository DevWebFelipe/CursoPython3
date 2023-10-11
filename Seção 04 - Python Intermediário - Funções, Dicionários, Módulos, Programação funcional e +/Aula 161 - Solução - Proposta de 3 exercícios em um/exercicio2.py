from util import copiar_tudo, listar_resultado, produtos

novos_produtos = copiar_tudo(produtos)

novos_produtos_ordenados_por_nome = sorted(
    novos_produtos,
    key= lambda p: p['nome'], 
    reverse=True
)

"""
    SOLUÇÃO DO PROFESSOR: usou list comprehension

    novos_produtos_ordenados_por_nome = sorted(
        copy.deepcopy(novos_produtos),
        key= lambda p: p['nome'], 
        reverse=True
    )

    pritn(*produtos, sep='\n')
    pritn()
    pritn(*novos_produtos_ordenados_por_nome, sep='\n')
"""

listar_resultado(novos_produtos_ordenados_por_nome, 'Ordenado por nome')
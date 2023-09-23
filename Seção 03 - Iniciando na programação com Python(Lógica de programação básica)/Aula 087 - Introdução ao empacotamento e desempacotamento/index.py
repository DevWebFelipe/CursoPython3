lista_nomes = ['Felipe', 'Giulia', 'Isis']
nome1, nome2, nome3 = lista_nomes

nome1_sv, nome2_sv, nome3_sv = ['Felipe', 'Giulia', 'Isis']

print(nome1, nome2, nome3)
print(nome1_sv, nome2_sv, nome3_sv)


nome1_r, *resto = lista_nomes # por convenção, se eu usar *_ estarei dizendo que a variável com o restante da lista existe, mas que não será usada
print(nome1_r, resto)

_, nome1, *_ = lista_nomes # estou ignorando o primeiro item, pegando o segundo e o restante dizendo que não será usado
print(nome1, _)

_, _, nome1 = lista_nomes
print(nome1)
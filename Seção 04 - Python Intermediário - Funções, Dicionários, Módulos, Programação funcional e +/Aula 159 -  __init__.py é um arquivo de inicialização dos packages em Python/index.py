# https://stackoverflow.com/questions/2386714/why-is-import-bad

import pprint

import package
from package import monta_dados_nfe as monta_nfe

print(package.dobrar_valor(5))
print()

pprint.pprint(monta_nfe([50, 20]))
print()

print(package.mudei_nome_f2_modulo_1)
print()
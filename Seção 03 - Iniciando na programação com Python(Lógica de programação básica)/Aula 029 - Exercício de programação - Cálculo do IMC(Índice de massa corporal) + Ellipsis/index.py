nome = 'Felipe Texeira'
altura = 1.75
peso = 133
imc = peso / (altura ** 2) # não precisaria do parentese por conta da precedencia, mas acho mais organizado e visualmente mais fácil de identificar como o calculo está sendo feito

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu IMC é:')
print(imc)
print()

altura = 1.80
peso = 95
imc = peso / (altura ** 2)
print('Dados do professor para conferência da fórmula')
print('Altura', altura, 'Peso', peso, sep=' = ') # to colocando sep só pra ir memorizando, mas fica ruim, porque fica com = no meio do valor da altura e da descrição 'Peso'
print(imc)
print()

print('Abaixo está o ELLIPSIS')
print('Se você vai colocar um código aqui, mas ainda não pensou em como fazer isso, pode usar ... no meio do código, não irá gerar nenhum erro (existem outras finalidades)')
print(...)
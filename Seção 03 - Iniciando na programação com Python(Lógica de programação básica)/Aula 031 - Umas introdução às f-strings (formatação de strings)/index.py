var1 = 123
var2 = 56.56
var3 = '"TESTE"'

# como eu quero usar variáveis dentro do texto que estou montando abaixo
# uso o f no começo da sentença, esse f vai habilitar o uso de varáveis dentro do 
# texto, tendo habilitado o uso delas, basta que eu as envolva em chaves
linha_1 = f'{var1} é um valor inteiro. {var2} é um valor float. {var3} é um valor string'

print(linha_1)
print()
print()

# habilitando as variáveis, envolvendo-as em chaves, agora tem-se a possibilidade
# de adicionar opções de formação desses valores, abaixo, vou colocar dois valores
# um formatado para mostrar duas casas decimais, outro sem essa formatação
# para formatar casas decimais, adicono . + quantidade de casas decimais + f
# essa formatação irá ARREDONDAR o valor formatado, não TRUNCAR
# para adicionar qualquer tipo de formatação eu adiciono :
valor_flutuante = 33.3667

"f-strings"
print(f'Com formatação: {valor_flutuante:.2f}') # irá ARREDONDAR
print(f'Com formatação: {valor_flutuante:.6f}') # estou formatando com mais casas decimais do que 
# realmente tem, nesse caso, irá aidionar zeros a direita
print(f'Sem formatação: {valor_flutuante}')

print()
print()

# caso queira fazer uma conversão para reais por exemplo, adicionado vírgula do decimal e ponto do milhar
valor_real = 90000000.5559
print(f'Com formatação (,): {valor_real:,.2f}')
print(f'Com formatação: {valor_real:.2f}')
print(f'Sem formatação: {valor_real}')
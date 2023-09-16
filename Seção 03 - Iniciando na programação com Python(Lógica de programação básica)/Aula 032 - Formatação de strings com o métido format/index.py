a = 'A'
b = 'B'
c = 1.1

# nesse caso, o format está funcionando como um array, a cada chave que eu chamar
# será colocado o valor do argumento com índice correspondente (mas também posso pegar pelo índice
# nesse caso, vai funcionar como qualquer índice, começando por 0, aí a ordem não importa) 
# IMPORTANTE: ou coloca índice em todas as chaves, ou não coloca em nenhuma
# é possível formatar o valor mostrado, usa-se a mesma sintaxe utilizada com f-strings (aula 031)
# a quantidade de chaves não pode exceder a quantidade de argumentos no format
string_nomral = 'a = {0}, b = {0}, c = {2:.2f}, d = {3:.2f}'
string_nomral2 = 'a = {}, b = {}, c = {:.2f}, d = {:.2f}'
string_nomral_nomeado = 'a = {0}, b = {1}, c = {nome3:.2f}, d = {nome4:.2f}'

formato = string_nomral.format(a, b, c, float('23.5'))
formato2 = string_nomral2.format(a, b, c, int('55'))
# depois de nomeado um argumento, todos os que vierem depois dele, deverão ser nomeados
formato_nomeado = string_nomral_nomeado.format(
  a, 
  str(55.6) + ' str', 
  nome3=float(15.8), 
  nome4=int('28')
)

print(formato)
print()
print(formato2)
print()
print(formato_nomeado)

# parametro nomeado (é quando é dado nome para os argumentos passados na chamada do método)
#  Conversão de tipos, coerção
#  type convertion, typecasting, coercion
#  é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
#  str, int, float, bool
print(5 + 10)
print('5' + '10')
print('1', type('1'))
print(str(5) + '5') # é possível converter um int ou float para str para concatenar
print(str(5) + '5.5') # é possível converter um int ou float para str para concatenar
print(int('1'), type(int('1'))) # convertendo str para int e averiguando se o tipo ficou como int corretamente
print(float('5') + 10.5) # convertendo str para float
print(float('5.5') + int('10')) # diferente do delphi, aqui pode-se calcular int com float
print(float(5)) # é possível transformar um int em float
print(int(5.6)) # é possível trnasformar um float em int, ele vai truncar o valor
# print(int('5.6')) mas não é possível transformar um str com ponto flutuante em int
print(int(float('5.9'))) # é possível transformar um str com ponto flutuante em float, depois transformar em int
print(bool('')) # converte uma string para boolean, como está vazia retorna FALSE
print(bool(' ')) # converte uma string para boolean, como não está vazia retorna TRUE
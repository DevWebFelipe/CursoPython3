# if / elif      / else
# se / se não se / então

# blocos de códigos aninhados precisam seguir a mesma identação, 
# no caso seria uma identação própria, cada um com o seu, mas o 
# que tiver dentro do mesmo bloco de código precisa respeitar a 
# identação do próprio bloco
condicao1 = True
condicao2 = True
condicao3 = False
condicao4 = False

if condicao1 and condicao4:
  print('Código para condição 1 e condição 4')
  if condicao2:
    print('Código para condição 2 dentro da condição 1')
  else:
    print('Condicação 2 dentro da condição 1 não atendida')  
elif (condicao1 and (not condicao3)):
  print('Condicão 1 atendida mas condicão 3 não atendida')
elif ((not condicao4) and (not condicao2)):
  ...   # ELLIPSIS, não quero fazer nada agora, depois vejo o que colocar aqui
else:
  print('Nenhuma condição foi satisfeita')

if condicao1 and condicao2:
  print('Condicaçõo 1 e 2 atendidas')

print('Isso ta fora do IF')
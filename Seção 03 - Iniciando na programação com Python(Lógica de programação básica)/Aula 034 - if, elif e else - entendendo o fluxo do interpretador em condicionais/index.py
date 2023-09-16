# if / elif      / else
# se / se não se / então

entrada = input('Você quer "entrar" ou "sair"? ')

# vai ser aberto o if, ao invés de usar o THEN como no delphi, usa-se :
# o bloco de código que vai ser executado, vem na próxima linha, seguido de um TAB
# ou um espaço já basta, o ponto, é que não pode estar colado a esquerda
# estranhamente, não precisa de begin end nem nada, pode ser confuso entender onde 
# começa e onde termina kkkkk
if (entrada == 'entrar'):  
   print('Você entrou no sistema')
   print('Entrou no sistema, agora use ele')  
elif (entrada == 'sair'):
  print('Você saiu do sistema')
else:
  print('Nenhuma opção foi selecionado') 

print('vai passar por aqui sempre')
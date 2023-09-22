"""
  Faça um jogo para o usuário adivinhar qual a palavra secreta.
  - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
  - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
  - Se a letra digitada estiver na palavra secreta; exiba a letra;
  - Se a letra digitada não estiver na palavra secreta; exiba *.
  
  Faça a contagem de tentativas do seu usuário.

"""

""" Minha solução """

frase_secreta = 'Eu amo voce'
frase_secreta_minuscula = frase_secreta.lower() 
frase_secreta_oculta = len(frase_secreta) * '*'
letras_ja_digitadas = ''
numero_tentativas = 0

print(f'Frase secreta: {frase_secreta_oculta}')

while True:
  print()
  letra_digitada = input('Digite uma letra: ').lower()
  
  if letras_ja_digitadas.find(letra_digitada) >= 0:
    print('Você já digitou essa letra')
    continue

  letras_ja_digitadas += letra_digitada

  if len(letra_digitada) > 1:
    print('Sem trapaças! Digite apenas 1 letra')
    continue

  numero_tentativas += 1

  nova_frase_secreta_oculta = ''
  if frase_secreta_minuscula.find(letra_digitada) >= 0:
    for indice_letra in range(len(frase_secreta_minuscula)):
      if frase_secreta_minuscula[indice_letra] == letra_digitada:
        nova_frase_secreta_oculta += frase_secreta_minuscula[indice_letra]
      else:
        if frase_secreta_minuscula[indice_letra] in frase_secreta_oculta:
          nova_frase_secreta_oculta += frase_secreta_minuscula[indice_letra]
        else:
          nova_frase_secreta_oculta += '*'
  else:
    print(f'Que pena, a frase secreta não contém a letra "{letra_digitada}"')
    continue
        
  frase_secreta_oculta = nova_frase_secreta_oculta
  print(f'Frase secreta: {frase_secreta_oculta}')

  if frase_secreta_oculta.find('*') < 0:
    break

  if (input('Você já sabe qual é a frase secreta? [S] [N]: ').lower()[0] == 's'):
    completar_frase = input('Qual a frase secreta? ').lower()
    if completar_frase == frase_secreta_minuscula:
      break
    else:
      print('Que pena, essa não é a frase secreta, continue tentando!')

print()
print('Parabéns!')
print(f'Você completou a frase secreta em {numero_tentativas} tentativas!')
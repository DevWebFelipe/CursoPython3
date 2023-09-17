"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade_carro = 50  # velocidade atual do carro
local_carro_km = 99  # local em que o carro está na estrada

VELOCIDADE_MAXIMA_RADAR = 60  # velocidade máxima do radar 1
LOCAL_KM = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade_carro > VELOCIDADE_MAXIMA_RADAR:
  print('Velocidade do carro acima do limite permitido para a pista') 

if local_carro_km >= (LOCAL_KM - RADAR_RANGE) and  \
   local_carro_km <= (LOCAL_KM - RADAR_RANGE) and \
   velocidade_carro > VELOCIDADE_MAXIMA_RADAR: # No python, pra quebrar a linha no meio de um código, tem que colocar uma barra invertida
  print('Carro multado em RADAR 1') 

# acima tem um exemplo básico do que precisaria para funcionar, agora vamos refatorar
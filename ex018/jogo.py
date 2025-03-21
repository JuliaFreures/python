import getpass
import random
EMPATE = 0
VIT_JOGADOR1 = 1
VIT_JOGADOR2 = 2

ESCOLHAS_VALIDAS = ['pedra', 'papel', 'tesoura']

def pre_processar_resposta(escolha):
    return escolha.lower().strip()

def solicitar_escolhas(num_jogadores):
    escolhas = []
    for i in range(1, num_jogadores + 1):
        escolha = getpass.getpass(f"Jogador{i} - escolha 'pedra', 'papel' ou 'tesoura':")
        escolhas.append(pre_processar_resposta(escolha))
        if len(escolhas) > 2:
              escolhas.append(random.choice)
    return escolhas

def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
            return EMPATE
    elif ((jogador1 == 'pedra' and jogador2 == 'tesoura') or 
          (jogador1 == 'tesoura' and jogador2 == 'papel')or
          (jogador1 == 'papel' and jogador2 == 'pedra')):
            return VIT_JOGADOR1
    else:
            return VIT_JOGADOR2

num_jogadores = int(input("Quantos jogadores (1 ou 2):"))

escolhas = solicitar_escolhas(num_jogadores)
resultado = jokenpo(escolhas[0], escolhas[1])
print("\n---------")
for i, escolha in  enumerate (escolhas):
      print(f"Jogador {i+1}: {escolha}")
print("\nResultado:")
      
if resultado == EMPATE:
      print ("Empate")
elif resultado == VIT_JOGADOR1:
      print("Jogador 1 venceu!")
else:
      print("Jogador 2 venceu!")
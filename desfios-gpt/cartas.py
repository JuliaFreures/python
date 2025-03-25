import random

# Criando o baralho com 40 cartas (sem 8, 9 e 10)
naipes = ["♠", "♥", "♦", "♣"]
valores = ["A", "2", "3", "4", "5", "6", "7", "J", "Q", "K"]
baralho = [f"{v}{n}" for n in naipes for v in valores]
random.shuffle(baralho)  # Embaralha o baralho

# Distribuir 9 cartas para cada jogador
jogadores = {"Jogador 1": [], "Jogador 2": []}
for _ in range(9):
    for jogador in jogadores:
        jogadores[jogador].append(baralho.pop())

# Criar monte e pilha de descarte
monte = baralho
descarte = []

def mostrar_mao(jogador):
    print(f"\nMão de {jogador}: {', '.join(jogadores[jogador])}")

# Loop do jogo
while True:
    for jogador in jogadores:
        mostrar_mao(jogador)

        # Compra uma carta do monte ou do descarte
        if descarte:
            escolha = input(f"{jogador}, deseja comprar do (M)onte ou do (D)escarte? ").strip().lower()
            if escolha == "d":
                carta_comprada = descarte.pop()
            else:
                carta_comprada = monte.pop()
        else:
            carta_comprada = monte.pop()

        jogadores[jogador].append(carta_comprada)
        print(f"{jogador} comprou {carta_comprada}")

        # Jogador escolhe uma carta para descartar
        print(f"Sua mão: {', '.join(jogadores[jogador])}")
        carta_descartada = input("Escolha uma carta para descartar: ").strip()
        
        if carta_descartada in jogadores[jogador]:
            jogadores[jogador].remove(carta_descartada)
            descarte.append(carta_descartada)
            print(f"{jogador} descartou {carta_descartada}")
        else:
            print("Carta inválida! Tente novamente.")

        # TODO: Verificar vitória (precisamos implementar uma função para isso)

        if not monte:
            print("O monte acabou! O jogo empatou!")
            exit()

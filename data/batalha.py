import random
from pokemon import Pokemon, pokemons
from card_game import Selecao

class BatalhaSimples:
    def __init__(self, deck1, deck2, rodadas=3):
        self.deck1 = deck1
        self.deck2 = deck2
        self.rodadas = rodadas

    def calcular_dano(self, atacante, defensor):
        """Calcula o dano causado por um Pokémon ao outro."""
        dano = max(0, atacante.ataque - defensor.defesa)  # Garante que o dano mínimo seja 0
        return dano

    def batalhar(self):
        pontos1 = 0
        pontos2 = 0

        for i in range(self.rodadas):
            p1 = self.deck1[i]
            p2 = self.deck2[i]

            print(f"\n🔸 Rodada {i+1}:")
            print(f"Jogador 1 - {p1.nome} (ATK: {p1.ataque} / DEF: {p1.defesa})")
            print(f"Jogador 2 - {p2.nome} (ATK: {p2.ataque} / DEF: {p2.defesa})")

            dano1 = self.calcular_dano(p1, p2)
            dano2 = self.calcular_dano(p2, p1)

            print(f"⚔️ {p1.nome} causou {dano1} de dano em {p2.nome}.")
            print(f"⚔️ {p2.nome} causou {dano2} de dano em {p1.nome}.")

            if dano1 > dano2:
                pontos1 += 1
                print("✅ Jogador 1 venceu a rodada!")
            elif dano2 > dano1:
                pontos2 += 1
                print("✅ Jogador 2 venceu a rodada!")
            else:
                print("🤝 Empate na rodada!")

        self.exibir_resultado(pontos1, pontos2)

    def exibir_resultado(self, pontos1, pontos2):
        """Exibe o resultado final da batalha."""
        print("\n🏁 Resultado Final:")
        if pontos1 > pontos2:
            print("🏆 Jogador 1 venceu a batalha!")
        elif pontos2 > pontos1:
            print("🏆 Jogador 2 venceu a batalha!")
        else:
            print("🤝 A batalha terminou em empate!")
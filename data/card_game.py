from pokemon import Pokemon, pokemons

class Selecao:
    def __init__(self):
        self.pokemons = pokemons  # Carrega a lista de pokémons

    def mostrar_todos(self):
        print("🏁 Mostrando TODOS os Pokémons:\n")
        for idx, pokemon in enumerate(self.pokemons, start=1):
            print(f"{idx}.", end=" ")
            pokemon.exibir()
            print("-" * 40)

    def selecionarpokemons(self):
        self.mostrar_todos()
        selecionados = []

        while len(selecionados) < 3:
            try:
                escolha = int(input(f"Escolha 3 Pokémons, numerando-os de 1 a {len(self.pokemons)}: "))
                if escolha < 1 or escolha > len(self.pokemons):
                    print(f"❌ Escolha inválida. Por favor, escolha um número entre 1 e {len(self.pokemons)}.")
                elif escolha in selecionados:
                    print("⚠️ Esse Pokémon já foi escolhido. Por favor, selecione outro.")
                else:
                    selecionados.append(escolha)
                    print(f"✅ Pokémon {self.pokemons[escolha-1].nome} selecionado!")
            except ValueError:
                print("❌ Entrada inválida. Por favor, insira um número válido.")

        print("\n🎉 Pokémons selecionados para batalha:")
        for i in selecionados:
            self.pokemons[i-1].exibir()

        return [self.pokemons[i-1] for i in selecionados]
from card_game import Selecao
from batalha import BatalhaSimples

def selecionar_deck(jogador, selecao):
    """Função para selecionar o deck de um jogador."""
    print(f"\n🎮 {jogador}, selecione seus 3 Pokémons:")
    return selecao.selecionarpokemons()# Função que pede para o jogador escolher 3 Pokémons e retorna a seleção feita pelo método selecionarpokemons() da classe Selecao.

if __name__ == "__main__":
    selecao = Selecao() #Só execute isso se o arquivo for rodado diretamente, e não quando ele for importado como módulo em outro código.

    try:
        while True:
            print("\nEscolha uma opção:")
            print("1. Mostrar todos os Pokémons")
            print("2. Selecionar Pokémons para a Batalha")
            print("3. Sair")

            opcao = input("Digite a opção desejada:").strip()#O .strip() é um método de string no Python que remove os espaços em branco (e quebras de linha) do começo e do fim de uma string.

            if opcao == "1":
                selecao.mostrar_todos()

            elif opcao == "2":
                print("\n🎮 Jogador 1, selecione seus 3 Pokémons:")
                deck1 = selecionar_deck("Jogador 1", selecao)
                deck2 = selecionar_deck("Jogador 2", selecao)

                iniciar = input("\n⚔️ Deseja iniciar a batalha agora? (s/n): ").lower().strip()

                if iniciar == "s":
                    batalha_final = BatalhaSimples(deck1, deck2)
                    batalha_final.batalhar()
                else:
                    print("🔙 Voltando ao menu...")

            elif opcao == "3":
                print("👋 Valeu por jogar! Até mais.")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")
    except KeyboardInterrupt:
        print("\n👋 Programa encerrado pelo usuário. Até mais!")
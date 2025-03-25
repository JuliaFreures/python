import random
numero = random.randint(1, 100)

chute = 0
tentativas = 0
while chute != numero:
    try: 
        chute = int(input("Adivinhe o valor (entre 1 e 100):"))
        if chute < 1 or chute > 100:
            print("O valor deve ser entre 0 e 100, Tente novamente.")
            continue
        tentativas = tentativas + 1
        if chute == numero:
            print(f"Parabéns, Você acertou em {tentativas} tentativas")
            break
        elif chute < numero:
            print("O valor é maior")
        elif chute > numero:
            print("O valor é menor")
    except ValueError:
        print("Por favor, insira um número válido.")
        
        

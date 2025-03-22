import random
numero = random.randint(0, 1000)


while True:
    try:
        chute = int(input("Adivinhe o valor (entre 0 e 1000): "))
        if chute < 0 or chute > 1000:
            print("O valor deve estar entre 0 e 1000. Tente novamente.")
            continue
        break
    except ValueError:
        print("Por favor, insira um número válido.")


while chute != numero:
    print(f" chute = {chute}")  
    
    if chute > numero:
        print("Seu chute é maior que o valor.")
    elif chute < numero:
        print("Seu chute é menor que o valor.")
    
    
    while True:
        try:
            chute = int(input("Adivinhe o valor: "))
            if chute < 0 or chute > 1000:
                print("O valor deve estar entre 0 e 1000. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido.")


print(f"Parabéns, o número era {numero}!")

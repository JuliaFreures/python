import random

numero = random.randint(0, 1000)

chute = int(input("adivinhe o valor (entre 0 e 1000):"))

while chute != numero:
    if chute > numero:
        print("Seu chute é maior que o valor")
    else:
        print("Seu chute é menor que o valor")
    chute = int(input("adivinhe o valor:"))

print(f"Parabens, o numero era {numero}")
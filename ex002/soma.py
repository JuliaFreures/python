num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

operaçao = input("Digite a operação(+,-,*,/):")
if operaçao == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operaçao == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operaçao == "*":
    resultado = num1 *num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operaçao == "/":
    resultado = num1 / num2
    print(f"Resultado: {num1} / {num2} = {resultado}")
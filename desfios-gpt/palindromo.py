palavra = input("Digete uma palavra o frase:")
palavra_limpa = palavra.replace(" ", "").lower()
palavra_invertida = palavra_limpa[::-1]
if palavra_limpa == palavra_invertida:
    print("É um palíndromo")
else: 
    print("Não é um palíndromo")


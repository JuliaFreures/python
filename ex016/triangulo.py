from trianglos import triangulo_valido

a = float(input('Digite um valor de lado:'))
b = float(input('Digite um valor de lado:'))
c = float(input('Digite um valor de lado:'))

if triangulo_valido(a, b, c):
    print(f"{a}, {b} e {c} formam um triangulo VÁLIDO")
else:
     print(f"{a}, {b} e {c} formam um triangulo INVÁLIDO")
           
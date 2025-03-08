#media simples
n1 = float(input("Fale a nota:"))
n2 = float(input("Fale a outra nota:"))
n3 = (n1+n2) / 2
8

print(f'A média simple: {n3}')
#media harmonica
mh = 2 / (1/n1 + 1/n1)
print(f"A media harmonia: {mh}")
#media ponderada
p1 = 2
p2 = 4
print(f"Pesos são:{p1} e {p2}")
mp = (p1 * n1 + p2 * n2) / (p1 + p2)
print(f"Media ponderada: {mp}")

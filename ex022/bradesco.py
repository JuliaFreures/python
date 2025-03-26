
n1 = float(input("Digite sua nota:"))
n2 = float(input("Digite sua nota:"))

print("Nota 1:", n1)
print("Nota 2:", n2)
while n1 and n2 < 11:
 
 media = (n1 + n2) / 2
print("Média:", media)
if media >= 7:
    print("APROVADO")

else:
    print("REPROVADO")

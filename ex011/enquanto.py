nota =  float(input("Digite uma nota:"))
#if nota >= 0 and nota <= 10:
#  print("nota")
#else:
#    print("Nota invalida")
while nota< 0 or nota > 10:
    nota = float(input("Digite um valor VALIDO de nota:"))
    print(nota)

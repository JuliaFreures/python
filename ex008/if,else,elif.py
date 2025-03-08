nota = int(input("NOTA:"))
media_alta = 7
media_baixa = 5

if nota >= media_alta:
    print(f"Aprovado direto!")

elif nota >= media_baixa:
        print(f"Fazer prova final!")
nota_pf = 6
if nota_pf >= media_baixa:
        print(f"Aprovado na prova final")
else:
        print(f"Precisa fazer recuperação final")
        nota_rf = 5
if nota_rf >= media_baixa:
        print(f"Aprovado na recuperação")
else:
        print(f"REPROVADO")

print(f"Fazer recuperação final")
nota_rf = 5
if nota_rf >= media_baixa:
        print(f"Aprovado na recuperação")
else:
        print(f"REPROVADO")





notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM:")
    nota = float(input("nota:"))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
    contador = contador + 1

print("quantidades de notas", len(notas))
for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno,"Tirou nota", nota)
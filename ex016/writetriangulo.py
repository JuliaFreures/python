import trianglos as tri

with open ("data/lados.txt", "r")as arq:
    linhas = arq.readlines()
respostas =[]
for linha in linhas:
      partes =  linha.strip().split()

      for i in range (len(partes)):
          partes[i] = float(partes[i])
      resposta = tri.triangulo_valido(partes[0], partes[1], partes[2])
      
      if resposta:
        respostas.append("Sim")
      else:
        respostas.append("False")
with open("resposta-triangulos.txt", "w")as arq:
    for resp in respostas:
     arq.write(f"{resp}\n")
        
    
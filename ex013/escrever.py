msg = "A nota de matematica foi 9.0"
caminho = "mensagem.txt"

with open ("mensagem.txt", "w") as arquivo:
    arquivo.write(msg)

    #adicionando de forma fake
with open(caminho) as arq:
    conteudo = arq.read()

conteudo = conteudo + "\nA nota de historia foi 9.7"

with open(caminho , 'w') as arq:
    arq.write(conteudo)
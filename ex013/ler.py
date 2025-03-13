
arquivo = open("mensagem.txt", "r")

msg = arquivo.read()

arquivo.close()

print(msg)

caminho = "mensagem.txt"
with open(caminho, "r") as arq:
    m = arq.read()
    print("-------------")
    print(m)
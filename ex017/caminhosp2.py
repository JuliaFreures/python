import os
OUTPUT_DIR = "saidas"
nomearquivo = "mensagem.txt" 

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    
with open (os.path.join(OUTPUT_DIR, nomearquivo), 'w')as arq:
    arq.write("To com fome mundo")
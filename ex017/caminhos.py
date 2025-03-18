import os
DATA_DIR = "data"
print(os.path.abspath(DATA_DIR))

caminhos = os.path.join(os.path.abspath(DATA_DIR), "lado.txt")
print(caminhos)

print(os.listdir("PYTHON"))

modulos_python = []
for nome in os.listdir("PYTHON"):
    if nome.endswith(".py"):
        modulos_python.append(nome)
    print(modulos_python)
os.path.join(os.path.abspath('.'), 'data', 'lados.txt')

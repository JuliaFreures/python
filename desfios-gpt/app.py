from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Acomaf - Acotar',
        'Autor': 'Sarah J. Maas'
    },
    {
        'id': 2,
        'titulo': 'Coroa da meia oite - Trono de vidro',
        'Autor': 'Sarah J. Maas'  
    },
    {
        'id': 3,
        'titulo': 'Cidade da lua crecente - cidade dos ventos ',
        'Autor': 'Sarah J. Maas'
    }
    
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def ober_livro_por_id(id):
    for livro in livros:
        if livro.get ('id')== id:
            return jsonify(livro)


@app.route('/livros', methods=['PUT'])
def editar_livro_por_id(id):
   livro_alterado = request.get_json()
   for indice,livro in enumerate(livros):
       if livro.get('id') == id:
           livros[indice].update(livro_alterado)
           return jsonify(livros[indice])
       
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro():
    for indice, livro in enumerate(livros):
        if livro.get('id')== id:
          del livros[indice]  

    return jsonify(livros)
           

app.run(port=5000,host='localhost',debug=True)
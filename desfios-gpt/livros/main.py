import os
from flask import Flask, request, render_template
import requests

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates") )

@app.route("/")
def home():
    return render_template("index.html", livros=[])  

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("q", "").strip()
    livros = []
    mensagem_erro = None

    if termo:
        if len(termo) < 3:  # Validação para termos muito curtos
            mensagem_erro = "O termo de busca deve ter pelo menos 3 caracteres."
        else:
            url = "https://www.googleapis.com/books/v1/volumes"
            parametros = {"q": termo, "maxResults": 5}
            try:
                resposta = requests.get(url, params=parametros)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    if "items" in dados:
                        livros = [
                            {
                                "titulo": item["volumeInfo"].get("title", "Título desconhecido"),
                                "autor": ", ".join(item["volumeInfo"].get("authors", ["Autor desconhecido"])),
                                "capa": item["volumeInfo"].get("imageLinks", {}).get("thumbnail", ""),
                            }
                            for item in dados["items"]
                        ]
                    else:
                        mensagem_erro = "Nenhum livro encontrado para o termo pesquisado."
                else:
                    mensagem_erro = f"Erro na API: {resposta.status_code} - {resposta.reason}"
            except requests.RequestException as e:
                mensagem_erro = "Erro ao conectar à API. Por favor, tente novamente mais tarde."
                app.logger.error(f"Erro ao conectar à API: {str(e)}")  # Substitui print por logging
    else:
        mensagem_erro = "Por favor, forneça um termo de busca válido."

    if not livros:  # Garante que livros seja uma lista
        livros = []

    app.logger.info(f"Livros encontrados: {livros}")  # Substitui print por logging
    return render_template("index.html", livros=livros, mensagem_erro=mensagem_erro)  

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Erro inesperado: {str(e)}")
    return render_template("index.html", livros=[], mensagem_erro="Ocorreu um erro inesperado. Tente novamente mais tarde."), 500

if __name__ == "__main__":
    # Verifica se o diretório templates existe
    if not os.path.exists(app.template_folder):
        os.makedirs(app.template_folder)
        app.logger.warning(f"Diretório 'templates' criado em: {app.template_folder}")
    app.run(debug=True)  # Certifique-se de desativar o modo debug em produção

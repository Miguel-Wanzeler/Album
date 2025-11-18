import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

app.config["pasta_fotos"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

fotos = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/postar", methods=["POST"])
def upload():
    file = request.files["foto"]
    if file:
        save_path = os.path.join(app.config["pasta_fotos"], file.filename)
        file.save(save_path)
        fotos.append(file.filename)
    return redirect(url_for("galeria"))

@app.route("/galeria")
def galeria():
    # remove fotos que não existem mais
    fotos_existentes = []
    for foto in fotos:
        caminho = os.path.join(app.config["pasta_fotos"], foto)
        if os.path.exists(caminho):
            fotos_existentes.append(foto)

    # atualiza a lista
    fotos.clear()
    fotos.extend(fotos_existentes)

    return render_template("galeria.html", fotos=fotos)

if __name__ == "__main__":
    app.run(debug=True)

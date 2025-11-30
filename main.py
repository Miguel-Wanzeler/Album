import os
from flask import Flask, render_template, request, redirect, url_for
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

# -----------------------------------------------
# CONFIGURAÇÃO DO CLOUDINARY
# -----------------------------------------------
cloudinary.config(
    cloud_name="dz8nukjdv",
    api_key="359541287531737",
    api_secret="osPJd1-AbjUxkeW_ni7G6_UAtpM"
)

# Lista local para armazenar URLs das fotos
fotos = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/postar", methods=["POST"])
def upload():
    file = request.files["foto"]

    if file:
        # Faz upload para o Cloudinary
        resultado = cloudinary.uploader.upload(file)
        
        # Pega a URL pública da imagem
        url = resultado["secure_url"]

        # Salva a URL na lista
        fotos.append(url)

    return redirect(url_for("galeria"))

@app.route("/galeria")
def galeria():
    # Envia para o template as URLs das fotos
    return render_template("galeria.html", fotos=fotos)

if __name__ == "__main__":
    app.run(debug=True)

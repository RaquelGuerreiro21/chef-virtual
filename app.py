from flask import Flask, render_template, request, session, flash
from prompt import gerar_receita
import os

app = Flask(__name__)
app.secret_key = os.getenv("", "chave-secreta-padrao")  # use variável no deploy

MAX_CHAMADAS = 3  # limite por sessão

@app.route("/", methods=["GET", "POST"])
def index():
    receita = None

    # Inicializa contagem de chamadas se não existir
    if "chamadas_api" not in session:
        session["chamadas_api"] = 0

    if request.method == "POST":
        if session["chamadas_api"] >= MAX_CHAMADAS:
            flash("⚠️ Limite de chamadas à API atingido nesta sessão.")
        else:
            ingredientes = request.form["ingredientes"]
            receita = gerar_receita(ingredientes)
            session["chamadas_api"] += 1

    return render_template("index.html", receita=receita)

if __name__ == "__main__":
    app.run(debug=True)

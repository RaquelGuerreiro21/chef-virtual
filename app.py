from flask import Flask, render_template, request
from prompt import gerar_receita

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    receita = None
    if request.method == "POST":
        ingredientes = request.form["ingredientes"]
        receita = gerar_receita(ingredientes)
    return render_template("index.html", receita=receita)

if __name__ == "__main__":
    app.run(debug=True)

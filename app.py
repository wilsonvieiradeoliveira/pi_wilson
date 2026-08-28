from flask import Flask, render_template

app = Flask(__name__)

nome = "Aluno"
idade = 18
email = "aluno@email.com"
youtube = "Youtube_Aluno"
lista_hobbies = ["Jogar bola", "Ouvir música", "Jogar Vídeo Game"]

produtos = [
    {"nome": "Caderno", "preco": 12.50, "estoque": 8},
    {"nome": "Caneta", "preco": 2.00, "estoque": 0},
    {"nome": "Mochila", "preco": 89.90, "estoque": 3},
    {"nome": "Estojo", "preco": 25.90, "estoque": 5},
    {"nome": "Lápis", "preco": 1.50, "estoque": 0},
]


@app.route("/")
def inicio():
    return render_template("index.html", name=nome, idade=idade)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", hobbies=lista_hobbies)


@app.route("/hobbies-vazio")
def hobbies_vazio():
    return render_template("hobbies.html", hobbies=[])


@app.route("/futuro")
def futuro():
    return render_template("futuro.html")


@app.route("/contato")
def contato():
    return render_template(
        "contato.html",
        email=email,
        youtube=youtube,
    )


@app.route("/perfil")
def perfil():
    return render_template("perfil.html", name=nome, idade=idade, curso=None)


@app.route("/perfil/<n>")
def perfil_nome(n):
    return render_template("perfil.html", nome=n, idade=idade, curso="Informática")


@app.route("/aluno/<n>")
def aluno(n):
    return render_template("aluno.html", nome=n)


@app.route("/recado/<n>")
def recado(n):
    return render_template("recado.html", nome=n)


@app.route("/tabuada/<int:n>")
def tabuada(n):
    return render_template("tabuada.html", numero=n)


@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return render_template("soma.html", a=a, b=b)


@app.route("/dobro/<int:n>")
def dobro(n):
    return render_template("dobro.html", n=n)


@app.route("/catalago")
def catalago():
    return render_template("catalago.html", produtos=produtos)


@app.route("/produto")
def produto():
    p = {"nome": "Caderno", "preco": 12.50, "estoque": 0, "marca": "Tilibra"}
    return render_template("produto.html", produto=p)


@app.route("/produto/<int:id>")
def detalhe(id):
    if id < 0 or id >= len(produtos):
        return render_template("detalhe.html", produto=False)
    p = produtos[id]
    return render_template("detalhe.html", produto=p)


if __name__ == "__main__":
    app.run(debug=True)

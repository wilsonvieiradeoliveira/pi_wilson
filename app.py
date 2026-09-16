from flask import Flask, render_template, request, redirect, url_for

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
    {"nome": "Caneta Azul", "preco": 10.50, "estoque": 9},
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
    busca = request.args.get("busca", "")
    lista = produtos
    if busca:
        lista = [p for p in produtos if busca.lower() in p["nome"].lower()]
    return render_template("catalago.html", produtos=lista, busca=busca)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        erro = None

        if not nome:
            erro = "Preencha o nome do produto."

        if not erro:
            try:
                preco = float(request.form["preco"])
            except ValueError:
                erro = "Preco invalido."

        if not erro and preco <= 0:
            erro = "O preco deve ser maior que zero."

        if erro:
            return render_template("cadastro.html", erro=erro)

        novo = {
            "nome": nome,
            "preco": preco,
            "estoque": int(request.form["estoque"]),
            "categoria": request.form.get("categoria", ""),
        }
        produtos.append(novo)
        return redirect(url_for("catalago"))
    return render_template("cadastro.html")


@app.route("/enquete", methods=["GET", "POST"])
def enquete():
    if request.method == "POST":
        voto = request.form["voto"]
        motivo = request.form["motivo"]
        return render_template("obrigado.html", voto=voto, motivo=motivo)
    return render_template("enquete.html")


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

import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

nome = "Aluno"
idade = 18
email = "aluno@email.com"
youtube = "Youtube_Aluno"
lista_hobbies = ["Jogar bola", "Ouvir música", "Jogar Vídeo Game"]


def conectar():
    con = sqlite3.connect("loja.db")
    con.row_factory = sqlite3.Row
    return con


def criar_tabela():
    con = conectar()
    con.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
    """)
    con.close()


criar_tabela()


def buscar_produto(id_produto):
    con = conectar()
    produto = con.execute("SELECT * FROM produtos WHERE id = ?",
                          (id_produto,)).fetchone()
    con.close()
    return produto


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
def catalogo():
    busca = request.args.get("busca", "")
    con = conectar()
    produtos = con.execute("SELECT * FROM produtos").fetchall()
    con.close()
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

        estoque = int(request.form["estoque"])
        con = conectar()
        con.execute("INSERT INTO produtos (nome, preco, estoque) "
                    "VALUES (?, ?, ?)", (nome, preco, estoque))
        con.commit()
        con.close()

        return redirect(url_for("catalogo"))

    return render_template("cadastro.html")


@app.route("/enquete", methods=["GET", "POST"])
def enquete():
    if request.method == "POST":
        voto = request.form["voto"]
        motivo = request.form["motivo"]
        return render_template("obrigado.html", voto=voto, motivo=motivo)
    return render_template("enquete.html")


@app.route("/produto/<int:id_produto>")
def detalhe(id_produto):
    produto = buscar_produto(id_produto)
    if produto is None:
        return "Produto não encontrado", 404
    return render_template("produto.html", produto=produto)


@app.route("/excluir/<int:id_produto>", methods=["POST"])
def excluir(id_produto):
    con = conectar()
    con.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    con.commit()
    con.close()

    return redirect(url_for("catalogo"))


@app.route("/editar/<int:id_produto>", methods=["GET", "POST"])
def editar(id_produto):
    produto = buscar_produto(id_produto)
    if produto is None:
        return "Produto não encontrado", 404
    if request.method == "POST":
        nome = request.form["nome"].strip()
        if not nome:
            return render_template("editar.html", produto=produto,
                                   erro="Preencha o nome.")
        preco = float(request.form["preco"])
        estoque = int(request.form["estoque"])
        con = conectar()
        con.execute("UPDATE produtos SET nome = ?, preco = ?, "
                    "estoque = ? WHERE id = ?",
                    (nome, preco, estoque, id_produto))
        con.commit()
        con.close()
        return redirect(url_for("detalhe", id_produto=id_produto))
    return render_template("editar.html", produto=produto)


if __name__ == "__main__":
    app.run(debug=True)

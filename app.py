import json
import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

nome = "Aluno"
idade = 18
email = "aluno@email.com"
youtube = "Youtube_Aluno"
lista_hobbies = ["Jogar bola", "Ouvir música", "Jogar Vídeo Game"]


def carregar_produtos():
    if not os.path.exists("produtos.json"):
        return []  # primeira vez: começa vazio
    with open("produtos.json", "r") as arquivo:
        return json.load(arquivo)


def salvar_produtos():
    with open("produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)


produtos = carregar_produtos()


def proximo_id():
    maior = 0
    for p in produtos:
        if p["id"] > maior:
            maior = p["id"]
    return maior + 1


def buscar_produto(id_produto):
    for p in produtos:
        if p["id"] == id_produto:
            return p
    return None


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
            "id": proximo_id(),
            "nome": nome,
            "preco": preco,
            "estoque": int(request.form["estoque"]),
            "categoria": request.form.get("categoria", ""),
        }
        produtos.append(novo)
        salvar_produtos()  # grava logo depois de cadastrar
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
    produto = buscar_produto(id_produto)
    if produto is not None:
        produtos.remove(produto)
        salvar_produtos()
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
        produto["nome"] = nome
        produto["preco"] = float(request.form["preco"])
        produto["estoque"] = int(request.form["estoque"])
        salvar_produtos()
        return redirect(url_for("detalhe", id_produto=id_produto))
    return render_template("editar.html", produto=produto)


if __name__ == "__main__":
    app.run(debug=True)

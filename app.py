from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/hobbies")
def hobbies():
    lista = ["Jogar bola", "Ouvir música", "Jogar Vídeo Game"]
    return render_template("hobbies.html", hobbies=lista)


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
        email="wilson22vieira@gmail.com",
        youtube="vieira7915",
    )

@app.route("/perfil")
def perfil():
    return render_template("perfil.html", nome="Ana", idade=15, curso=None)


@app.route("/perfil/<nome>")
def perfil_nome(nome):
    return render_template("perfil.html", nome=nome, idade=15, curso="Informática")


@app.route("/aluno/<nome>")
def aluno(nome):
    return render_template("aluno.html", nome=nome)

@app.route("/recado/<nome>")
def recado(nome):
    return render_template("recado.html", nome=nome)

@app.route("/tabuada/<int:numero>")
def tabuada(numero):
    return render_template("tabuada.html", numero=numero)

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return render_template("soma.html", a=a, b=b)


@app.route("/dobro/<int:n>")
def dobro(n):
    return render_template("dobro.html", n=n)


if __name__ == "__main__":
    app.run(debug=True)

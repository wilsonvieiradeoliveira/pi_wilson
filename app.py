from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
        <h1>Ola, eu sou Wilson!</h1>
        <p>Tenho 41 anos e sou professor de Informatica.</p>
    """

@app.route("/sobre")
def sobre():
    return """
        <h1>Sobre mim</h1>
        <p>Sou professor de informática com 2 anos de atuação.</p>
        <p>Desenvolvedor full-stack sênior!</p>
    """

@app.route("/hobbies")
def hobbies():
    return """
        <h1>Meus hobbies</h1>
        <ul>
            <li>Jogar bola</li>
            <li>Ouvir música</li>
            <li>Jogar Vídeo Game</li>
        </ul>
    """

@app.route("/futuro")
def futuro():
    return """
        <h1>Meu futuro</h1>
        <p>Quero continuar trabalhando como desenvolvedor porque gosto de resolver problemas com tecnologia.</p>
    """

@app.route("/contato")
def contato():
    return """
        <h1>Contato</h1>
        <p>Email: wilson22vieira@gmail.com</p>
        <p>Youtube: vieira7915</p>
    """

@app.route("/aluno/<nome>")
def perfil(nome):
    return f"<h1>Perfil de {nome}</h1>"

@app.route("/recado/<nome>")
def recado(nome):
    return f"<h1>Recado para {nome}</h1><p>Obrigado por visitar meu cartão de visita, {nome}!</p>"

@app.route("/tabuada/<int:numero>")
def tabuada(numero):
    html = f"<h1>Tabuada do {numero}</h1>"
    for i in range(1, 11):
        html += f"<p>{numero} x {i} = {numero * i}</p>"
    return html

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return f"<h1>{a} + {b} = {a + b}</h1>"


@app.route("/dobro/<int:n>")
def dobro(n):
    return f"<h1>O dobro de {n} é {n * 2}</h1>"


if __name__ == "__main__":
    app.run(debug=True)

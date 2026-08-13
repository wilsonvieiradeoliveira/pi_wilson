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


if __name__ == "__main__":
    app.run(debug=True)

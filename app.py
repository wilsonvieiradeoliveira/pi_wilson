from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
        <h1>Ola, eu sou Wilson!</h1>
        <p>Tenho 41 anos e estudo Informatica.</p>
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
        <p>Quero ser desenvolvedor porque gosto de resolver problemas com tecnologia.</p>
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

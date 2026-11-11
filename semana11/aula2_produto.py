def buscar_produto(id_produto):
    for p in produtos:
        if p["id"] == id_produto:
            return p
    return None

@app.route("/produto/<int:id_produto>")
def detalhe(id_produto):
    produto = buscar_produto(id_produto)
    if produto is None:
        return "Produto não encontrado", 404
    return render_template("produto.html", produto=produto)

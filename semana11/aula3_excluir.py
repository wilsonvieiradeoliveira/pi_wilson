@app.route("/excluir/<int:id_produto>", methods=["POST"])
def excluir(id_produto):
    produto = buscar_produto(id_produto)
    if produto is not None:
        produtos.remove(produto)
        salvar_produtos()
    return redirect(url_for("catalogo"))

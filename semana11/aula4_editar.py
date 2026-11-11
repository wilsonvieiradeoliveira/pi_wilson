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

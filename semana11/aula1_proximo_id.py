def proximo_id():
    maior = 0
    for p in produtos:
        if p["id"] > maior:
            maior = p["id"]
    return maior + 1

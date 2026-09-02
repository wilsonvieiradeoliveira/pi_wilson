# Cartao de Visita Web

Meu primeiro site em Flask.
Feito no curso Tecnico em Informatica.

## Como rodar
1. pip install flask
2. python app.py

## Semana 5 — Bootstrap e visual profissional
- Bootstrap 5.3.3 instalado no `base.html` via CDN, com a linha do plano
  B offline (`static/bootstrap.min.css`) comentada ao lado — se a internet
  cair, basta trocar qual linha fica comentada.
- Navbar responsiva (`navbar navbar-expand-lg navbar-dark bg-dark`) com
  todos os links do site, herdada por todas as paginas via `base.html`.
- Grid responsivo (`row`/`col-md-4`) com os diferenciais da loja na
  pagina inicial.
- Catalogo em cards (`card h-100`) com badges condicionais (`Esgotado`
  ou `Oferta`) e uma tabela administrativa (`table-striped table-hover`)
  logo abaixo.
- Pasta `static/` guarda arquivos fixos do projeto (hoje, o CSS do
  Bootstrap para uso offline).
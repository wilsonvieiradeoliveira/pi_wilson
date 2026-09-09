# Cartao de Visita Web

Meu primeiro site em Flask.
Feito no curso Tecnico em Informatica.

## Como rodar
1. pip install flask
2. python app.py

## Jinja2 no VSCode

### O problema
Os arquivos em `templates/` são HTML misturado com sintaxe Jinja2
(`{% %}`, `{{ }}`, `{# #}`). Por padrao, o VSCode trata qualquer `.html`
como HTML puro e o validador embutido reclama de coisas como:
- `Doctype must be declared before any non-comment content` (porque tags
  Jinja como `{% extends %}` vem antes do `<!DOCTYPE>` nos templates filhos)
- `Special characters must be escaped: [ < ]` (o validador tenta ler
  `{% elif p.preco < 10 %}` como HTML e nao entende o `<` da comparacao)

Esses avisos sao falsos positivos: o codigo esta correto, o VSCode
so nao sabe que aquele arquivo tambem tem Jinja2 misturado.

### Configuracao recomendada
1. Instale a extensao **Better Jinja** (`samuelcolvin.jinjahtml`) —
   pela aba de Extensions ou:
   ```
   code --install-extension samuelcolvin.jinjahtml
   ```
2. Crie (ou edite) o arquivo `.vscode/settings.json` do projeto com:
   ```json
   {
       "files.associations": {
           "**/templates/**/*.html": "jinja-html"
       },
       "emmet.includeLanguages": {
           "jinja-html": "html"
       }
   }
   ```
   > **Atencao:** a pasta `.vscode/` esta no `.gitignore` deste projeto
   > (config de editor e pessoal, nao versionamos). Isso significa que
   > cada pessoa que clonar o repositorio precisa criar esse
   > `settings.json` na propria maquina — ele nao vem pronto do Git.
3. Reabra os arquivos `.html` de `templates/` (ou recarregue a janela
   do VSCode: `Ctrl+Shift+P` → "Reload Window"). O realce de sintaxe do
   Jinja2 passa a funcionar e os avisos falsos de HTML desaparecem.

### Sintaxe basica do Jinja2 usada neste projeto
| Sintaxe | Para que serve | Onde aparece |
|---|---|---|
| `{% extends "base.html" %}` | herda o layout comum | topo de cada template |
| `{% block nome %}...{% endblock %}` | define/preenche uma secao do layout | `base.html` e templates filhos |
| `{{ variavel }}` | imprime um valor vindo do `app.py` | `{{ p.nome }}`, `{{ idade }}` |
| `{% for item in lista %}...{% endfor %}` | repete um bloco de HTML | cards e tabela do catalogo |
| `{% if cond %}...{% elif cond %}...{% else %}...{% endif %}` | HTML condicional | badges de Esgotado/Oferta |
| `{{ valor|format(...) }}` | filtro: transforma o valor antes de imprimir | `{{ "%.2f"|format(p.preco) }}` |
| `loop.index0` | indice (comecando em 0) dentro de um `{% for %}` | link `/produto/{{ loop.index0 }}` |

Documentacao completa: https://jinja.palletsprojects.com/
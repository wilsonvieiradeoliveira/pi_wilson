# Gabarito — Semana 3: Templates com Jinja2 e herança de páginas

Respostas de referência para as perguntas escritas da apostila. O código de todos os
mini-desafios, do exercício de rota e da prática avaliativa está implementado em
[app.py](app.py) e em [templates/](templates/).

## Aula 1 — O HTML sai do Python

**1) Por que a pasta precisa se chamar exatamente `templates`?**
Porque é o nome que o `render_template` (e o Flask por baixo dos panos) usa para
localizar os arquivos automaticamente. Qualquer outro nome faz o Flask não encontrar
o arquivo e lançar `TemplateNotFound`.

**2) Vantagens de separar lógica (Python) e aparência (HTML):**
- O editor reconhece o arquivo como HTML puro: colorido de sintaxe e autocomplete
  voltam a funcionar (dentro de uma string Python isso se perde).
- Cada responsabilidade fica isolada: quem mexe no visual (HTML/CSS) não precisa
  entender rotas, e quem mexe na lógica não precisa editar marcação. Em equipes reais,
  isso permite back-end e front-end trabalharem em paralelo sem pisar no código um do outro.

**Mini-desafio:** o `index.html` foi migrado para `templates/index.html` e a rota `/`
agora usa `render_template("index.html")` — ver [app.py](app.py#L6-L8). Para quem
acessa o site pelo navegador, nada muda (mesmo HTML final). Para quem programa, o
ganho é grande: o `app.py` fica limpo, sem HTML espremido em string.

## Aula 2 — Variáveis no template

**1) Diferença entre o que o Python faz e o que o template faz:**
O Python decide *quais dados existem* (busca, calcula, valida) e os repassa ao
template através dos argumentos nomeados de `render_template`. O template só
*exibe* esses dados no lugar certo, usando `{{ variavel }}` — ele não decide nada,
apenas encaixa o valor recebido no HTML.

**2) Rota `/perfil/<nome>`:**
```python
@app.route("/perfil/<nome>")
def perfil_nome(nome):
    return render_template("perfil.html", nome=nome, idade=15, curso="Informática")
```
Implementada em [app.py](app.py#L46-L48), usando [templates/perfil.html](templates/perfil.html).

**Mini-desafio (estilizar perfil.html):** a estilização em si foi deixada propositalmente
de fora por enquanto — `base.html` e as páginas filhas estão sem CSS. O visual do site
será resolvido em uma aula futura com Bootstrap offline, então o HTML fica "limpo" hoje
para não competir com as classes do Bootstrap depois. O `{{ nome }}` já funciona
normalmente com qualquer nome passado na URL, independentemente de existir CSS ou não —
a substituição do Jinja2 acontece antes de qualquer estilo ser aplicado.

## Aula 3 — Herança de templates: base.html

**1) Onde mudar o menu do site: no `base.html` ou em cada página?**
No `base.html`. Ele é a única fonte do menu; todas as páginas filhas herdam esse
trecho automaticamente via `{% extends %}`. Editar o menu em cada página filha
reintroduziria o problema original (duplicação e risco de inconsistência).

**2) O que fazem `{% extends %}` e `{% block %}`?**
- `{% extends "base.html" %}`: diz que este template herda a estrutura inteira do
  `base.html` (html, head, nav, footer etc.).
- `{% block nome %}...{% endblock %}`: marca um "encaixe". No `base.html` ele fica
  vazio (só delimita onde o conteúdo da filha entra); na página filha ele é
  preenchido com o conteúdo específico daquela página.

**Mini-desafio:** `index.html` e `sobre.html` herdam de `base.html` (ver
[templates/index.html](templates/index.html) e [templates/sobre.html](templates/sobre.html)).
**O que acontece se a filha esquecer o `extends`:** testado diretamente — sem a linha
`{% extends "base.html" %}`, o `{% block conteudo %}` deixa de ser um "encaixe" e passa
a ser renderizado como conteúdo solto. O resultado é uma página **sem** `<html>`,
sem `<head>` e sem o `<nav>` do menu — só o HTML cru que estava dentro do bloco
aparece na tela, sem nenhuma navegação.

## Aula 4 — Listas no template: {% for %}

**1) Diferença entre `{{ }}` e `{% %}`:**
- `{{ }}` **mostra** um valor: `{{ item }}`, `{{ nome }}`.
- `{% %}` **executa** uma ação/comando: `{% for item in hobbies %}`,
  `{% if hobbies %}`, `{% extends "base.html" %}`.

**2) Por que usar `{% for %}` em vez de escrever os `<li>` na mão?**
Porque o template passa a funcionar para qualquer tamanho de lista — 3 hobbies ou
300 — sem precisar editar o HTML. Isso também elimina erros de copiar/colar e
prepara o template para quando os dados vierem de um banco de dados (2º bimestre):
a lista muda, o template continua igual.

**Mini-desafio:** foi adicionado um hobby novo na lista dentro de [app.py](app.py#L18-L20)
sem tocar em `hobbies.html`. Ao recarregar `/hobbies`, o novo item aparece
automaticamente na lista renderizada — isso é essencial para sistemas com dados que
mudam (cadastros, banco de dados): o template não precisa ser reescrito a cada
mudança de conteúdo.

## Aula 5 — Prática avaliativa: Cartão de visita 2.0

Checklist de entrega:
- [x] `base.html` com menu funcionando em todas as páginas (Início, Sobre, Hobbies,
      Futuro, Contato) — [templates/base.html](templates/base.html)
- [x] Todas as páginas com `{% extends %}` e `app.py` sem HTML em strings —
      confirmado em [app.py](app.py): toda rota retorna `render_template(...)`
- [x] `hobbies.html` montando a lista com `{% for %}` —
      [templates/hobbies.html](templates/hobbies.html)
- [ ] 2+ commits durante a aula + push no GitHub — a fazer pelo aluno/professor
      no fluxo normal de Git (ver commits sugeridos abaixo)

## Desafio extra — {% if %}

Implementado em [templates/hobbies.html](templates/hobbies.html): se `hobbies` vier
vazia, mostra "Nenhum hobby cadastrado ainda." em vez da lista. Para testar o `else`
em ação, foi criada a rota `/hobbies-vazio` em [app.py](app.py#L14-L16), que chama
`render_template("hobbies.html", hobbies=[])`.

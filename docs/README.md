# yolopunk Documentation

<div align="center">

![yolopunk](https://img.shields.io/badge/yolopunk-ergodic-c41e3a?style=for-the-badge)
![MkDocs](https://img.shields.io/badge/MkDocs-Material-526CFE?style=for-the-badge&logo=materialformkdocs)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge&logo=jinja)

**Documentação ergódica que sangra precisão**

</div>

---

## 🎯 Estrutura

```
docs/
├── index.md                    # Página inicial
├── grimorio/                  # Documentação profunda
│   ├── sinopse.md
│   ├── treino.md
│   └── validacao.md
├── api/                      # Referência da API
│   └── overview.md
├── exemplos/                 # Exemplos práticos
│   └── quickstart.md
├── overrides/                # Templates Jinja2 customizados
│   ├── main.html             # Template principal
│   └── home.html             # Template da home
├── stylesheets/              # Estilos CSS
│   ├── yolopunk.css          # Tema ergódico base
│   └── custom.css            # Customizações do usuário
├── javascripts/              # Scripts JS
│   └── yolopunk.js           # Efeitos ergódicos
└── .pages                    # Navegação
```

## 🚀 Quick Start

### Instalação

```bash
# Instalar dependências
pip install -r requirements-docs.txt
```

### Desenvolvimento Local

```bash
# Servir localmente com live reload
mkdocs serve

# Abrir no navegador
# http://127.0.0.1:8000
```

### Build

```bash
# Gerar site estático
mkdocs build

# Output em: site/
```

### Deploy

```bash
# Deploy para GitHub Pages
mkdocs gh-deploy
```

## 🎨 Customização

### Cores e Tema

Edite `docs/stylesheets/custom.css` para customizar:

```css
/* Suas customizações aqui */
.md-typeset h1 {
    color: var(--yp-blood-red);
    border-bottom: 2px solid var(--yp-blood-red);
}
```

### Variáveis CSS Disponíveis

```css
/* Paleta Ergódica */
--yp-blood-red: #c41e3a;
--yp-dark-red: #8b0000;
--yp-deep-red: #4a0000;
--yp-chaos-purple: #6a0dad;
--yp-void-black: #0a0a0a;
--yp-steel-gray: #2c2c2c;
--yp-ash-gray: #4a4a4a;
--yp-fog-white: #e8e8e8;
--yp-pulse-cyan: #00ffff;

/* Gradientes */
--yp-gradient-blood: linear-gradient(135deg, var(--yp-blood-red), var(--yp-dark-red));
--yp-gradient-chaos: linear-gradient(135deg, var(--yp-chaos-purple), var(--yp-blood-red));
--yp-gradient-void: linear-gradient(180deg, var(--yp-void-black), var(--yp-steel-gray));
```

### Templates Jinja2

Modifique `docs/overrides/main.html` para alterar estrutura:

```jinja2
{% extends "base.html" %}

{% block announce %}
  <!-- Seu conteúdo customizado -->
{% endblock %}

{% block content %}
  {{ super() }}
  <!-- Adicione elementos extras -->
{% endblock %}
```

### Blocos Disponíveis

- `{% block announce %}` - Barra de anúncio no topo
- `{% block header %}` - Cabeçalho
- `{% block hero %}` - Seção hero
- `{% block content %}` - Conteúdo principal
- `{% block footer %}` - Rodapé

## 📝 Escrevendo Documentação

### Frontmatter

Adicione metadados no início dos arquivos markdown:

```markdown
---
title: Título da Página
description: Descrição para SEO
ergodic: true
chaos_level: high
---

# Conteúdo
```

### Components Customizados

#### Grimório Header

```markdown
<div class="grimorio-header" markdown>

**Título do Grimório**  
_Subtítulo ergódico_

</div>
```

#### Hero Section

```markdown
<div class="hero" markdown>

## Título Grande

Descrição do conteúdo.

[Botão Primário](link.md){ .md-button .md-button--primary }
[Botão Secundário](link.md){ .md-button }

</div>
```

#### Cards Grid

```markdown
<div class="grid cards" markdown>

- :material-icon: **Título**

    ***

    Descrição do card.

- :material-icon: **Título**

    ***

    Descrição do card.

</div>
```

#### Navigation Footer

```markdown
<div class="navigation-footer" markdown>

[← Página Anterior](link.md){ .md-button }
[Próxima Página →](link.md){ .md-button .md-button--primary }

</div>
```

#### Ergodic Footer

```markdown
<div class="ergodic-footer" markdown>

_"Sua frase ergódica e inspiradora aqui."_

</div>
```

### Admonitions

```markdown
!!! tip "Dica"
Conteúdo da dica.

!!! warning "Aviso"
Conteúdo do aviso.

!!! quote "Citação"
Conteúdo da citação.
```

### Code Blocks

`````markdown
````python title="example.py"
from yolopunk import YoloPunk

detector = YoloPunk(model="yolov8n.pt")
\```
````
`````

`````

### Tabs

````markdown
=== "Python"

    ```python
    # Código Python
    ```

=== "YAML"

    ```yaml
    # Configuração YAML
    ```
`````

## 🔧 JavaScript Customizado

Edite `docs/javascripts/yolopunk.js` para adicionar interações:

```javascript
// Adicione suas funções customizadas
function myCustomFunction() {
    // Seu código aqui
}

document.addEventListener("DOMContentLoaded", function () {
    myCustomFunction();
});
```

## 🌐 Publicação

### GitHub Pages

```bash
# Deploy automático
mkdocs gh-deploy

# Site disponível em:
# https://crise-ergodica.github.io/yolopunk
```

### Outras Plataformas

**Netlify:**

```bash
# Build command
mkdocs build

# Publish directory
site/
```

**Vercel:**

```json
{
    "buildCommand": "mkdocs build",
    "outputDirectory": "site"
}
```

## 💡 Tips & Tricks

### Live Preview com Hot Reload

```bash
mkdocs serve --dev-addr=0.0.0.0:8000
```

### Strict Mode (Build com Warnings)

```bash
mkdocs build --strict
```

### Limpar Build

```bash
rm -rf site/
```

### Validar Links

```bash
# Instalar plugin
pip install mkdocs-linkcheck

# Adicionar ao mkdocs.yml
plugins:
- linkcheck
```

## 📖 Recursos

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Markdown Guide](https://www.markdownguide.org/)

## 👥 Contribuindo

Para contribuir com a documentação:

1. Fork o repositório
2. Crie sua branch (`git checkout -b docs/nova-secao`)
3. Commit suas mudanças (`git commit -m 'docs: add nova seção'`)
4. Push para a branch (`git push origin docs/nova-secao`)
5. Abra um Pull Request

---

<div align="center">

**Sangre precisão na documentação** 🩸

Feito com ❤️ e caos controlado

</div>

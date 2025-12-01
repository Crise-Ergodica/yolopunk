# Troubleshooting - yolopunk Docs

<div align="center">

![Status](https://img.shields.io/badge/status-resolvendo%20caos-c41e3a?style=for-the-badge)

**Guia de solução para problemas comuns da documentação**

</div>

---

## 🔥 Problemas Comuns

### 1. CSS/HTML Não Aparece (Bento Grid Não Renderiza)

#### Sintomas
- Página carrega mas o bento grid não aparece
- Inspecionando elemento, HTML não está presente
- CSS não carrega no DevTools

#### Causa
**Filtro Jinja2 `| url` incompatível com custom themes sem Material for MkDocs**

Quando você usa `theme.name: null` e `custom_dir`, os filtros do Material não estão disponíveis.

#### Solução

**ANTES (errado):**
```html
<!-- main.html -->
<link rel="stylesheet" href="{{ 'stylesheets/yolopunk-base.css' | url }}">
```

**DEPOIS (correto):**
```html
<!-- main.html -->
{% for path in config.extra_css %}
<link rel="stylesheet" href="{{ base_url }}/{{ path }}">
{% endfor %}
```

**Para partials (bento-grid.html, etc.):**

**ANTES (errado):**
```html
<a href="{{ 'grimorio/sinopse/' | url }}" class="bento-card">
```

**DEPOIS (correto):**
```html
<a href="{{ base_url }}/grimorio/sinopse/" class="bento-card">
```

---

### 2. Estilos Não Aplicam

#### Sintomas
- HTML renderiza mas sem estilos
- Página branca ou com estilos padrão
- Console mostra erros 404 para arquivos CSS

#### Causa
Caminhos incorretos no `mkdocs.yml` ou templates

#### Solução

**Verifique `mkdocs.yml`:**
```yaml
extra_css:
  - stylesheets/yolopunk-base.css  # ✓ Caminho relativo a docs/
  - stylesheets/bento-grid.css
```

**Estrutura de pastas esperada:**
```
docs/
├── stylesheets/
│   ├── yolopunk-base.css
│   └── bento-grid.css
├── custom_theme/
│   ├── main.html
│   └── partials/
└── index.md
```

**Verificar no navegador:**
1. Abra DevTools (F12)
2. Aba "Network"
3. Recarregue a página
4. Procure por arquivos CSS com status 404
5. Ajuste caminhos conforme necessário

---

### 3. Fontes Não Carregam

#### Sintomas
- Texto aparece com fonte padrão do sistema
- Console mostra erros de CORS ou 404 para fontes

#### Solução

**Google Fonts (recomendado):**
```html
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
```

**No CSS:**
```css
:root {
  --font-sans: "Space Grotesk", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}

body {
  font-family: var(--font-sans);
}
```

---

### 4. Templates Não Encontrados

#### Sintomas
- Erro: `jinja2.exceptions.TemplateNotFound: partials/bento-grid.html`
- Página não renderiza

#### Causa
Estrutura de diretórios incorreta ou caminhos errados

#### Solução

**Estrutura correta:**
```
docs/
└── custom_theme/
    ├── main.html
    ├── home.html
    └── partials/
        ├── bento-grid.html
        ├── header.html
        └── footer.html
```

**No `mkdocs.yml`:**
```yaml
theme:
  name: null
  custom_dir: docs/custom_theme  # Caminho correto
```

**Incluindo partials:**
```jinja2
{# Correto - caminho relativo a custom_theme/ #}
{% include "partials/bento-grid.html" %}

{# Errado - não funciona #}
{% include "docs/custom_theme/partials/bento-grid.html" %}
```

---

### 5. Variáveis CSS Não Funcionam

#### Sintomas
- Cores não aplicam
- Elementos aparecem com estilos padrão
- Console mostra `invalid property value`

#### Causa
Variáveis CSS não definidas antes do uso

#### Solução

**Defina variáveis no `:root`:**
```css
/* yolopunk-base.css */
:root {
  --crimson: #dc143c;
  --dark-bg: #0a0a0a;
  --text-primary: #f5f5f5;
  /* ... outras variáveis */
}
```

**Use em outros arquivos:**
```css
/* bento-grid.css */
.bento-card {
  background: var(--card-bg);  /* ✓ Variável definida no :root */
  color: var(--text-primary);
}
```

**Ordem de importação no `mkdocs.yml`:**
```yaml
extra_css:
  - stylesheets/yolopunk-base.css  # PRIMEIRO - define variáveis
  - stylesheets/bento-grid.css     # DEPOIS - usa variáveis
```

---

### 6. JavaScript Não Executa

#### Sintomas
- Interações não funcionam
- Animações travadas
- Console mostra erros

#### Causa
Scripts carregados antes do DOM ou erros de sintaxe

#### Solução

**Carregar scripts no final do body:**
```html
<body>
    <!-- conteúdo -->
    
    <!-- Scripts no final -->
    <script src="{{ base_url }}/javascripts/yolopunk.js"></script>
</body>
```

**Ou usar defer:**
```html
<head>
    <script src="{{ base_url }}/javascripts/yolopunk.js" defer></script>
</head>
```

**Aguardar DOM pronto:**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Seu código aqui
});
```

---

### 7. Build Falha no GitHub Actions

#### Sintomas
- Deploy falha no CI/CD
- Erro: `mkdocs.exceptions.ConfigurationError`

#### Causa
Dependências não instaladas ou versões incompatíveis

#### Solução

**Criar/atualizar `requirements-docs.txt`:**
```txt
mkdocs>=1.5.0
mkdocs-material>=9.5.0
mkdocs-material-extensions>=1.3.0
pygments>=2.16.0
pymdown-extensions>=10.5.0
```

**GitHub Actions workflow:**
```yaml
# .github/workflows/docs.yml
name: Deploy Docs

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements-docs.txt
      
      - name: Build docs
        run: mkdocs build --strict
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

---

## 🛠️ Ferramentas de Debug

### MkDocs Serve com Debug

```bash
# Modo verbose
mkdocs serve --verbose

# Strict mode (falha em warnings)
mkdocs build --strict
```

### Verificar Sintaxe Jinja2

```python
# test_template.py
from jinja2 import Template, Environment

with open('docs/custom_theme/main.html') as f:
    template_str = f.read()

try:
    env = Environment()
    template = env.from_string(template_str)
    print("✅ Template válido")
except Exception as e:
    print(f"❌ Erro: {e}")
```

### Validar CSS

```bash
# Instalar stylelint
npm install -g stylelint stylelint-config-standard

# Validar
stylelint "docs/stylesheets/**/*.css"
```

### Inspecionar Build Output

```bash
# Build e inspecionar
mkdocs build
cd site/
python -m http.server 8080

# Abrir http://localhost:8080
```

---

## 💡 Dicas de Prevenção

### 1. Use Linting

**HTML/Jinja2:**
```bash
pip install djlint
djlint docs/custom_theme --check
```

**CSS:**
```bash
npm install -g stylelint
stylelint "docs/**/*.css"
```

**Markdown:**
```bash
pip install mdformat
mdformat docs/
```

### 2. Teste Localmente Antes de Commitar

```bash
# Limpar build anterior
rm -rf site/

# Build fresh
mkdocs build --strict

# Servir e testar
mkdocs serve

# Se tudo OK, commit
git add .
git commit -m "docs: atualização"
```

### 3. Versionamento de Dependências

**Pin versões exatas em produção:**
```txt
mkdocs==1.5.3
mkdocs-material==9.5.3
pygments==2.17.2
```

### 4. Validação Automática

**Pre-commit hook:**
```bash
# .git/hooks/pre-commit
#!/bin/bash
mkdocs build --strict || exit 1
```

---

## 📚 Recursos Úteis

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Jinja2 Template Designer Docs](https://jinja.palletsprojects.com/templates/)
- [CSS Variables MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [GitHub Pages Deploy](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)

---

## ❓ Ainda com Problemas?

1. **Cheque os logs:** `mkdocs serve --verbose`
2. **Limpe o cache:** `rm -rf site/ && mkdocs build`
3. **Teste em modo strict:** `mkdocs build --strict`
4. **Abra uma issue:** [GitHub Issues](https://github.com/Crise-Ergodica/yolopunk/issues)

---

<div align="center">

**O caos é apenas ordem não compreendida** 🔥

*Mantenha a documentação sangrando precisão*

</div>
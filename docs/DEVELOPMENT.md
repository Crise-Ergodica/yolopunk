# Guia Rápido de Desenvolvimento

## Setup Inicial

```bash
# 1. Clone o repositório
git clone https://github.com/Crise-Ergodica/yolopunk.git
cd yolopunk

# 2. Install as dependências de documentação
pip install -r requirements-docs.txt

# 3. Inicie o servidor de desenvolvimento
mkdocs serve

# 4. Acesse no navegador
# http://127.0.0.1:8000
```

## Workflow de Desenvolvimento

### 1. Criar Nova Página

```bash
# Criar arquivo markdown na pasta apropriada
touch docs/grimorio/nova-secao.md
```

### 2. Adicionar à Navegação

Edite `mkdocs.yml`:

```yaml
nav:
    - Grimório:
          - Sinopse: grimorio/sinopse.md
          - Nova Seção: grimorio/nova-secao.md # Adicione aqui
```

### 3. Preview em Tempo Real

O `mkdocs serve` tem live reload - basta salvar o arquivo e o navegador atualiza automaticamente.

### 4. Build para Produção

```bash
# Build com strict mode (falha em warnings)
mkdocs build --strict

# Build normal
mkdocs build
```

### 5. Deploy

```bash
# Deploy manual para GitHub Pages
mkdocs gh-deploy

# Ou deixe o GitHub Actions fazer automaticamente ao push para main
git add .
git commit -m "docs: adiciona nova seção"
git push origin main
```

## Estrutura de Pastas

```
docs/
├── index.md              # Página inicial
├── grimorio/            # Documentação profunda
├── api/                 # Referência da API
├── exemplos/            # Exemplos práticos
├── overrides/           # Templates Jinja2
│   ├── main.html        # Template base
│   └── home.html        # Template da home
├── stylesheets/         # CSS customizado
│   ├── yolopunk.css     # Tema base (não editar)
│   └── custom.css       # Suas customizações
└── javascripts/         # JavaScript
    └── yolopunk.js      # Efeitos ergódicos
```

## Customização

### CSS

Edite `docs/stylesheets/custom.css`:

```css
/* Exemplo: mudar cor dos headings */
.md-typeset h1 {
    color: var(--yp-blood-red);
    border-bottom: 2px solid var(--yp-blood-red);
}

/* Exemplo: customizar cards */
.md-typeset .grid.cards > ol > li:hover {
    transform: translateY(-5px);
    box-shadow: var(--yp-shadow-void);
}
```

### Templates Jinja2

Edite `docs/overrides/main.html`:

```jinja2
{% extends "base.html" %}

{% block content %}
  {{ super() }}
  <!-- Seu conteúdo adicional aqui -->
{% endblock %}
```

### JavaScript

Edite `docs/javascripts/yolopunk.js`:

```javascript
document.addEventListener("DOMContentLoaded", function () {
    // Seu código aqui
});
```

## Components Disponíveis

Veja a [página de components](exemplos/components.md) para todos os elementos visuais disponíveis.

### Quick Reference

**Hero:**

```markdown
<div class="hero" markdown>
## Título
Descrição
</div>
```

**Cards:**

```markdown
<div class="grid cards" markdown>
-   :material-icon: **Título**
    ---
    Descrição
</div>
```

**Grimório Header:**

```markdown
<div class="grimorio-header" markdown>
**Título**  
*Subtítulo*
</div>
```

**Navigation Footer:**

```markdown
<div class="navigation-footer" markdown>
[← Anterior](link.md){ .md-button }
[Próximo →](link.md){ .md-button .md-button--primary }
</div>
```

## Debugging

### Build Errors

```bash
# Build com strict mode para ver todos os warnings
mkdocs build --strict

# Build com mais verbosidade
mkdocs build --verbose
```

### Preview em Outros Dispositivos

```bash
# Bind em todas as interfaces
mkdocs serve --dev-addr=0.0.0.0:8000

# Acesse de outro dispositivo na mesma rede
# http://SEU_IP:8000
```

### Limpar Cache

```bash
# Remover build anterior
rm -rf site/

# Rebuild
mkdocs build
```

## CI/CD

O repositório tem GitHub Actions configurado em `.github/workflows/docs.yml`.

### Trigger Automático

Deploy automático quando:

- Push para `main` afetando `docs/**` ou `mkdocs.yml`
- Pull request modificando documentação

### Trigger Manual

Via GitHub Actions UI ou:

```bash
gh workflow run docs.yml
```

## Tips & Tricks

### 1. Live Reload Múltiplas Janelas

Abra várias abas do navegador - todas atualizam simultaneamente.

### 2. Strict Mode

Sempre use `--strict` em CI/CD para pegar errors cedo:

```yaml
- name: Build documentation
  run: mkdocs build --strict
```

### 3. Link Check

Install plugin para validar links:

```bash
pip install mkdocs-linkcheck
```

Adicione ao `mkdocs.yml`:

```yaml
plugins:
    - linkcheck
```

### 4. Minificação

Já configurado no `requirements-docs.txt`:

```yaml
plugins:
    - minify:
          minify_html: true
          minify_js: true
          minify_css: true
```

### 5. Git Revision Date

Mostra data da última modificação automaticamente (já configurado).

## Troubleshooting

### Error: "Port already in use"

```bash
# Usar outra porta
mkdocs serve --dev-addr=127.0.0.1:8001
```

### Error: "Theme not found"

```bash
# Reinstalar dependências
pip install --upgrade -r requirements-docs.txt
```

### CSS não aplica

```bash
# Limpar cache do navegador (Ctrl+Shift+R)
# Ou reconstruir
rm -rf site/
mkdocs build
```

### JavaScript não executa

Verifique o console do navegador (F12) para errors.

## Recursos

- [MkDocs Docs](https://www.mkdocs.org/)
- [Material Theme](https://squidfunk.github.io/mkdocs-material/)
- [Jinja2 Docs](https://jinja.palletsprojects.com/)
- [Markdown Guide](https://www.markdownguide.org/)

---

**Happy documenting! 🩸**

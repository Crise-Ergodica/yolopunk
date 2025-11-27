# Customização com Jinja2

<div class="grimorio-header" markdown>

**Templates Ergódicos**  
*Controle total sobre cada elemento*

</div>

---

Este guia mostra como customizar completamente a documentação usando templates Jinja2.

## O que é Jinja2?

Jinja2 é um template engine Python que permite:

- **Herança de templates** - Estenda templates base
- **Blocos customizáveis** - Substitua ou estenda seções específicas
- **Lógica condicional** - Mostre conteúdo baseado em condições
- **Loops** - Gere conteúdo dinamicamente
- **Filtros** - Transforme dados no template

## Estrutura de Templates

```
docs/overrides/
├── main.html              # Template principal (você customiza)
├── home.html              # Template da home
├── partials/              # Componentes reutilizáveis
│   ├── header.html
│   ├── footer.html
│   └── toc.html
└── 404.html               # Página de erro customizada
```

## Blocos Disponíveis

### Blocos Principais

```jinja2
{% block site_meta %}        # Meta tags HTML
{% block htmltitle %}        # Título da página (<title>)
{% block styles %}           # Estilos CSS
{% block libs %}             # Bibliotecas JS
{% block fonts %}            # Fontes
{% block analytics %}        # Analytics

{% block announce %}         # Barra de anúncio
{% block header %}           # Cabeçalho
{% block tabs %}             # Abas de navegação
{% block hero %}             # Seção hero
{% block content %}          # Conteúdo principal
{% block footer %}           # Rodapé

{% block scripts %}          # Scripts JavaScript
```

### Exemplo: Estrutura Básica

```jinja2
{% extends "base.html" %}

{% block content %}
  <!-- Seu conteúdo aqui -->
  {{ super() }}  {# Inclui o conteúdo original #}
{% endblock %}
```

## Customizações Comuns

### 1. Barra de Anúncio Customizada

```jinja2
{% block announce %}
  <div class="md-banner">
    <div class="md-banner__inner">
      {% if config.extra.announcement %}
        {{ config.extra.announcement }}
      {% else %}
        <strong>yolopunk v1.0</strong> - Agora com suporte a YOLOv8!
      {% endif %}
    </div>
  </div>
{% endblock %}
```

Configure em `mkdocs.yml`:

```yaml
extra:
  announcement: |
    <strong>Novo!</strong> Documentação completamente redesenhada.
```

### 2. Footer Customizado

```jinja2
{% block footer %}
  <footer class="md-footer">
    <div class="md-footer-meta md-typeset">
      <div class="md-footer-meta__inner md-grid">
        <div class="md-footer-copyright">
          <div class="blood-line"></div>
          {% if config.copyright %}
            <div>{{ config.copyright }}</div>
          {% endif %}
          <div>
            Built with 
            <a href="https://www.mkdocs.org/" target="_blank">MkDocs</a>
            and 
            <a href="https://squidfunk.github.io/mkdocs-material/" target="_blank">Material</a>
          </div>
          <div class="convergence-line"></div>
        </div>
      </div>
    </div>
  </footer>
{% endblock %}
```

### 3. Scripts Customizados

```jinja2
{% block scripts %}
  {{ super() }}  {# Mantém scripts originais #}
  
  <script>
    // Seu JavaScript customizado
    document.addEventListener('DOMContentLoaded', function() {
      console.log('yolopunk docs loaded!');
      
      // Adicionar analytics customizado
      if (typeof gtag !== 'undefined') {
        gtag('config', 'GA_MEASUREMENT_ID');
      }
    });
  </script>
{% endblock %}
```

### 4. Meta Tags SEO

```jinja2
{% block site_meta %}
  {{ super() }}
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{{ page.title }} - {{ config.site_name }}">
  <meta property="og:description" content="{{ config.site_description }}">
  <meta property="og:url" content="{{ page.canonical_url }}">
  <meta property="og:image" content="{{ config.site_url }}/assets/images/banner.png">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{{ page.title }}">
  <meta name="twitter:description" content="{{ config.site_description }}">
  <meta name="twitter:image" content="{{ config.site_url }}/assets/images/banner.png">
{% endblock %}
```

## Variáveis Disponíveis

### Config

```jinja2
{{ config.site_name }}           # Nome do site
{{ config.site_description }}    # Descrição
{{ config.site_url }}            # URL base
{{ config.repo_url }}            # URL do repositório
{{ config.copyright }}           # Copyright
{{ config.extra }}               # Variáveis extras do mkdocs.yml
```

### Page

```jinja2
{{ page.title }}                 # Título da página
{{ page.content }}               # Conteúdo HTML
{{ page.toc }}                   # Table of Contents
{{ page.meta }}                  # Metadados do frontmatter
{{ page.canonical_url }}         # URL canônica
{{ page.edit_url }}              # URL para editar
{{ page.is_homepage }}           # True se for a home
```

### Nav

```jinja2
{% for nav_item in nav %}
  {{ nav_item.title }}
  {{ nav_item.url }}
  {{ nav_item.is_page }}
  {{ nav_item.is_section }}
{% endfor %}
```

## Exemplos Avançados

### 1. Hero Dinâmico

```jinja2
{% block hero %}
  {% if page.meta and page.meta.hero %}
    <div class="ergodic-hero" style="
      background: linear-gradient(135deg, 
        {{ page.meta.hero_color_1 | default('#c41e3a') }}, 
        {{ page.meta.hero_color_2 | default('#8b0000') }}
      );
    ">
      <div class="hero-content">
        <h1>{{ page.meta.hero }}</h1>
        {% if page.meta.hero_description %}
          <p>{{ page.meta.hero_description }}</p>
        {% endif %}
      </div>
    </div>
  {% endif %}
{% endblock %}
```

Use no frontmatter:

```yaml
---
hero: Título Customizado
hero_description: Descrição
hero_color_1: "#6a0dad"
hero_color_2: "#c41e3a"
---
```

### 2. Breadcrumbs Customizados

```jinja2
{% block content %}
  {% if page.ancestors %}
    <nav class="ergodic-breadcrumbs">
      <ul>
        <li><a href="{{ config.site_url }}">Home</a></li>
        {% for ancestor in page.ancestors %}
          <li>
            <span class="separator">/</span>
            <a href="{{ ancestor.url }}">{{ ancestor.title }}</a>
          </li>
        {% endfor %}
        <li>
          <span class="separator">/</span>
          <span class="current">{{ page.title }}</span>
        </li>
      </ul>
    </nav>
  {% endif %}
  
  {{ super() }}
{% endblock %}
```

### 3. Table of Contents Customizado

```jinja2
{% block site_nav %}
  {% if page.toc %}
    <div class="ergodic-toc">
      <div class="toc-title">
        <span class="chaos-indicator"></span>
        Contents
      </div>
      {{ page.toc }}
    </div>
  {% endif %}
{% endblock %}
```

### 4. Navegação Anterior/Próxima

```jinja2
{% block content %}
  {{ super() }}
  
  <nav class="md-footer-nav" aria-label="Page navigation">
    <div class="md-footer-nav__inner">
      {% if page.previous_page %}
        <a href="{{ page.previous_page.url }}" class="md-footer-nav__link md-footer-nav__link--prev">
          <div class="md-footer-nav__title">
            <span class="md-footer-nav__direction">← Anterior</span>
            <div class="md-ellipsis">{{ page.previous_page.title }}</div>
          </div>
        </a>
      {% endif %}
      
      {% if page.next_page %}
        <a href="{{ page.next_page.url }}" class="md-footer-nav__link md-footer-nav__link--next">
          <div class="md-footer-nav__title">
            <span class="md-footer-nav__direction">Próxima →</span>
            <div class="md-ellipsis">{{ page.next_page.title }}</div>
          </div>
        </a>
      {% endif %}
    </div>
  </nav>
{% endblock %}
```

## Condições e Loops

### Condições

```jinja2
{% if page.is_homepage %}
  <!-- Conteúdo especial para home -->
{% elif page.meta.template == "api" %}
  <!-- Conteúdo para páginas de API -->
{% else %}
  <!-- Conteúdo padrão -->
{% endif %}
```

### Loops

```jinja2
{% for nav_item in nav %}
  {% if nav_item.is_section %}
    <div class="section">
      <h3>{{ nav_item.title }}</h3>
      {% for item in nav_item.children %}
        <a href="{{ item.url }}">{{ item.title }}</a>
      {% endfor %}
    </div>
  {% endif %}
{% endfor %}
```

## Filtros Úteis

```jinja2
{{ page.title | upper }}          # MAIÚSCULAS
{{ page.title | lower }}          # minúsculas
{{ page.title | capitalize }}     # Primeira letra maiúscula
{{ page.content | length }}       # Tamanho do conteúdo
{{ page.meta.date | default('N/A') }}  # Valor padrão
```

## Partials Reutilizáveis

Crie componentes reutilizáveis:

**`docs/overrides/partials/chaos-indicator.html`:**

```jinja2
<div class="chaos-indicator" 
     data-level="{{ level | default('medium') }}">
  <span class="pulse"></span>
  <span class="label">Chaos: {{ level | upper }}</span>
</div>
```

**Usar no template principal:**

```jinja2
{% include "partials/chaos-indicator.html" %}
```

## Macros

Crie funções reutilizáveis:

**`docs/overrides/macros.html`:**

```jinja2
{% macro render_badge(text, color) %}
  <span class="badge" style="background: {{ color }}">
    {{ text }}
  </span>
{% endmacro %}

{% macro render_card(title, content, icon) %}
  <div class="card">
    <div class="card-icon">{{ icon }}</div>
    <h3>{{ title }}</h3>
    <p>{{ content }}</p>
  </div>
{% endmacro %}
```

**Usar:**

```jinja2
{% import "macros.html" as macros %}

{{ macros.render_badge("New", "#c41e3a") }}
{{ macros.render_card("Título", "Conteúdo", "🔥") }}
```

## Debug

### Ver Variáveis Disponíveis

```jinja2
<pre>
{{ page | pprint }}
{{ config | pprint }}
{{ nav | pprint }}
</pre>
```

### Comentar Template

```jinja2
{# Isso é um comentário e não aparece no HTML #}

{# 
Comentário
multilinha
#}
```

## Best Practices

!!! tip "Dicas de Templates"
    
    1. **Sempre use `{{ super() }}`** quando estender blocos
    2. **Mantenha lógica no Python**, não no template
    3. **Use partials** para componentes reutilizáveis
    4. **Comente** templates complexos
    5. **Teste** em múltiplos navegadores

!!! warning "Cuidados"
    
    - Não coloque muita lógica nos templates
    - Evite queries complexas no template
    - Cuidado com performance em loops grandes
    - Sempre escape conteúdo do usuário

## Recursos

- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Material Theme Customization](https://squidfunk.github.io/mkdocs-material/customization/)
- [MkDocs Theming Guide](https://www.mkdocs.org/user-guide/custom-themes/)

---

<div class="ergodic-footer" markdown>

**Controle total sobre cada pixel**  
*Customize até o caos convergir em perfeição*

</div>

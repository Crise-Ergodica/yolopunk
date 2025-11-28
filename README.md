<div align="center">
<img src="docs/img/yolopunk_titulo.png" width="640" alt="YOLOPunk Logo">

###### _sǝɐ̰ɥןɐƃɐW ˙Ɔ ˙ᗡ ɐɹoɹn∀ - 5202/11/52 ǝpsǝp soʇuıɹıqɐן sop ɐsɐɔ ɐu opuɐɹʇuƎ_

![Licença: AGPL-3.0](https://img.shields.io/badge/☥_Licença-AGPL--3.0-8B0000.svg?style=for-the-badge) 
![Status](https://img.shields.io/badge/Δ_Status-Em_Construção-crimson.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/_Python-3.9+-darkred.svg?style=for-the-badge&logo=python)
![Docs](https://img.shields.io/badge/📖_Docs-MkDocs-c41e3a.svg?style=for-the-badge)
![PEP 8](https://img.shields.io/badge/code%20style-PEP%208-darkred.svg?style=for-the-badge)
![PEP 257](https://img.shields.io/badge/docstrings-PEP%20257-8B0000.svg?style=for-the-badge)
![Type Hints](https://img.shields.io/badge/type%20hints-PEP%20484-crimson.svg?style=for-the-badge)

</div>

## <img src="docs/img/pentagrama_icone.svg" width="26"> 𝔐𝔞𝔫𝔦𝔣𝔢𝔰𝔱𝔬 𝔡𝔬 ℭ𝔬𝔡𝔦𝔤𝔬
**YOLOPunk** é o anti-framework.  
O código foi escrito com o objetivo de perpetuar o formato ergodico antes do conteudo.  
Aqui, a visão da máquina é barroca, **um espaço reverso** onde não há clareira, só corredores.

- Não prometa simplicidade; abrace a carne excêntrica da complexidade.
- Documente cada paço que tiver antes que se perca.
- Não fuja daquilo que parece impossível: corrompa, inquiete, desoriente.
- Teste tudo, mas desconfie de tudo.
**Entre. Perca-se.**

---

## <img src="docs/img/pentagrama_icone.svg" width="26"> 📐 Padrões de Qualidade do Código

**YOLOPunk** segue rigorosos padrões de qualidade e legibilidade de código:

### 🌐 Idioma do Código
- **Código-fonte**: Inglês (nomes de variáveis, funções, classes, comentários)
- **Documentação de usuário**: Português (README, docs/)
- **Motivo**: Acessibilidade global e conformidade com padrões internacionais

### 📋 PEPs Seguidas

#### PEP 8 - Style Guide for Python Code
- Indentação de 4 espaços
- Linhas com máximo de 79 caracteres (código) e 72 (docstrings)
- Imports organizados: stdlib, terceiros, locais
- Nomenclatura: `snake_case` para funções/variáveis, `PascalCase` para classes
- Espaçamento consistente em operadores e after commas

#### PEP 257 - Docstring Conventions
- Docstrings obrigatórias para todos os módulos, classes e funções públicas
- Uma linha para descrições simples, múltiplas linhas para documentação detalhada
- Formato Google Style Guide para argumentos, retornos e exceções

#### PEP 484 - Type Hints
- Type hints obrigatórios em todas as assinaturas de funções
- Uso de `typing` para tipos complexos (`Optional`, `Union`, `List`, `Tuple`, etc.)
- Return types explícitos (incluindo `None`)
- Type hints para atributos de classe quando apropriado

#### Google Style Guide for Python
- Docstrings seguem formato Google:
  ```python
  def function(arg1: str, arg2: int) -> bool:
      """Brief description.

      Longer description if needed.

      Args:
          arg1: Description of arg1.
          arg2: Description of arg2.

      Returns:
          Description of return value.

      Raises:
          ValueError: Description of when this is raised.
      """
  ```

### 🔍 Ferramentas de Qualidade
- **black**: Formatação automática (quando disponível)
- **flake8**: Linting e checagem de estilo
- **mypy**: Verificação de tipos estáticos
- **pylint**: Análise de código estática

---

## <img src="docs/img/pentagrama_icone.svg" width="26">𝔊𝔯𝔦𝔪𝔬𝔯𝔦𝔬 𝔈𝔯𝔤𝔬𝔡𝔦𝔠𝔬 ᵈᵒᶜᵘᵐᵉⁿᵗᵃᶜᵃᵒ

**A documentação vive. Sangra. Converge. E pode ser [INVOCADO](https://yolopunk.github.io)**.

...ou construído localmente:

```bash
# Instale dependências
pip install -r requirements-docs.txt

# Sirva localmente com live reload
mkdocs serve

# Acesse: http://127.0.0.1:8000
```

### 📚 Estrutura do Grimório

INCOMPLETO

### 🛠️ Customização

Veja [docs/README.md](docs/README.md) para guia completo de customização.

**Quick customização CSS:**

```css
/* docs/stylesheets/custom.css */
.md-typeset h1 {
  color: var(--yp-blood-red);
  border-bottom: 2px solid var(--yp-blood-red);
}
```

**Quick customização Jinja2:**

```jinja2
<!-- docs/overrides/main.html -->
{% extends "base.html" %}

{% block content %}
  <!-- Seu conteúdo aqui -->
  {{ super() }}
{% endblock %}
```

---

## <img src="docs/img/pentagrama_icone.svg" width="26"> 𝔐𝔞𝔭𝔞 𝔡𝔢  𝙔𝙊𝙇𝙊𝙋𝙐𝙉𝙆

```plaintext
yolopunk/
│
├── yolopunk/
│   └── ...
│
├── tests/                      # IMPORTANTE: seus testes vão aqui!
│   ├── __init__.py
│   ├── test_module1.py
│   └── ...
│
├── docs/                       # Documentação MkDocs (Grimório Ergódico)
│   ├── index.md                # Página inicial
│   ├── grimorio/               # Documentação profunda
│   ├── api/                    # Referência da API
│   ├── exemplos/               # Exemplos práticos
│   ├── overrides/              # Templates Jinja2 customizados
│   ├── stylesheets/            # CSS customizado
│   ├── javascripts/            # JavaScript interativo
│   ├── README.md               # Guia da documentação
│   └── DEVELOPMENT.md          # Guia de desenvolvimento
│
├── .github/                    
│   └── ISSUE_TEMPLATE/         # Templates para 'issues'
│   └── workflows/              # Automação de CI/CD
│       ├── ci.yml
│       ├── format.yml
│       └── docs.yml            # Deploy automático da documentação
│
├── .gitignore                  # Arquivos que o Git ignora
├── LICENSE                     # Licença do projeto
├── pyproject.toml              # CRUCIAL: configurações do projeto
├── mkdocs.yml                  # Configuração do MkDocs
├── requirements-docs.txt       # Dependências da documentação
└── README.md                   # Você está aqui!
```

---

## <img src="docs/img/pentagrama_icone.svg" width="26"> 𝔓𝔯𝔦𝔪𝔢𝔦𝔯𝔬 ℭ𝔬𝔫𝔱𝔞𝔱𝔬

INCOMPLETO

---

## <img src="docs/img/pentagrama_icone.svg" width="26"> CONFIGURE O OꓕNIꓤIꓭⱯꓶ

O framework não é suave — é um _labirinto de folhas_.  
Cada parâmetro pode abrir uma porta… ou trancar você na sala errada.

Veja o arquivo `pyproject.toml` para livros de receitas proibidas.  
Exemplo de configuração:

---

## <img src="docs/img/pentagrama_icone.svg" width="26"> NOTAS

- Tudo documentado em `docs/`, mas é prudente duvidar.
- Leia tudo com uma lanterna (e um sal).
- Código amaldiçoado é melhor documentado, ou então some do repositório com ruídos.

---

## <img src="docs/img/pentagrama_icone.svg" width="26"> CONTRIBUA _ˢᵉ ᵒᵘˢᵃʳ_

Para adicionar seus próprios demônios,  
- Faça um **fork**
- Crie uma **branch** do seu ritual (`feature/aberracao`)
- Faça um commit que doa nos outros (`git commit -m '💀 feat: miragem de pose'`)
- Abra um PR. O sangue será avaliado.

Aceitamos contribuições que desafiem a razão e a sanidade. Testes são bem-vindos, e docstrings protegem dos horrores.

**Para contribuir com a documentação:**

1. Edite arquivos em `docs/`
2. Teste localmente: `mkdocs serve`
3. Commit e push - GitHub Actions faz deploy automático

**Para contribuir com código:**

1. Siga as PEPs listadas acima (PEP 8, PEP 257, PEP 484)
2. Escreva código em **inglês** (variáveis, funções, docstrings)
3. Use Google Style Guide para docstrings
4. Adicione type hints em todas as funções
5. Teste seu código antes de submeter PR

---

## <img src="docs/img/pentagrama_icone.svg" width="26">️ LICENÇA

**AGPL-3.0**: Compartilhe. Sangre. Corrompa novamente.  
O que é derramado aqui, nunca mais retorna limpo.

---

<div align="center">

## O FRAMEWORK É O LABIRINTO  
#### _Você não decifra, você se perde._

[![Bem-Vindo!](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)](https://github.com/Crise-Ergodica/yolopunk/pulls)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Documentation](https://img.shields.io/badge/docs-MkDocs-c41e3a?style=flat-square)](https://crise-ergodica.github.io/yolopunk)
[![PEP 8](https://img.shields.io/badge/code%20style-PEP%208-black?style=flat-square)](https://peps.python.org/pep-0008/)

<img src="docs/img/pentagrama_icone.svg" width="26"><img src="docs/img/pentagrama_icone.svg" width="26"><img src="docs/img/pentagrama_icone.svg" width="26">
</div>

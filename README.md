<div align="center">
<a href="https://www.ultralytics.com/"><img src="docs/img/yolopunk_titulo.png" width="640" alt="Ultralytics logo"></a>

# 🛠 yolopunk Python Project 
###### _(Em construção desde 25/11/2025, por Aurora Drumond Costa Magalhães)_
</div>
Welcome to the Ultralytics Python Project Template! This repository provides a standardized foundation for initiating Python projects at [Ultralytics](https://www.ultralytics.com/). It incorporates best practices in project structure, configuration, and essential tooling to streamline development. By using this template, Ultralytics developers can ensure consistency, maintain high quality standards, and accelerate the setup process for new Python-based software. Explore our [Ultralytics Solutions](https://www.ultralytics.com/solutions) to see how we apply these standards in real-world applications.

[![Template CI](https://github.com/ultralytics/template/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/template/actions/workflows/ci.yml)
[![Ultralytics Actions](https://github.com/ultralytics/template/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/template/actions/workflows/format.yml)
[![codecov](https://codecov.io/gh/ultralytics/template/graph/badge.svg?token=K9IunpFzjS)](https://codecov.io/gh/ultralytics/template)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

## 🗂️ Repository Structure

This template is meticulously organized for intuitive navigation and a clear understanding of project components. Familiarize yourself with the [Python project structure best practices](https://realpython.com/python-application-layouts/) to make the most of this layout.
- `yolopunk/`: Contains the core source code of your Python package, organized into modules. Using a `src` layout is a common practice detailed in [Python packaging guides](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata).
- `tests/`: Dedicated directory for unit tests and integration tests, crucial for implementing [continuous testing](https://docs.ultralytics.com/help/CI/) practices. Consider using frameworks like [pytest](https://docs.pytest.org/en/stable/) for writing tests.
- `docs/`: (Optional) Houses project documentation. Tools like [MkDocs](https://www.mkdocs.org/) can be used to generate comprehensive documentation from this directory.
- `pyproject.toml`: The standard configuration file for Python projects, detailing dependencies, build system requirements, formatting rules, and packaging information as specified by [PEP 518](https://peps.python.org/pep-0518/) and subsequent PEPs.
- `.gitignore`: Configured to exclude unnecessary files (like `*.pyc` or virtual environment directories) from [Git](https://git-scm.com/) tracking.
- `LICENSE`: Specifies the open-source license (defaulting to AGPL-3.0) under which the project is released.
- `.github/workflows/`: Contains [GitHub Actions](https://docs.github.com/en/actions) workflows for automating Continuous Integration and Continuous Deployment (CI/CD) processes. Learn more about [CI/CD concepts](https://www.redhat.com/en/topics/devops/what-is-ci-cd).

```plaintext
your-project/
│
├── yolopunk/
│   └── ...
│
├── tests/                      # IMPORTANTE: seus testes vão aqui!
│   ├── __init__.py
│   ├── test_module1.py
│   └── ...
│
├── docs/                       # Sua documentação MkDocs
│   └── ...
│
├── .github/                    
│   └── ISSUE_TEMPLATE/         # Templates para 'issues'
│   └── workflows/              # Automação de CI/CD
│       ├── ci.yml
|       └── format.yml
│
├── .gitignore                  # Arquivos que o Git ignora
├── LICENSE                     # Licença do projeto
├── pyproject.toml              # CRUCIAL: configurações do projeto
└── README.md                   # Você está aqui!
```


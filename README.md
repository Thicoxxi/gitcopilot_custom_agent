# 🚀 DevOps Specialist — Pipeline Generator

Este projeto combina um agente para o GitHub Copilot com um backend em Python utilizando a API da Groq para gerar, revisar e otimizar pipelines CI/CD para:

- GitLab CI
- GitHub Actions

O objetivo é facilitar a criação de workflows padronizados, revisar pipelines existentes e fornecer templates reutilizáveis para diferentes linguagens e cenários.

---

# 📂 Estrutura do Projeto

```text
.github/
├── agents/
│   └── devops-specialist.agent.md
│       # Manifesto do agente Copilot
│
├── prompts/
│   # Exemplos de prompts de uso
│
├── templates/
│   # Templates genéricos de pipelines
│
├── scripts/
│   ├── generate_pipeline.py
│   │   # Gerador de pipelines integrado ao Copilot e backend Groq
│   │
│   └── groq_backend.py
│       # Backend Python integrado à API da Groq
│
├── examples/
│   # Exemplos de pipelines gerados
│
└── docs/
    # Documentação adicional
```

---

# 🤖 Uso com GitHub Copilot Agent

O arquivo `devops-specialist.agent.md` define o agente:

> **DevOps Specialist — Pipeline Generator**

Ele pode ser utilizado diretamente no Copilot Chat dentro do VS Code.

---

# ✨ Capacidades do Agente

- Criar pipelines novos para GitHub Actions e GitLab CI
- Analisar pipelines existentes
- Sugerir melhorias de:
  - Performance
  - Segurança
  - Boas práticas
- Gerar templates reutilizáveis
- Suportar múltiplas linguagens e cenários

---

# 💬 Exemplos de Prompts

## GitLab CI — Node.js

```text
Gere um pipeline GitLab CI para um projeto Node.js
que rode testes com Jest e faça build de uma imagem Docker.
```

## GitHub Actions — Python

```text
Gere um workflow GitHub Actions para um projeto Python
que execute pytest e publique um pacote em PyPI em tags.
```

## Revisão de Pipeline

```text
Analise este pipeline GitLab CI e sugira melhorias,
retornando apenas o YAML otimizado.
```

## Template Reutilizável

```text
Crie um template de pipeline GitLab CI
para projetos Java com Maven e testes JUnit.
```

---

# ⚙️ Uso do Backend Groq em Python

O script `groq_backend.py` permite gerar ou revisar pipelines diretamente via terminal utilizando a API da Groq.

---

# 📦 Instalação

## 1. Crie um arquivo `.env`

Na raiz do projeto:

```env
GROQ_API_KEY=seu_token_aqui
```

---

## 2. Instale as dependências

```bash
pip install python-dotenv openai
```

---

# 🖥️ Comandos

## Gerar novo pipeline GitHub Actions

```bash
python .github/scripts/groq_backend.py \
"Gere um workflow GitHub Actions para projeto Python com pytest e deploy no PyPI"
```

---

## Gerar pipeline GitLab CI

```bash
python .github/scripts/groq_backend.py \
"Gere um pipeline GitLab CI para Node.js com Jest e Docker"
```

---

## Revisar pipeline existente

```bash
python .github/scripts/groq_backend.py \
"revise este pipeline" meu-pipeline.yml
```

---

## Criar template reutilizável

```bash
python .github/scripts/groq_backend.py \
"Crie um template GitLab CI genérico para projetos Java com Maven e JUnit"
```

---

# 📌 Boas Práticas

- Sempre solicite saída somente em YAML
- Evite explicações adicionais ao gerar pipelines
- Preserve a estrutura original ao revisar pipelines
- Aplique boas práticas de:
  - Segurança
  - Performance
  - Reutilização
- Utilize templates genéricos e reutilizáveis
- Siga padrões recomendados do GitLab e GitHub

---

# 🎯 Objetivo

Unir a praticidade do GitHub Copilot Agent com a flexibilidade do backend Groq em Python para permitir:

- ⚡ Criação rápida de pipelines CI/CD
- 🔍 Revisão e otimização de pipelines existentes
- 📦 Padronização via templates reutilizáveis
- 🤖 Automação inteligente com IA

---

# 🛠️ Tecnologias Utilizadas

- Python
- Groq API
- GitHub Copilot
- GitHub Actions
- GitLab CI/CD
- YAML

---

# 📄 Licença

Este projeto pode ser adaptado conforme as necessidades da sua organização ou fluxo DevOps.
# DevOps Specialist — Pipeline Generator

Este projeto combina um **GitHub Copilot Agent** com um **backend em Python (Groq)** para gerar, otimizar e sugerir melhorias em pipelines CI/CD para **GitLab CI** e **GitHub Actions**.  
O objetivo é facilitar a criação de workflows padronizados, revisar pipelines existentes e fornecer **templates reutilizáveis** para diferentes linguagens e cenários.

---

## 📂 Estrutura do Projeto

.github/
 ├── agents/
 │    └── devops-specialist.agent.md   # Manifesto do agente Copilot
 ├── prompts/                          # Exemplos de prompts de uso
 ├── templates/                        # Templates genéricos de pipelines
 ├── scripts/
 |    └── generate_pipeline.py         # Gerador de pipelines em python integrado com copilot e Groq backend 
 │    └── groq_backend.py              # Backend Python integrado ao Groq
 ├── examples/                         # Exemplos de pipelines gerados
 └── docs/                             # Documentação adicional

---

## 🚀 Uso com GitHub Copilot Agent

O arquivo `devops-specialist.agent.md` define o agente **DevOps Specialist — Pipeline Generator**.  
Ele pode ser chamado diretamente no **Copilot Chat** dentro do VS Code.

### Capacidades do agente
- Criar pipelines novos para GitHub Actions e GitLab CI.  
- Analisar pipelines existentes e sugerir melhorias de performance, segurança e boas práticas.  
- Gerar templates reutilizáveis para diferentes linguagens e cenários.  

### Exemplos de prompt
- Gere um pipeline GitLab CI para um projeto Node.js que rode testes com Jest e faça build de uma imagem Docker.  
- Gere um workflow GitHub Actions para um projeto Python que execute pytest e publique um pacote em PyPI em tags.  
- Analise este pipeline GitLab CI e sugira melhorias, retornando apenas o YAML otimizado.  
- Crie um template de pipeline GitLab CI para projetos Java com Maven e testes JUnit.  

---

## ⚙️ Uso do Backend Groq em Python

O script `groq_backend.py` permite gerar ou revisar pipelines diretamente via terminal, usando a API da Groq.

### Instalação
1. Crie um arquivo `.env` na raiz com sua chave:  
   GROQ_API_KEY=seu_token_aqui

2. Instale dependências:  
   pip install python-dotenv openai

### Comandos

- Gerar novo pipeline GitHub Actions  
  python .github/scripts/groq_backend.py "Gere um workflow GitHub Actions para projeto Python com pytest e deploy no PyPI"

- Gerar pipeline GitLab CI  
  python .github/scripts/groq_backend.py "Gere um pipeline GitLab CI para Node.js com Jest e Docker"

- Revisar pipeline existente  
  python .github/scripts/groq_backend.py "revise este pipeline" meu-pipeline.yml

- Criar template reutilizável  
  python .github/scripts/groq_backend.py "Crie um template GitLab CI genérico para projetos Java com Maven e JUnit"

---

## 📌 Boas práticas

- Sempre peça saída somente em YAML, sem explicações adicionais.  
- Ao revisar pipelines, preserve a estrutura original e aplique boas práticas.  
- Templates devem ser genéricos e reutilizáveis, seguindo padrões recomendados (ex: Instance Template Repository do GitLab).  

---

## ✨ Objetivo

Unir a praticidade do **GitHub Copilot Agent** com a flexibilidade do **backend Groq em Python**, permitindo:  
- Criação rápida de pipelines CI/CD.  
- Revisão e otimização de pipelines existentes.  
- Padronização via templates reutilizáveis.  

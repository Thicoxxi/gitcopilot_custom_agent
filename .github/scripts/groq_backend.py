import os
import sys
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("A chave GROQ_API_KEY não foi encontrada no .env")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def clean_yaml(content: str) -> str:
    # Remove blocos de código markdown
    content = re.sub(r"^```(?:yaml|yml)?\s*", "", content, flags=re.IGNORECASE | re.MULTILINE)
    content = re.sub(r"```$", "", content.strip(), flags=re.MULTILINE)
    return content.strip()

def call_groq(prompt: str, model: str = "llama-3.3-70b-versatile"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um agente DevOps especialista em CI/CD. "
                    "Sua função é: (1) gerar pipelines novos, (2) revisar pipelines existentes sugerindo melhorias "
                    "de performance, segurança e boas práticas, e (3) criar templates reutilizáveis para diferentes linguagens. "
                    "Sempre responda apenas com YAML válido, sem explicações fora do código."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )
    return clean_yaml(response.choices[0].message.content)

def detect_target(prompt: str, yaml_output: str) -> str:
    lower_prompt = prompt.lower()
    if "gitlab" in lower_prompt or "stages:" in yaml_output:
        return ".gitlab-ci.yml"
    elif "github" in lower_prompt or "jobs:" in yaml_output or "runs-on:" in yaml_output:
        return os.path.join(".github", "workflows", "generated.yml")
    else:
        return "pipeline.yml"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python groq_backend.py \"seu prompt aqui\" [arquivo_existente.yml]")
    else:
        prompt = sys.argv[1]

        # Se o usuário passar um arquivo existente, vamos revisar
        if len(sys.argv) == 3 and os.path.isfile(sys.argv[2]):
            with open(sys.argv[2], "r", encoding="utf-8") as f:
                existing_pipeline = f.read()
            prompt = f"Analise e sugira melhorias para este pipeline:\n{existing_pipeline}"

        yaml_output = call_groq(prompt)
        filename = detect_target(prompt, yaml_output)

        # Cria pastas se necessário
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(yaml_output)

        print(f"Arquivo gerado: {filename} ({len(yaml_output.splitlines())} linhas)")
        os.system(f"code {filename}")

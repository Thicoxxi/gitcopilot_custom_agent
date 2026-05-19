# Exemplo de uso

Gerar um pipeline GitLab para Node.js:

```bash
python scripts/generate_pipeline.py --platform gitlab --language node --build-cmd "npm ci && npm run build" --test-cmd "npm test" --image node:18 --deploy-cmd "echo deploy" --deploy-branch main
```

Gerar um workflow GitHub Actions para Python:

```bash
python scripts/generate_pipeline.py --platform github --language python --build-cmd "pip install -r requirements.txt" --test-cmd "pytest -q" --image python:3.11 --deploy-branch main
```

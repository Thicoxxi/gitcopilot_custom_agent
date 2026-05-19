#!/usr/bin/env python3
"""
Gera pipeline YAML simples para GitLab CI ou GitHub Actions a partir de parâmetros.
Uso: python scripts/generate_pipeline.py --platform gitlab --language node --build-cmd "npm run build" --test-cmd "npm test" --image node:18 --deploy-branch main
"""
import argparse
from pathlib import Path

TEMPLATES = {
    'gitlab': Path(__file__).resolve().parents[1] / 'templates' / 'gitlab-ci.yml.tmpl',
    'github': Path(__file__).resolve().parents[1] / 'templates' / 'github-actions.yml.tmpl',
}

def load_template(path: Path) -> str:
    return path.read_text(encoding='utf-8')

def render(template: str, ctx: dict) -> str:
    return template.format(**ctx)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--platform', choices=['gitlab','github'], required=True)
    p.add_argument('--language', default='unknown')
    p.add_argument('--build-cmd', default='echo build')
    p.add_argument('--test-cmd', default='echo test')
    p.add_argument('--deploy-cmd', default='echo deploy')
    p.add_argument('--image', default='python:3.11')
    p.add_argument('--deploy-branch', default='main')
    p.add_argument('--env', default='production')
    p.add_argument('--output', help='Arquivo de saída (padrão stdout)')
    args = p.parse_args()

    tpl_path = TEMPLATES['gitlab' if args.platform == 'gitlab' else 'github']
    template = load_template(tpl_path)

    ctx = {
        'language': args.language,
        'build_command': args.build_cmd,
        'test_command': args.test_cmd,
        'deploy_command': args.deploy_cmd,
        'image': args.image,
        'deploy_branch': args.deploy_branch,
        'env': args.env,
    }

    out = render(template, ctx)

    if args.output:
        Path(args.output).write_text(out, encoding='utf-8')
        print(f'Gerado: {args.output}')
    else:
        print(out)

if __name__ == '__main__':
    main()

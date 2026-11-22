# Auditoria — ETL-com-Python — 2026-11-22

## Estado anterior
- O repositório tinha só `README.md` e `project-bolt-sb1-xbwv6slq.zip` (export do Bolt). Todo o código estava dentro do zip.
- Sem CI (`gh run list` vazio). README descrevia um ETL REST→banco, mas o ponto de entrada é um dashboard Dash do Ibovespa.

## Problemas encontrados

| # | Sev. | Problema | Evidência |
|---|---|---|---|
| 1 | P0 | Dependências não instalam em Python 3.12 (`numpy==1.24.0` exige `distutils`) | `uv pip install -r requirements.txt` falhou na build do numpy |
| 2 | P0 | Dependências vulneráveis: `requests 2.31.0` (3 avisos), `python-dotenv 1.0.0` (1), `dash 2.14.0` (1) | `pip-audit -r requirements.txt` original: 9 linhas / 3 pacotes |
| 3 | P0 | Aplicação não inicia: `python src/main.py` → `ImportError: attempted relative import beyond top-level package`; sem `__init__.py` | execução real |
| 4 | P1 | `ibovespa_dashboard.py` usa `dcc.Interval` sem importar `dcc` → `NameError` | teste `test_dashboard_monta_layout_e_metodo_run` antes da correção |
| 5 | P1 | `app.run_server` não existe no Dash ≥ 3 | código + Dash 4.5.1 |
| 6 | P1 | **Fonte de dados fora do ar**: endpoints InfoMoney retornam HTTP 404 | `curl` e log real do dashboard: `404 Client Error: Not Found` |
| 7 | P2 | `requests.get` sem timeout (pode travar indefinidamente) | leitura do código |
| 8 | P2 | `debug=True` fixo no servidor (debugger do Werkzeug/Dash exposto) | `src/main.py` |
| 9 | P2 | `sqlalchemy` usado mas ausente do requirements; `dash-bootstrap-components` listado e nunca usado | grep |
| 10 | P3 | Arquivos do template Node (index.js "Hello Node", package.json) sem relação com o projeto | conteúdo do zip |

Segredos: nenhum. `.env.example` e README só têm placeholders (`your_api_key_here`, `user:password@localhost`).
Busca por regex em todo o histórico e no conteúdo do zip (gitleaks não instalado).

## Mudanças
- Código extraído do zip para `src/`, `tests/`, `requirements.txt`, `.env.example`; zip removido da árvore (permanece no histórico). Template Node não foi trazido.
- Pacotes Python (`__init__.py`), imports relativos em `main.py`, `dcc` importado, `app.run`, timeout nas requisições, debug via `DASH_DEBUG`.
- Imports não usados removidos (ruff).
- `requirements.txt` com versões atuais fixadas e testadas (sem vulnerabilidades conhecidas), `requirements-dev.txt`, `ruff.toml`, `.gitignore`.
- Novos testes `tests/test_dashboard.py` (4) além dos 5 existentes; CI (ruff, compileall, pytest; `contents: read`; actions por SHA).
- README e `.env.example` reescritos.

## Testes executados (Windows, Python 3.12)
- Antes (após atualizar deps para conseguir instalar): `pytest -q tests` → 2 failed (ModuleNotFoundError `dashboard`, NameError `dcc`), 2 passed nos novos; os 5 originais passavam.
- Depois: `pytest -q tests` → **9 passed**; `ruff check .` OK; `pip-audit -r requirements.txt` → sem vulnerabilidades.
- Execução real: `python -m src.main` sobe em http://127.0.0.1:8050 (GET / → 200). O callback de atualização responde "Error loading data" porque a API retorna 404.

## Riscos residuais / decisões do dono
- **Sem fonte de dados funcional.** Escolher outra fonte (gratuita, com termos de uso compatíveis) é decisão de negócio; não foi implementada.
- Os módulos `api_client`/`transformer`/`database` não estão integrados ao fluxo principal.
- Atualização major de dependências (pandas 3, numpy 2, Dash 4): coberta pelos testes, mas o dashboard real não pôde ser visto com dados.
- Sem arquivo LICENSE.

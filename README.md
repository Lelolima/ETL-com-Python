# ETL com Python — Dashboard Ibovespa

Dashboard Dash que busca a cotação do Ibovespa, transforma em DataFrame e exibe estatísticas e gráficos com
atualização periódica. O repositório também traz módulos ETL genéricos (cliente REST com API key, transformador
pandas e carregador SQLAlchemy) que **não estão ligados ao dashboard**.

> ⚠️ **Fonte de dados indisponível (verificado em 2026-11-22):** o endpoint
> `https://www.infomoney.com.br/wp-json/infomoney/v1/cotacoes/ibovespa` (e o de bitcoin) responde **HTTP 404**.
> O dashboard abre, mas mostra "Error loading data". Trocar a fonte é decisão do dono do projeto.

Até 2026-11-22 o código estava só dentro de um `.zip` gerado pelo Bolt; ele foi extraído para a árvore do
repositório (o zip continua disponível no histórico do git).

## Estrutura

```
src/
├── main.py                     # ponto de entrada (python -m src.main)
├── config/settings.py          # URLs, timeout, intervalo de atualização, cores
├── dashboard/                  # app Dash + componentes (gráficos e estatísticas)
├── extract/                    # ibovespa_client, infomoney_client (bitcoin), api_client (genérico, exige API_KEY)
├── transform/                  # transformadores Ibovespa, Bitcoin e genérico
├── load/database.py            # carga via SQLAlchemy (exige DB_CONNECTION)
└── utils/                      # logger, cache em memória, estatísticas
tests/                          # pytest/unittest
```

## Instalação

Python 3.10+ (testado com 3.12).

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt          # execução
pip install -r requirements-dev.txt      # + testes e lint
```

## Execução

```bash
python -m src.main
```

Abre o servidor em http://127.0.0.1:8050 (atualização a cada 60 s).

## Variáveis de ambiente

Veja `.env.example` (sem valores reais). `API_KEY` e `DB_CONNECTION` só são exigidas por `APIClient` e
`DatabaseLoader`; o dashboard não as usa. `DASH_DEBUG=1` liga o modo debug do Dash.

## Testes e lint

```bash
ruff check .
pytest -q tests
```

Os testes não acessam a rede (o cliente HTTP é substituído por `patch` onde necessário). CI em
`.github/workflows/ci.yml`.

## Licença

Não há arquivo `LICENSE` no repositório (o README antigo citava MIT).

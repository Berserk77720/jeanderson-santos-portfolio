# Laboratórios e ferramentas de demonstração

Os scripts abaixo são **projetos de referência produzidos para compor o repositório**. Não representam entrega contratual, pentest real ou experiência anterior do titular. Todos utilizam dados de exemplo ou operações locais.

| Projeto | Finalidade | Como executar |
|---|---|---|
| `infra-health` | Verificação local de espaço em disco e resolução de DNS | `python projects/infra-health/healthcheck.py --host example.com --path .` |
| `incident-insights` | Consolidação de incidentes fictícios em CSV | `python projects/incident-insights/analyze.py` |
| `backup-integrity` | Gerar e validar manifesto SHA-256 | `python projects/backup-integrity/integrity.py --help` |
| `security-headers` | Revisão offline de cabeçalhos HTTP | `python projects/security-headers/review.py` |

## Qualidade de código
Execute na raiz: `python -m unittest discover -s tests -v`. Nenhuma dependência externa é necessária para os exercícios.

## Uso responsável
Não execute testes ou coleta de informações em sistemas de terceiros sem autorização. Valores, logs e exemplos são sintéticos.

# 🛰️ Postman API Platform Blueprint — Capital Intelligence System

> **Versão:** 1.0 · **Data:** 2026-10-31  
> **Repositório:** `compilatorum/claude-para-investidores`  
> **Tipo:** blueprint de API, contrato OpenAPI, arquitetura de Collections, Environments, Mock Servers, Flows, Monitors, testes, documentação e automação Postman.  
> **Integração:** WebApp 17 abas · Scripts Python · Skills · Plano de Upgrade I · Plano de Upgrade II · Meta-Prompt Template Chain.  
> **Objetivo:** transformar os recursos do repositório em uma plataforma API-first, testável e interoperável, que possa ser modelada, simulada, documentada e posteriormente implementada usando o ecossistema Postman.  
> **Limite de escopo:** este documento especifica o desenho e o plano de implantação. Não afirma que uma API já exista, não cria endpoints operacionais por si só e não substitui a implementação de backend, autenticação, persistência, cálculos ou controles de segurança.

---

## 0. Tese central — do arsenal local a uma plataforma interoperável

O repositório já reúne uma interface WebApp, prompts, Skills, scripts quantitativos, dados sintéticos, testes E2E e documentos de arquitetura. O próximo passo arquitetural é expor capacidades como **contratos de serviço**, sem acoplar a lógica de domínio a um fornecedor de IA, a uma interface específica ou ao próprio Postman.

[
\boxed{
\text{Capital Intelligence Platform}
=
\text{API Contracts}
+ \text{Domain Services}
+ \text{Agent Workflows}
+ \text{Data & Evidence}
+ \text{Evaluation Harness}
+ \text{Governance}
}
]

**Filosofema:** *A interface conversa com o usuário; a API conversa com o ecossistema. O contrato permite que ambas evoluam sem se confundirem.*

### 0.1 O que o Postman será — e o que não será

| Papel | Postman | Sistema do repositório |
|---|---|---|
| Definir contrato | OpenAPI/API Builder e documentação | Especificação canônica versionada |
| Agrupar operações | Collections e folders | Serviços e casos de uso |
| Simular backend | Mock Servers e Examples | Fixtures e contratos de resposta |
| Orquestrar integrações | Postman Flows | Workflows de domínio e agentes |
| Validar comportamento | Scripts, tests, Runner, CLI | Testes unitários, integração, E2E e evals |
| Monitorar disponibilidade | Monitors | Observabilidade e SLOs do serviço |
| Gerenciar configuração | Environments e variables | Configuração por ambiente |
| Compartilhar conhecimento | Documentation e Workspaces | README, ADRs, Skills e Org |
| Implementar lógica de negócio | Não é sua função principal | Python/backend/serviços reais |
| Persistir dados financeiros | Não presumir Postman como banco | Banco/arquivos sob governança |
| Executar modelos/agentes | Pode chamar provedores externos | Runtime adapters e orquestrador |

**Princípio:** Postman é a bancada de contrato, integração, simulação e teste. A fonte de verdade do domínio continua no Git e na implementação do projeto.

---

## 1. Objetivos e critérios de sucesso

### 1.1 Objetivos

1. Expor operações do sistema com contratos previsíveis.
2. Permitir testar a API antes de existir backend, por meio de mocks.
3. Criar Collections organizadas por domínio e fluxo de trabalho.
4. Encadear operações com Postman Flows, sem transformar Flow em substituto de backend.
5. Validar schemas, status HTTP, invariantes e erros.
6. Separar ambientes local, mock, staging e produção.
7. Registrar exemplos, documentação, variáveis e dependências.
8. Automatizar execução em CI com Postman CLI/Newman quando compatível com a configuração adotada.
9. Preservar segurança: nenhum segredo em Git, exemplos públicos ou logs.
10. Preparar integração futura com Claude, Pi Agentic Coder, ChatGPT/Codex, Gemini, agentes locais, MCP e ferramentas externas.

### 1.2 Critérios de aceite do primeiro release

- OpenAPI válido e versionado.
- Collections importáveis e organizadas.
- Pelo menos um Mock Server utilizável sem backend.
- Examples para respostas de sucesso e erro.
- Testes de contrato para endpoints prioritários.
- Environments sem credenciais reais.
- Flows demonstrativos com tratamento de falhas.
- Documentação com limites explícitos entre mock e implementação real.
- Execução repetível por CLI/CI, com relatório.
- Dados financeiros e pessoais sintéticos nos exemplos.

---

## 2. Arquitetura lógica

### 2.1 Diagrama de contexto

```text
[WebApp / Emacs Org / CLI / Agents / External Clients]
                         |
                         v
                 [API Gateway / BFF]
                         |
       +-----------------+------------------+
       |                 |                  |
       v                 v                  v
 [Research API]    [Portfolio API]    [Workflow API]
       |                 |                  |
       +-----------------+------------------+
                         |
                [Domain / Application Layer]
                         |
       +-----------------+------------------+
       |                 |                  |
       v                 v                  v
 [Data & Sources] [Quant Engine] [Agent Runtime Adapters]
       |                 |                  |
       +-----------------+------------------+
                         |
               [Validation / Harness]
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
   [Audit Log]       [Artifacts]      [Decision Journal]

Postman: contract design + Collections + Mocks + Examples
         + Flows + Tests + Monitors + Documentation + CI
```

O diagrama é conceitual. Não implica que Gateway, banco, serviços ou runtimes estejam implementados.

### 2.2 Camadas e responsabilidades

| Camada | Responsabilidade | Contrato principal |
|---|---|---|
| L0 — API Edge | HTTP, versionamento, autenticação, rate limits | OpenAPI |
| L1 — Application | Casos de uso e orquestração | Request/response DTOs |
| L2 — Domain | Teses, portfólio, fontes, experimentos, capital | Entidades e regras |
| L3 — Data | Ingestão, normalização, proveniência | Data contracts |
| L4 — Quant | Cálculos determinísticos e modelos | Inputs/outputs numéricos |
| L5 — AI/Agents | Planejamento, geração, crítica e síntese | Task Contract |
| L6 — Evaluation | Schemas, invariantes, testes e red team | Evaluation contract |
| L7 — Persistence | Estado, histórico, arquivos e eventos | Repository interfaces |
| L8 — Observability | Logs, traces, métricas, custos | Event schema |
| L9 — Governance | Consentimento, permissões e aprovação | Policy contract |

### 2.3 Estilo de API

- HTTP REST/JSON como primeira interface interoperável.
- OpenAPI 3.x como contrato legível por humanos e máquinas.
- JSON Schema para validação de payloads.
- Identificadores estáveis e versionados.
- Paginação, filtros, ordenação e idempotência quando aplicáveis.
- Datas em ISO 8601 com timezone explícito.
- Valores monetários como decimal string ou representação decimal definida, nunca float binário sem política explícita.
- Unidades e moedas sempre declaradas.
- Erros em envelope uniforme.
- API versionada por prefixo, inicialmente `/api/v1`.
- Webhooks/eventos apenas quando houver necessidade real de integração assíncrona.

Não adotar GraphQL, gRPC, event sourcing ou microserviços distribuídos por antecipação. Começar com um modular monolith ou serviços pequenos com fronteiras claras; separar fisicamente apenas quando houver pressão operacional demonstrável.

---

## 3. Domínios e recursos da API

Os nomes abaixo são propostas de design, não endpoints existentes.

### 3.1 Mapa de recursos

| Domínio | Recurso | Finalidade | Prioridade |
|---|---|---|---|
| Health | `/health`, `/ready` | Liveness/readiness | P0 |
| API metadata | `/api/v1/capabilities` | Descobrir capacidades e versões | P0 |
| Data intake | `/api/v1/ingestions` | Submeter arquivos/datasets | P1 |
| Data quality | `/api/v1/data-quality/reports` | Relatórios de validação | P1 |
| Sources | `/api/v1/sources` | Cadastro e proveniência de fontes | P1 |
| Portfolios | `/api/v1/portfolios` | Carteiras fornecidas explicitamente | P1 |
| Portfolio analysis | `/api/v1/portfolio-analyses` | Exposição, concentração e raio-X | P1 |
| Theses | `/api/v1/theses` | Biblioteca de teses e status epistêmico | P1 |
| Research | `/api/v1/research-runs` | Execuções de pesquisa | P1 |
| Valuation | `/api/v1/valuations` | DCF, comparáveis e cenários | P2 |
| Quant | `/api/v1/quant-experiments` | Experimentos reproduzíveis | P2 |
| Workflows | `/api/v1/workflows` | Cadeias e estados de execução | P1 |
| Tasks | `/api/v1/tasks` | Contratos e execução de tarefas | P1 |
| Agents | `/api/v1/agent-runs` | Execuções de adapters/agentes | P2 |
| Evaluations | `/api/v1/evaluations` | Testes, evals e resultados | P1 |
| Artifacts | `/api/v1/artifacts` | Relatórios e arquivos produzidos | P1 |
| Decisions | `/api/v1/decisions` | Diário de decisões e revisões | P2 |
| Grants/opportunities | `/api/v1/opportunities` | Oportunidades de capital não limitado a ativos | P2 |
| Audit | `/api/v1/audit-events` | Trilha de auditoria | P1 |

### 3.2 Convenções de recursos

- Coleções: `GET /resources`, `POST /resources`.
- Item: `GET /resources/{id}`, `PATCH /resources/{id}`.
- Exclusão: preferir arquivamento lógico quando histórico e auditoria importarem.
- Execuções longas: `POST` cria job e retorna `202 Accepted` + `run_id`; `GET` consulta estado.
- Cancelamento: `POST /runs/{id}/cancel`, se houver suporte real.
- Artefatos: metadados via API; conteúdo binário por URL temporária ou endpoint controlado.
- Idempotência: `Idempotency-Key` em submissões que possam ser repetidas.
- Concorrência: `ETag`/If-Match ou versão do recurso quando houver edição concorrente.

### 3.3 Exemplo de envelope de sucesso

```json
{
  "data": {
    "id": "run_demo_001",
    "type": "research_run",
    "status": "queued"
  },
  "meta": {
    "request_id": "req_demo_001",
    "api_version": "v1",
    "synthetic": true
  },
  "links": {
    "self": "/api/v1/research-runs/run_demo_001"
  }
}
```

### 3.4 Exemplo de envelope de erro

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "O payload não atende ao contrato.",
    "details": [
      {
        "field": "as_of",
        "issue": "timezone_required"
      }
    ]
  },
  "meta": {
    "request_id": "req_demo_002",
    "api_version": "v1"
  }
}
```

### 3.5 Estados canônicos de execução

`draft` → `queued` → `running` → `validating` → `succeeded`

Estados alternativos: `needs_approval`, `partial`, `failed`, `cancelled`, `expired`.

Não representar `partial` como sucesso integral. Cada transição deve ter evento, timestamp, motivo e ator.

---

## 4. Contratos de domínio

### 4.1 Thesis

Campos mínimos sugeridos:

- `thesis_id`, `title`, `domain`, `hypothesis`, `mechanism`;
- `epistemic_status`: `DECLARED_INTEREST`, `RESEARCH_HYPOTHESIS`, `PRELIMINARY_EVIDENCE`, `VALIDATING`, `CORROBORATED`, `REFUTED`, `OBSERVING`, `NOT_ASSESSED`;
- `indicators[]`, `risks[]`, `falsifiers[]`;
- `sources[]`, `updated_at`, `version`.

Uma tese não deve receber status corroborado apenas porque um agente produziu uma narrativa convincente.

### 4.2 Evidence / Source

Cada evidência deve preservar:

- `evidence_id`, `source_id`, `source_type`;
- URL ou identificador documental quando permitido;
- autor/entidade, data de publicação e data de acesso;
- trecho/localizador: página, seção, tabela, célula ou timestamp;
- hash do arquivo quando disponível;
- afirmação suportada e escopo;
- classificação: `FACT`, `INFERENCE`, `HYPOTHESIS`, `OPINION`, `ASSUMPTION`, `SYNTHETIC`, `UNKNOWN`, `STALE`, `CONFLICTING`.

### 4.3 Portfolio / Position

- Não criar carteiras reais por inferência de perfil ou conversas.
- Cada carteira precisa de origem, titularidade declarada, data-base, moeda-base e consentimento.
- Posição: instrumento, identificador, quantidade, preço, moeda, valor, timestamp, custodiante opcional e fonte.
- Diferenciar dado observado, calculado, estimado e ausente.
- Não expor PII em mock público nem em exemplos compartilhados.

### 4.4 Task / Workflow

A API deve alinhar-se ao Meta-Prompt Template Chain:

- `task_id`, `contract_version`, `intent`, `domain`;
- `inputs[]`, `context_refs[]`, `tools_allowed[]`, `tools_forbidden[]`;
- `procedure[]`, `output_schema`, `quality_gates[]`;
- `risk_policy`, `autonomy_level`, `stop_conditions[]`;
- `approval_required`, `status`, `artifacts[]`, `validation[]`.

### 4.5 Artifact

- `artifact_id`, `artifact_type`, `format`, `uri` ou `content_ref`;
- `created_at`, `created_by`, `run_id`, `source_refs[]`;
- `checksum`, `sensitivity`, `synthetic`, `retention_policy`.

---

## 5. Postman Workspace e Collections

### 5.1 Workspace recomendado

Criar um workspace com nome como **Capital Intelligence API Lab**. Separar acesso e dados conforme sensibilidade; não misturar ambiente de demonstração público com carteiras, credenciais ou documentos privados.

### 5.2 Collections propostas

| Collection | Conteúdo | Pasta / requests |
|---|---|---|
| `00 — Platform & Health` | Descoberta e saúde | Health, Ready, Capabilities |
| `01 — Data Intake & Sources` | Ingestão e proveniência | Create ingestion, Get status, List sources |
| `02 — Portfolio Intelligence` | Raio-X e exposição | Create portfolio, Analyze, Get report |
| `03 — Thesis & Research` | Teses e pesquisas | Create thesis, Update status, Run research |
| `04 — Quant & Valuation` | Cálculo e experimentos | DCF, comps, quant experiment, results |
| `05 — Prompt Chains & Agents` | Tasks, workflows e agents | Validate task, Run workflow, Poll run |
| `06 — Evaluation & Red Team` | Harness e qualidade | Schema checks, evaluation run, findings |
| `07 — Artifacts & Decisions` | Entregáveis e decisão | List artifacts, fetch metadata, log decision |
| `08 — Opportunities & Grants` | Oportunidades de capital | Intake, scorecard, compare |
| `90 — Error & Security Cases` | Negativos e abuso | 400, 401, 403, 404, 409, 413, 422, 429 |
| `99 — End-to-End Journeys` | Jornadas completas | Synthetic thesis update, portfolio diagnostic |

**Regra de organização:** uma Collection deve representar uma fronteira de domínio ou uma jornada claramente identificável; não criar uma coleção por endpoint.

### 5.3 Naming convention

- Collections: `CI — <Domain>`.
- Folders: `<NN> — <Capability>`.
- Requests: verbo + objeto, ex. `POST — Create Research Run`.
- Variables: `baseUrl`, `apiVersion`, `requestId`, `runId`.
- Test names: `[CONTRACT]`, `[SCHEMA]`, `[SECURITY]`, `[INVARIANT]`, `[FLOW]`.
- Tags/documentation: domínio, prioridade, risco, estado (`mock`, `implemented`, `deprecated`).

---

## 6. Environments e variáveis

### 6.1 Environments

| Environment | Base URL | Uso |
|---|---|---|
| `Local` | `http://localhost:<port>` | Backend local |
| `Mock` | URL do Mock Server | Contrato sem backend |
| `Development` | URL de desenvolvimento | Integração de equipe |
| `Staging` | URL de homologação | Pré-produção |
| `Production` | URL de produção | Operação real, acesso restrito |

Não preencher uma URL fictícia como se já existisse. O placeholder deve ser substituído quando o serviço estiver implantado.

### 6.2 Variáveis sugeridas

| Variável | Escopo | Sensível? | Observação |
|---|---|---:|---|
| `baseUrl` | Environment | Não | Host do ambiente |
| `apiVersion` | Collection | Não | Inicialmente `v1` |
| `requestId` | Local/runtime | Não | Correlation ID |
| `runId` | Local/runtime | Não | Execução atual |
| `portfolioId` | Local/runtime | Pode ser | Usar fixture sintética em mocks |
| `thesisId` | Local/runtime | Não | ID de teste |
| `apiToken` | Vault/secret store | Sim | Nunca commitar |
| `clientSecret` | Vault/secret store | Sim | Nunca usar em exemplos |
| `mockMode` | Environment | Não | Sinaliza respostas simuladas |

### 6.3 Política de segredos

- Preferir Postman Vault ou mecanismo de segredo aprovado pela organização.
- Não colocar tokens em Collection variables compartilhadas.
- Não exportar Environment com segredo resolvido.
- Não registrar Authorization headers em exemplos, logs ou documentação.
- Rotacionar credenciais expostas e usar escopos mínimos.
- Usar identidades distintas por ambiente.
- Nunca armazenar chaves privadas de carteira, seed phrases ou credenciais de corretoras no Postman.

---

## 7. Mock Servers e Examples — desenvolver o contrato antes do backend

### 7.1 Estratégia mock-first

1. Definir primeiro OpenAPI e schemas.
2. Criar requests representativos e Examples associados.
3. Criar Mock Server a partir da Collection/contrato.
4. Configurar exemplos para sucesso, vazio, parcial e erro.
5. Testar consumidores e Flows contra o mock.
6. Implementar backend real.
7. Reapontar Environment para staging/local.
8. Executar os mesmos testes de contrato contra a implementação real.

Mock valida integração e expectativas de contrato; **não valida cálculos, persistência, segurança real, performance ou correção econômica**.

### 7.2 Catálogo de Examples obrigatório

Para cada endpoint prioritário:

- `200/201`: resposta válida;
- `202`: execução assíncrona aceita;
- `204`: sem conteúdo, quando aplicável;
- `400`: JSON malformado;
- `401`: ausência de autenticação;
- `403`: escopo insuficiente;
- `404`: recurso inexistente;
- `409`: conflito/idempotência/versão;
- `413`: payload excessivo;
- `422`: regra de domínio inválida;
- `429`: rate limit;
- `500/503`: falha interna/indisponibilidade.

Não é necessário implementar todos os códigos em todos os endpoints; documentar os aplicáveis.

### 7.3 Fixtures sintéticas

Criar fixtures versionadas com prefixo `demo_` ou `synthetic_`:

- carteira sintética pequena;
- conjunto de teses com estados epistêmicos variados;
- ITR/DFP fictícios claramente identificados;
- fontes fictícias para testes de proveniência;
- workflow de atualização de tese;
- execuções com sucesso, falha, parcial e aprovação pendente.

Toda resposta mock deve incluir `meta.synthetic=true` ou mecanismo equivalente. Não usar nomes, CPF, contas, posições ou patrimônio de pessoas reais.

### 7.4 Casos de mock importantes

- fonte não encontrada;
- fonte vencida;
- duas fontes conflitantes;
- dado ausente (não converter em zero);
- valor monetário com moeda divergente;
- cálculo que falha em invariant;
- workflow que requer aprovação;
- agente que retorna resposta parcial;
- timeout do provedor de IA;
- rate limit externo;
- idempotency key repetida;
- usuário sem permissão;
- artifact expirado.

---

## 8. Postman Flows — orquestração de jornadas

Flows devem compor APIs e demonstrar jornadas. Regras críticas, cálculos e transações persistentes devem permanecer no backend, scripts determinísticos ou serviço de domínio.

### 8.1 Flow F01 — Health & Capability Discovery

`Start → GET /health → GET /ready → GET /api/v1/capabilities → Branch → Report`

- Se health falhar: encerrar.
- Se health passar e readiness falhar: reportar dependência indisponível.
- Se versão/capacidade incompatível: bloquear jornada.

### 8.2 Flow F02 — Ingestão e qualidade de dados

`Upload/Submit → Create Ingestion → Poll Status → Get Quality Report → Branch`

- `succeeded`: permitir análise.
- `partial`: exigir revisão de lacunas.
- `failed`: não prosseguir.
- PII detectada: bloquear compartilhamento/exportação.

### 8.3 Flow F03 — Atualização de tese

`Select Thesis → Load Context → Submit Research Task → Poll Run → Get Evidence → Red Team → Evaluate → Approval Gate → Publish Artifact`

- O agente autor não aprova a própria tese.
- Se a auditoria de fontes falhar, não publicar como corroborada.
- Mudança de status epistêmico requer critérios e trilha de auditoria.
- A aprovação humana é um gate explícito.

### 8.4 Flow F04 — Diagnóstico de carteira sintética

`Load Synthetic Portfolio → Validate → Analyze Exposures → Run Invariants → Generate Report → Verify Artifact`

Usar apenas fixture sintética no workspace compartilhado. A jornada não é suitability nem recomendação personalizada.

### 8.5 Flow F05 — Experimento quantitativo reproduzível

`Create Experiment → Validate Dataset → Freeze Parameters → Execute → Validate Metrics → Save Artifact → Register Run`

Exigir dataset/version/hash, janela temporal, benchmark, custos, seed, parâmetros e controle de look-ahead/survivorship bias quando aplicável.

### 8.6 Flow F06 — Red Team / Evaluation

`Load Output → Load Evidence → Independent Review → Schema Validation → Invariant Tests → Findings → Pass/Fail`

Não aceitar avaliação apenas por score subjetivo de LLM. Combinar testes determinísticos com revisão qualitativa.

### 8.7 Flow F07 — Oportunidades e grants

`Create Opportunity → Classify Capital Mechanism → Eligibility Check → Evidence/Deadline Check → Scorecard → Human Review → Artifact`

Separar grants, bounties, pilotos, receita, investimento, crédito e incentivos. Uma pontuação não deve se passar por probabilidade de aprovação.

### 8.8 Convenções para Flows

- Cada Flow deve ter objetivo, entradas, saídas, falhas esperadas e dono.
- Nomear versões: `F03-thesis-update-v1`.
- Não embutir segredos em blocos.
- Tratar timeout, retry e idempotência explicitamente.
- Não fazer loops ilimitados.
- Persistir estado durável no serviço de backend, não apenas no Flow.
- Produzir resumo final com `run_id`, status e links de artefatos.

---

## 9. Testes Postman — contrato, comportamento e segurança

### 9.1 Camadas de teste

| Camada | O que verifica | Ferramenta/abordagem |
|---|---|---|
| T0 — Syntax | JSON e OpenAPI válidos | Linter/validator |
| T1 — Contract | Status, headers, schema e campos | Postman tests |
| T2 — Functional | Resultado esperado para fixture | Collection Runner |
| T3 — Invariants | Regras matemáticas/de domínio | Testes determinísticos no backend |
| T4 — Integration | Serviços e dependências | Flows + ambiente de integração |
| T5 — E2E | Jornada ponta a ponta | Playwright/API tests |
| T6 — Security | Auth, autorização, vazamento e abuso | Testes negativos e scanner aprovado |
| T7 — Resilience | Timeout, retry, rate limit e falha parcial | Mocks fault-injection |
| T8 — AI Evaluation | Grounding, citações, calibração e regressão | Harness de eval separado |

### 9.2 Exemplos de asserções

- Status HTTP dentro do conjunto esperado.
- `Content-Type` correto.
- `request_id` presente.
- Schema válido.
- Campos obrigatórios não nulos quando obrigatórios.
- `meta.synthetic` verdadeiro para fixtures.
- Datas com timezone quando o contrato exigir.
- Moeda/unidade presente em valores.
- `status=partial` nunca interpretado como `succeeded`.
- IDs e links coerentes.
- Erros sem stack trace, segredo ou PII.
- Ausência de dados de outro usuário/tenant.

### 9.3 Invariantes financeiros e quantitativos

Executar preferencialmente no código determinístico e testar via API:

- Pesos percentuais reconciliam dentro de tolerância definida.
- Soma de posições e total da carteira respeitam política de arredondamento.
- Moeda-base e conversões têm timestamp e fonte.
- Valores ausentes não são convertidos em zero.
- DCF: coerência entre fluxos, desconto, terminal value e EV bridge.
- Backtest: ausência de look-ahead, survivorship e leakage.
- Métricas incluem janela, frequência, benchmark e custos.
- Cenários e sensibilidades são reproduzíveis.

### 9.4 Testes adversariais

- Prompt injection em documentos/fontes.
- Documento contendo instruções para exfiltrar dados.
- Tentativa de acessar outro tenant.
- Payload excessivo ou malformado.
- IDs enumeráveis.
- Repetição de requisição de criação.
- Resposta de IA com fonte inexistente.
- Alucinação de preço, holding ou dado de perfil.
- Fonte contraditória e fonte desatualizada.
- Tentativa de alterar status de tese sem evidência/gate.

---

## 10. Monitors, observabilidade e SLOs

### 10.1 Monitors Postman

Criar monitores somente para endpoints estáveis e não destrutivos:

- health/readiness;
- capabilities/version;
- endpoint público de documentação, se existir;
- jornada sintética de leitura;
- endpoint de status de serviço.

Não executar monitors que criem carteiras reais, alterem teses, disparem custos de IA ou modifiquem decisões em produção.

### 10.2 Métricas úteis

- disponibilidade e latência p50/p95/p99;
- taxa de erro por endpoint;
- taxa de timeout por dependência;
- idade dos dados e fontes;
- taxa de sucesso/partial/failure de workflows;
- custo por execução e por etapa de agente;
- taxa de validação aprovada;
- regressões de schema;
- incidentes de segurança e autorização.

### 10.3 SLOs iniciais

Não fixar metas numéricas sem baseline. Primeiro coletar dados em desenvolvimento/staging; depois propor SLOs coerentes com custo, criticidade e capacidade operacional.

### 10.4 Tracing

Propagar `request_id`, `trace_id`, `run_id`, `task_id` e `artifact_id` entre API, agentes e serviços. Não incluir PII, prompts privados completos ou credenciais em labels de métricas.

---

## 11. Autenticação, autorização e privacidade

### 11.1 Modelo inicial

- OAuth 2.0/OIDC ou mecanismo de identidade adequado à arquitetura escolhida.
- Scopes mínimos por domínio e operação.
- RBAC/ABAC conforme necessidade real.
- Separação por usuário/tenant desde o desenho dos recursos privados.
- Rate limits por identidade e operação.
- Audit trail para leitura/exportação de dados sensíveis.
- Human approval para alterações de alto impacto.

### 11.2 Níveis de autonomia

| Nível | Capacidade | Gate |
|---|---|---|
| A0 | Documentar e explicar | Sem ação externa |
| A1 | Ler dados autorizados | Escopo de leitura |
| A2 | Preparar análise/artefato | Revisão antes de persistir |
| A3 | Criar/atualizar recursos não críticos | Confirmação conforme política |
| A4 | Operações externas de impacto | Aprovação explícita e controles fortes |
| A5 | Execução financeira/transacional | Fora do escopo inicial; não habilitar por padrão |

O Postman não é o mecanismo de autorização do produto. Ele apenas envia credenciais e testa o comportamento do serviço.

### 11.3 Regras de dados

- Usar dados sintéticos em exemplos, mocks e documentação pública.
- Classificar artefatos por sensibilidade.
- Definir retenção e exclusão.
- Minimizar dados enviados a provedores de IA.
- Registrar base legal/consentimento onde aplicável, com revisão especializada.
- Não presumir conformidade regulatória apenas por possuir testes ou documentação.

---

## 12. OpenAPI como contrato canônico

### 12.1 Organização proposta no repositório

```text
api/
  openapi/
    openapi.yaml
    schemas/
      common.yaml
      errors.yaml
      thesis.yaml
      evidence.yaml
      task.yaml
      workflow.yaml
      portfolio.yaml
      artifact.yaml
  examples/
    synthetic/
      thesis-created.json
      research-run-queued.json
      research-run-partial.json
      validation-error.json
  postman/
    README.md
    collections/
    environments/
    flows/
    mocks/
    test-data/
  contracts/
    event-envelope.schema.json
    task-envelope.schema.json
  tests/
    contract/
    security/
    invariants/
```

A estrutura é uma proposta. Adotar referências externas do OpenAPI com parcimônia; garantir que a especificação consolidada possa ser importada no Postman e validada em CI.

### 12.2 Governança de versões

- API: `/api/v1`.
- Schema: SemVer ou política documentada de compatibilidade.
- Mudanças aditivas tendem a ser minor; breaking changes exigem major.
- Depreciação com aviso, prazo e plano de migração.
- Collections devem declarar a versão do contrato que testam.
- Cada release registra commit, versão OpenAPI e resultado da suíte.

### 12.3 OpenAPI mínimo para começar

O primeiro arquivo deve conter somente:
- `GET /health`;
- `GET /ready`;
- `GET /api/v1/capabilities`;
- `POST /api/v1/research-runs`;
- `GET /api/v1/research-runs/{runId}`;
- `GET /api/v1/theses`;
- `POST /api/v1/theses`;
- schemas comuns de sucesso, erro, evidência, tese e execução.

Não gerar dezenas de endpoints sem consumidor, implementação planejada ou teste correspondente.

---

## 13. Integração com os prompts, Skills e agentes

### 13.1 Mapeamento de prompts para API

| Prompt/Skill | Operação candidata | Saída |
|---|---|---|
| P0 — Data Intake | `POST /ingestions` | dataset + quality report |
| P0b — Boundary Test | `POST /evaluations` | failure modes |
| P1 — Portfolio X-Ray | `POST /portfolio-analyses` | exposures + report |
| P2 — Red Team | `POST /research-runs` com workflow Red Team | findings |
| P3 — Quant Ranking | `POST /quant-experiments` | ranking + metrics |
| P4 — Source Intelligence | `POST /research-runs` | source map |
| P5 — News Triage | `POST /workflows` | event triage |
| P6 — Monitoring | serviço agendado + status API | alert/report |
| A1 — ITR/DFP | workflow documental | normalized financials |
| A2 — Earnings Call | workflow de transcript | claims/evidence |
| A3 — Scenarios/Short | workflow de cenários | scenario matrix |
| A4 — DCF Audit | valuation service | model audit |
| A5 — Agent Automation | workflow/agent adapter | run trace |
| A6 — Skill Generation | task/skill registry | versioned skill |

A operação HTTP deve representar um caso de uso, não simplesmente expor o texto de um prompt.

### 13.2 Envelope de execução de agente

A API não deve expor raciocínio interno privado do modelo. Deve expor resultados auditáveis:

- objetivo e versão do contrato;
- status;
- ferramentas utilizadas (metadados);
- fontes e evidências;
- cálculos reproduzíveis;
- validações e falhas;
- artefatos;
- custo/latência agregados quando disponíveis;
- aprovação necessária.

### 13.3 Portabilidade

O cliente envia contrato independente de modelo. O backend escolhe adapter conforme política/capacidade. O Postman testa a mesma interface com mocks e, depois, runtimes reais.

---

## 14. CI/CD e automação

### 14.1 Pipeline sugerido

`Commit → Lint OpenAPI → Validate Schemas → Run Contract Tests → Run Mock Journeys → Build/Deploy Backend → Integration Tests → Security Checks → Publish Docs`

### 14.2 Ferramentas

- Postman CLI ou Newman, conforme compatibilidade e manutenção do projeto.
- GitHub Actions para execução em pull requests e releases.
- OpenAPI linter/validator.
- pytest para lógica Python.
- Playwright para E2E da WebApp.
- JSON Schema validator para envelopes.
- Testes de invariantes no código de domínio.
- Artifact/report upload para auditoria do build.

Não duplicar a mesma regra em Postman, Python e Playwright sem definir qual é a fonte canônica. Postman valida a fronteira HTTP; código de domínio valida a regra de negócio.

### 14.3 Gatilhos

- Pull request: lint + schema + smoke mock tests.
- Merge: suíte de contrato e integração em ambiente controlado.
- Release: coleção versionada, documentação e relatório.
- Monitor: disponibilidade/saúde de endpoints não destrutivos.

---

## 15. Estratégia de implementação por fases

### Fase 0 — Inventário e decisões

- Mapear scripts, Skills, prompts, dados, outputs e dependências.
- Identificar quais funções já são determinísticas e executáveis.
- Marcar recursos como `implemented`, `prototype`, `planned` ou `mock-only`.
- Definir modular monolith vs serviços separados.
- Registrar ADRs.

**Saída:** capability map + API scope P0.

### Fase 1 — Contrato mínimo

- Criar `api/openapi/openapi.yaml`.
- Definir envelopes de sucesso/erro.
- Definir schemas de tese, evidência, task e run.
- Validar OpenAPI e importar no Postman.

**Saída:** contrato v1 inicial.

### Fase 2 — Postman mock-first

- Criar workspace e Collections.
- Configurar variables e environments.
- Criar Examples sintéticos.
- Criar Mock Server.
- Criar testes de contrato.

**Saída:** consumidor consegue integrar sem backend.

### Fase 3 — Primeiro vertical slice real

Escolher uma jornada de baixo risco e alto valor:

`POST research-run → GET status → GET artifact metadata`

Implementar serviço real que executa uma atualização de tese sobre fixture sintética, com fontes simuladas identificadas, validação de schema e relatório Org/Markdown.

**Saída:** mock e implementação real passam pela mesma Collection.

### Fase 4 — Flows e harness

- Criar F03 Thesis Update e F06 Evaluation.
- Adicionar fault cases, timeout e estados parciais.
- Separar validação determinística de crítica por IA.

**Saída:** jornada reproduzível e auditável.

### Fase 5 — Domínios adicionais

- Ingestão e data quality.
- Portfolio analysis.
- Quant experiments.
- Valuation.
- Opportunities/grants.
- Artifacts/decision journal.

**Saída:** expansão guiada por consumidores reais.

### Fase 6 — Segurança e operação

- Autenticação e autorização.
- Segredos e rotação.
- Observabilidade e SLOs.
- Retenção, privacidade e auditoria.
- Monitors e CI/CD.

**Saída:** staging operacionalmente controlado.

---

## 16. Primeiro vertical slice — especificação executável

### VS-01 — Synthetic Thesis Research

**Objetivo:** provar o contrato de ponta a ponta sem expor dados privados ou depender de um modelo específico.

**Entrada**
- `thesis_id` de fixture sintética;
- pergunta de pesquisa;
- fontes sintéticas identificadas;
- versão do task contract.

**Sequência**
1. `POST /api/v1/research-runs`.
2. Validar resposta `202` e capturar `run_id`.
3. `GET /api/v1/research-runs/{runId}` até estado terminal, com limite de polling.
4. Consultar artefatos.
5. Validar evidências e status epistêmico.
6. Executar avaliação independente.
7. Gerar relatório Org/Markdown.
8. Registrar resultado no audit log.

**Aceite**
- Mesma Collection roda contra Mock e Local/Staging.
- `meta.synthetic=true` no modo mock.
- Nenhuma fonte fictícia apresentada como real.
- Execução parcial é diferenciada de sucesso.
- Falha de validação impede promoção do status da tese.
- Request ID, run ID e artifact ID correlacionáveis.
- Relatório final reproduzível a partir dos fixtures.

**Não faz**
- Não movimenta dinheiro;
- não recomenda compra/venda;
- não usa dados patrimoniais reais;
- não declara tese corroborada sem evidência válida;
- não expõe chain-of-thought.

---

## 17. Checklist de publicação do Postman

### Workspace
- [ ] Workspace criado e com política de acesso.
- [ ] Coleções separadas por domínio/jornada.
- [ ] README com escopo, estado e instruções.
- [ ] Dados sintéticos identificados.

### API contract
- [ ] OpenAPI validado.
- [ ] Schemas reutilizáveis.
- [ ] Erros e estados documentados.
- [ ] Exemplos importáveis.
- [ ] Versionamento e depreciação definidos.

### Environments
- [ ] Mock, Local, Development, Staging e Production separados.
- [ ] `baseUrl` configurável.
- [ ] Segredos fora de exports e Git.
- [ ] Variáveis documentadas.

### Mocks
- [ ] Success, partial, empty e error examples.
- [ ] Casos de fonte ausente/conflitante.
- [ ] Idempotência e autorização simuladas.
- [ ] Respostas mock marcadas como sintéticas.

### Flows
- [ ] Objetivo e dependências documentados.
- [ ] Branches de falha e timeout.
- [ ] Limite de loops/polling.
- [ ] Human gates quando necessários.

### Tests / Monitors / CI
- [ ] Testes de schema e invariantes.
- [ ] Casos negativos de segurança.
- [ ] Monitors não destrutivos.
- [ ] CLI/Runner integrado ao CI.
- [ ] Relatórios arquivados por commit.

---

## 18. Metacrítica — riscos de uma API prematura

### 18.1 API-first não significa endpoint-first

Criar uma API para cada aba do WebApp apenas replica a interface em HTTP e gera acoplamento. A API deve refletir recursos e casos de uso estáveis, não a organização visual atual.

### 18.2 Mock não é backend

Um mock pode retornar JSON impecável enquanto o serviço real não existe ou está errado. Toda Collection deve declarar o ambiente e o grau de realidade do resultado.

### 18.3 Flow não é orquestrador universal

Postman Flows é ótimo para integração visual e demonstração. Workflows duráveis, filas, retries robustos, controle de concorrência e estado de negócio devem ficar no backend/orquestrador apropriado.

### 18.4 Monitor não é avaliação de qualidade

Disponibilidade HTTP não mede qualidade de pesquisa, validade de DCF, calibração de IA ou adequação de decisão.

### 18.5 Mais endpoints não significam mais produto

Priorizar consumidores, fronteiras de domínio e vertical slices. Se uma operação não tem consumidor, teste ou implementação plausível, mantê-la como hipótese.

### 18.6 Sugestão de melhoria

A menor arquitetura coerente para começar é:

[
\boxed{
\text{OpenAPI}
\rightarrow \text{Postman Collection}
\rightarrow \text{Mock}
\rightarrow \text{Contract Tests}
\rightarrow \text{One Real Service}
}
]

Primeiro provar uma jornada. Depois generalizar o padrão. Evitar construir uma “plataforma de plataformas” antes de validar o primeiro serviço.

---

## 19. Decisões arquiteturais pendentes

| Decisão | Opções | Critério |
|---|---|---|
| Backend | FastAPI / outro framework / existente | Reuso do Python atual, deploy e manutenção |
| Persistência | SQLite inicial / PostgreSQL | Concorrência, multiusuário, auditoria |
| Jobs | síncrono / worker + fila | Duração e volume das execuções |
| Auth | OIDC/OAuth / gateway existente | Identidade, tenants e escopos |
| Storage | filesystem / object storage | Tamanho, retenção e acesso |
| Agent runtime | adapter local / API / MCP | Portabilidade, custo e privacidade |
| Contract source | OpenAPI YAML | Deve permanecer versionado no Git |
| Flow ownership | Postman / backend | Durabilidade e criticidade |
| Deployment | local / container / cloud | Segurança e custo operacional |

Não decidir por moda. Registrar a escolha, alternativas descartadas, consequências e gatilho para revisão em ADR.

---

## 20. Definition of Done

O blueprint estará implementado — e não apenas documentado — quando:

1. OpenAPI validado e versionado estiver no repositório;
2. Collections e Environments puderem ser importados;
3. Mock Server responder com Examples sintéticos;
4. Testes de contrato passarem;
5. Flow VS-01 executar a jornada completa;
6. pelo menos um serviço real substituir o mock sem mudar o contrato do consumidor;
7. erros, logs e estados parciais forem observáveis;
8. credenciais e dados sensíveis estiverem protegidos;
9. CI executar validação e publicar relatório;
10. README explicar claramente o que está implementado, simulado e planejado.

---

## 21. Referências oficiais para execução

Consultar a documentação oficial do Postman para validar recursos, limites e nomenclaturas atuais antes da configuração:

- Postman API Platform: https://www.postman.com/product/what-is-postman/
- Postman Learning Center: https://learning.postman.com/
- API specifications / OpenAPI: https://learning.postman.com/docs/design-apis/specifications/working-with-openAPI/
- Collections: https://learning.postman.com/docs/collections/collections-overview/
- Mock servers: https://learning.postman.com/docs/design-apis/mock-apis/overview/
- Postman Flows: https://learning.postman.com/docs/postman-flows/overview/
- Environments and variables: https://learning.postman.com/docs/sending-requests/variables/variables/
- Monitors: https://learning.postman.com/docs/monitoring-your-api/intro-monitors/
- Postman CLI: https://learning.postman.com/docs/postman-cli/postman-cli-overview/
- Newman: https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/

A disponibilidade de recursos pode variar conforme plano, workspace e evolução do produto. Verificar permissões e limites da conta antes de desenhar automações dependentes de funcionalidades específicas.

---

## 22. Síntese

O Postman deve tornar o repositório **consumível por APIs**, sem transformar a ferramenta em centro da arquitetura.

[
\boxed{
\text{Git = fonte da verdade}
\quad
\text{OpenAPI = contrato}
\quad
\text{Postman = bancada de integração}
\quad
\text{Backend = execução}
\quad
\text{Harness = confiança verificável}
}
]

**Filosofema final:** *O mock ensaia a promessa; o contrato define o compromisso; o teste confronta ambos com a realidade.*

**Próxima ação recomendada:** criar primeiro `api/openapi/openapi.yaml` e uma Collection mínima para Health, Capabilities e Synthetic Thesis Research; importar no Postman, gerar Mock Server e provar o VS-01 antes de expandir o catálogo.

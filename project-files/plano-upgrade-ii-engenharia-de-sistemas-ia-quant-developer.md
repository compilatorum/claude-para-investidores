# 🧰 Plano de Upgrade II — Engenharia de Sistemas de IA para Quant Developers e Inteligência de Capital

> **Versão:** 1.0 · **Data:** 2026-10-30  
> **Repositório:** `compilatorum/claude-para-investidores`  
> **Tipo:** plano de arquitetura, engenharia de contexto, tooling, agentes, avaliação e execução.  
> **Escopo:** aplicar ao domínio de investimentos e inteligência de capital as práticas normalmente associadas a AI-assisted software engineering, agentic coding e desenvolvimento de sistemas com LLMs.  
> **Não é:** recomendação de investimento, promessa de desempenho, validação de estratégia quantitativa ou autorização para execução financeira autônoma.

---

## 0. Tese central

O projeto não deve apenas ensinar uma IA a responder prompts financeiros. Deve transformar o próprio processo de pesquisa, análise, modelagem, decisão e aprendizagem em um **ambiente de engenharia de sistemas de inteligência de capital**.

A inversão proposta:

- De *prompt engineering para obter respostas* → **engenharia de tarefas, contratos, contexto e evidências**;
- De *Claude como plataforma obrigatória* → **arquitetura agnóstica de modelos, agentes e runtimes**;
- De *prompts como artefatos isolados* → **workflows versionados, testáveis, compostos e reproduzíveis**;
- De *analista humano usando IA* → **quant developer / capital intelligence engineer usando IA como parte do ambiente de pesquisa**;
- De *relatório como produto final* → **relatório como build de um pipeline de dados, hipóteses, cálculos, validações e decisões**;
- De *automação que executa tarefas* → **harness que controla o que pode ser executado, observado, testado, aprovado e revertido**.

\[
\boxed{
\text{Capital Intelligence Engineering}
=
\text{Domain Model}
+
\text{Context Engineering}
+
\text{Agentic Workflows}
+
\text{Quant Tooling}
+
\text{Evaluation Harness}
+
\text{Decision Governance}
}
\]

**Filosofema:** *O prompt é uma interface; o sistema é o método. O modelo é substituível; a qualidade do processo deve sobreviver à troca do modelo.*

### 0.1 Princípio de design

O projeto deve ser capaz de usar Claude, Pi Agentic Coder, ChatGPT, Gemini, modelos locais, APIs compatíveis, agentes de terminal ou combinações deles, sem reescrever a lógica de domínio.

A unidade principal de portabilidade não é a conversa nem o prompt copiado. É o **contrato de tarefa**: objetivo, contexto necessário, entradas, saídas, ferramentas permitidas, critérios de qualidade, política de risco e evidências.

---

## 1. Diagnóstico do repositório como sistema de IA

O estado atual já contém uma boa base:

- `index.html`: WebApp com 17 abas, construtor de prompts e fluxos de análise;
- `ENGENHARIA_REVERSA_V1_MASTERCLASS.md` e `UPGRADE_V2_ARSENAL_E_FORMACAO_COMPLETA.md`: especificações, prompts e arquitetura multi-IA;
- `skills/*/SKILL.md`: competências especializadas em ITR/DFP, Red Team, DCF, radar e compliance;
- `scripts/*.py`: processamento, ranking, auditoria e dados sintéticos;
- `tests/e2e_playwright_suite.py`: testes E2E da interface e dos fluxos simulados;
- `project-files/perfil-investidor-joao.md`, `teses-de-investimento.md`, `fontes.md`: contexto e conhecimento persistente;
- `project-files/plano-upgrade-inteligencia-de-capital.md`: ampliação da ontologia de capital e do ciclo de decisão.

O gap não é simplesmente “mais prompts” ou “mais agentes”. É a falta de uma **camada explícita de engenharia que conecte**:

1. Domínio financeiro e ontologia de capital;
2. Contratos de tarefas e interfaces entre agentes;
3. Contexto persistente, transitório e recuperado;
4. Ferramentas determinísticas e ambientes de execução;
5. Harness de avaliação, segurança e observabilidade;
6. Artefatos de saída em formatos úteis ao trabalho real;
7. Feedback, calibração e evolução das competências.

### 1.1 Metacrítica: não confundir sofisticação de tooling com qualidade de investimento

Um sistema pode ter muitos agentes, Skills, MCPs, loops e prompts e ainda produzir uma tese ruim. O aumento de complexidade só é justificável quando melhora pelo menos uma destas dimensões:

- precisão factual e matemática;
- rastreabilidade e proveniência;
- cobertura de hipóteses e cenários;
- capacidade de falsificação;
- reprodutibilidade;
- custo, latência ou tempo de pesquisa;
- clareza da decisão;
- aprendizagem mensurável.

**Regra:** cada novo componente precisa de um problema, um contrato, um teste e uma condição de remoção.

---

## 2. Arquitetura de referência: de prompts a um sistema agêntico modular

### 2.1 Camadas

| Camada | Responsabilidade | Artefatos / tecnologias candidatas |
|---|---|---|
| L0 — Domínio | Ontologia financeira e de capital, entidades e relações | JSON Schema, YAML, Markdown, taxonomias |
| L1 — Linguagem | Instruções, gramáticas, templates e protocolos | Prompt templates, DSL, Markdown estruturado |
| L2 — Contexto | Seleção, compressão, recuperação e proveniência | Context packs, RAG, índices, manifests |
| L3 — Competências | Capacidades especializadas e reutilizáveis | Skills, agentes, scripts, notebooks |
| L4 — Orquestração | Sequenciamento, delegação, paralelismo e handoffs | Pi Agentic Coder, CLI agents, scripts, MCP |
| L5 — Execução | Cálculo, dados, pesquisa, arquivos e ambientes | Python, SQL, DuckDB, Polars, APIs, terminal |
| L6 — Harness | Testes, políticas, fixtures, mocks, avaliação | pytest, Playwright, evals, golden datasets |
| L7 — Observabilidade | Logs, custos, versões, decisões e auditoria | JSONL, SQLite/DuckDB, traces, Git |
| L8 — Interface | Interação humana e entregáveis | WebApp, Emacs Org mode, Markdown, HTML, XLSX |
| L9 — Governança | Permissões, aprovações, privacidade e rollback | Policies, allowlists, human gates, audit trail |

### 2.2 Fluxo geral

\[
\text{Intenção}
\rightarrow \text{Task Contract}
\rightarrow \text{Context Pack}
\rightarrow \text{Planner}
\rightarrow \text{Workers}
\rightarrow \text{Tools}
\rightarrow \text{Validators}
\rightarrow \text{Human Review}
\rightarrow \text{Artifact}
\rightarrow \text{Decision Log}
\]

A arquitetura deve separar **planejamento**, **execução**, **verificação** e **aprovação**. O agente que propõe uma ação não deve ser automaticamente o agente que a valida.

### 2.3 Componentes desacoplados

- **Model adapter:** traduz um contrato de tarefa para o formato de cada runtime/modelo;
- **Task registry:** catálogo de tarefas e seus contratos;
- **Context builder:** monta o pacote mínimo de contexto;
- **Tool registry:** lista ferramentas, schemas, permissões e limites;
- **Workflow runner:** executa DAGs e loops;
- **Evaluator:** aplica testes determinísticos e avaliações qualitativas;
- **Artifact renderer:** produz Org, Markdown, HTML, CSV, JSON ou XLSX;
- **Audit logger:** registra entradas, versões, saídas, custos, aprovações e erros.

Nenhum componente deve depender de uma marca de modelo específica.

---

## 3. Engenharia de tarefas: o prompt vira contrato executável

### 3.1 Contrato canônico

Cada tarefa deve possuir um manifesto com:

| Campo | Descrição |
|---|---|
| `task_id` | Identificador estável e versionado |
| `intent` | Decisão ou problema que a tarefa atende |
| `domain` | Macro, equity, crédito, venture, Web3, ReFi etc. |
| `inputs` | Dados, documentos, referências e parâmetros |
| `context_required` | Memórias e documentos necessários |
| `tools_allowed` | Ferramentas permitidas |
| `tools_forbidden` | Ferramentas ou ações proibidas |
| `procedure` | Etapas, dependências e critérios de parada |
| `output_schema` | Estrutura tipada do resultado |
| `quality_gates` | Testes de aceitação |
| `risk_policy` | Limites, aprovações e restrições |
| `provenance_policy` | Citações, fonte, data, página, célula ou hash |
| `model_policy` | Capacidades exigidas, não marca obrigatória |
| `version` | Versão semântica do contrato |

### 3.2 Anatomia expandida do prompt

A estrutura de seis partes existente continua útil, mas deve ser expandida para uma especificação operacional:

\[
\mathcal{T} =
(R, I, C, D, P, O, V, G, S, A)
\]

Onde:

- (R): role / competência;
- (I): intent / decisão a apoiar;
- (C): contexto e fontes autorizadas;
- (D): dados e parâmetros;
- (P): procedimento e decomposição;
- (O): output schema;
- (V): verification / critérios de validação;
- (G): guardrails e política de risco;
- (S): stop conditions;
- (A): approval / nível de autonomia.

A instrução deve declarar explicitamente o que fazer quando dados estiverem ausentes, conflitantes, vencidos ou fora do escopo.

### 3.3 Linguagem de tarefa / DSL

Criar uma pequena linguagem declarativa para descrever workflows, sem criar uma linguagem de programação proprietária prematuramente.

Exemplo conceitual de uma definição:

- tarefa: `equity.thesis.update`;
- entradas: ITR, DFP, release, call, modelo financeiro anterior;
- contexto: tese vigente, histórico de decisões, fontes autorizadas;
- etapas: extrair → reconciliar → comparar → atualizar premissas → red team;
- ferramentas: parser documental, Python, fontes oficiais;
- saída: relatório Org + JSON estruturado;
- gates: reconciliação contábil, fonte por número, cenários, invalidação;
- autonomia: leitura e proposta; alteração de modelo somente após aprovação.

A DSL deve gerar prompts, chamadas de ferramentas, schemas de saída e testes. Não deve ser um novo formato textual sem execução real.

---

## 4. Engenharia de contexto: memória não é despejar todo o histórico no prompt

### 4.1 Tipos de contexto

| Tipo | Conteúdo | Persistência |
|---|---|---|
| Identidade qualitativa | Preferências, filosofia, estilo cognitivo e princípios | Longa duração, com revisão |
| Situação financeira | Patrimônio, passivos, renda, liquidez, objetivos e restrições | Privada, datada, com consentimento |
| Contexto de projeto | Estado do repo, roadmap, decisões arquiteturais | Versionado no Git |
| Contexto de tese | Hipótese, evidências, fontes, cenários e falsificadores | Versionado e ligado ao registro |
| Contexto de tarefa | Inputs específicos e instruções locais | Efêmero |
| Contexto de sessão | Estado atual do workflow, handoffs e pendências | Temporário / recuperável |
| Contexto externo | Dados de mercado, documentos e fontes | Com timestamp, origem e validade |

### 4.2 Context packs

Em vez de enviar tudo a cada agente, o Context Builder deve produzir pacotes mínimos, rastreáveis e específicos por tarefa:

- `context/profile.md`: preferências qualitativas, sem dados patrimoniais;
- `context/mandate.yaml`: objetivos, restrições e suitability, quando fornecidos;
- `context/project-state.md`: estado atual do projeto;
- `context/thesis/<id>.md`: tese e evidências relevantes;
- `context/sources.yaml`: fontes permitidas e hierarquia;
- `context/session.json`: estado transitório da execução.

Cada pack deve incluir versão, data de atualização, origem, escopo, expiração e hashes dos documentos usados.

### 4.3 Política de recuperação

1. Buscar somente o contexto necessário à tarefa;
2. Priorizar fontes primárias e arquivos canônicos;
3. Resolver conflitos por precedência explícita, não por recência automática;
4. Mostrar o que foi recuperado e o que foi omitido quando isso afetar a conclusão;
5. Não completar lacunas com memória inferida;
6. Marcar fatos, hipóteses, inferências e dados sintéticos separadamente;
7. Revalidar dados sensíveis e voláteis antes de decisões.

### 4.4 Context engineering como compressão sem perda decisória

O objetivo não é maximizar tokens no contexto. É maximizar a informação relevante por unidade de custo, preservando as condições necessárias para reproduzir e auditar a decisão.

\[
\text{Context Efficiency}
=
\frac{\text{Relevant Evidence + Decision Constraints}}
{\text{Tokens + Noise + Staleness}}
\]

---

## 5. Engenharia de harness: o ambiente que torna agentes confiáveis

O harness é o conjunto de fixtures, ferramentas, políticas, testes, observabilidade e controles que envolve o agente. Não é apenas um prompt de sistema.

### 5.1 Harness por tarefa

Cada tarefa crítica deve possuir:

- fixtures realistas e dados sintéticos rotulados;
- schemas de entrada e saída;
- mocks para APIs e fontes instáveis;
- testes determinísticos de cálculos;
- golden examples / casos de referência;
- testes adversariais e casos-limite;
- avaliação de citações e proveniência;
- política de ferramentas e permissões;
- limites de custo, tempo e número de iterações;
- logs completos e reprodutíveis;
- critérios de aprovação humana.

### 5.2 Pirâmide de testes

1. **Unit tests:** fórmulas, parsers, conversões, métricas e funções;
2. **Schema tests:** entradas e saídas obedecem aos contratos;
3. **Golden tests:** resultados comparados com casos revisados;
4. **Property tests:** invariantes matemáticos e financeiros;
5. **Integration tests:** conectores, bancos, arquivos e ferramentas;
6. **Agent behavior tests:** o agente seleciona o fluxo correto e respeita limites;
7. **Adversarial tests:** prompt injection, dados conflitantes, fontes maliciosas e instruções embutidas;
8. **E2E tests:** workflow completo, do pedido ao artefato;
9. **Regression evals:** alterações de modelo, prompt, Skill ou contexto não degradam qualidade.

### 5.3 Exemplos de invariantes financeiros

- Pesos de carteira reconciliam com o valor total, dentro de tolerância declarada;
- Fluxos de caixa e períodos estão alinhados;
- Unidades, moedas e datas são explícitas;
- EV/Equity Value não são confundidos;
- WACC, crescimento terminal e perpetuidade passam por limites e cenários;
- Rentabilidade histórica não é projetada como garantia;
- Backtest não usa informação futura;
- Custos, impostos, spread e slippage são incluídos quando relevantes;
- Valores ausentes não são silenciosamente imputados;
- Resultados devem ser reproduzíveis a partir dos inputs e versões.

### 5.4 Harness não é benchmark de modelo

Avaliar modelos é diferente de avaliar o sistema. O mesmo modelo pode performar muito bem ou mal dependendo de contexto, ferramentas, instruções, harness e domínio.

Métricas sugeridas:
- factualidade e precisão de extração;
- taxa de erro matemático;
- cobertura de evidências;
- taxa de citações verificáveis;
- violação de políticas;
- completude de schemas;
- taxa de retrabalho humano;
- custo por tarefa concluída;
- latência;
- taxa de sucesso ponta a ponta;
- calibração de confiança;
- taxa de falsos positivos e falsos negativos.

Não otimizar apenas para “resposta bonita” ou “tarefa concluída”.

---

## 6. Engenharia de loops: do prompt único ao processo iterativo controlado

### 6.1 Loops recomendados

| Loop | Objetivo | Critério de parada |
|---|---|---|
| Plan → Execute → Verify | Completar uma tarefa com verificação | Gates aprovados ou bloqueio explícito |
| Research → Synthesize → Red Team | Construir e confrontar tese | Novas evidências deixam de alterar materialmente a conclusão |
| Extract → Reconcile → Model | Converter documentos em dados e cálculos | Reconciliações fechadas ou exceções documentadas |
| Generate → Test → Repair | Produzir código, planilha ou relatório | Testes passam ou limite de tentativas atingido |
| Hypothesis → Experiment → Update | Aprender sobre uma tese ou produto | Evidência suficiente, prazo ou orçamento esgotado |
| Observe → Alert → Review | Monitorar mudanças | Evento material, falso positivo ou janela encerrada |

### 6.2 Controle de loops

Cada loop deve declarar:
- estado inicial e estado final;
- número máximo de iterações;
- orçamento de tokens/custo/tempo;
- ferramentas permitidas;
- condições de sucesso e falha;
- eventos que exigem intervenção humana;
- mecanismo de rollback;
- log de cada iteração.

**Anti-padrão:** agente repetindo “reconsidere” até produzir uma resposta que parece convincente. Repetição não é evidência; reflexão sem novos dados pode amplificar viés.

### 6.3 Critérios de parada epistêmica

Parar quando:
- não há novas fontes relevantes;
- as fontes restantes são redundantes;
- os resultados estão dentro de tolerâncias pré-definidas;
- a incerteza residual foi explicitada;
- o custo marginal de mais pesquisa supera o valor esperado da informação;
- uma lacuna crítica exige dado ou decisão humana.

---

## 7. Engenharia multiagente: especialização, crítica e arbitragem

### 7.1 Topologia recomendada

Começar com um **orquestrador + especialistas sob demanda + verificador independente**, não com uma sociedade de dezenas de agentes autônomos.

Papéis candidatos:

1. **Orchestrator / Research PM:** entende a intenção, escolhe tarefas e controla o workflow;
2. **Domain Analyst:** analisa o domínio (equity, macro, crédito, venture, Web3, impacto);
3. **Data Engineer:** obtém, limpa, reconcilia e documenta dados;
4. **Quant Developer:** implementa e testa cálculos, modelos, backtests e pipelines;
5. **Thesis Architect:** organiza hipótese, mecanismo, evidência, cenários e falsificadores;
6. **Red Team:** busca explicações alternativas, falhas e condições de invalidação;
7. **Risk Officer:** avalia risco, liquidez, dependências, exposição e ruína;
8. **Source Auditor:** verifica origem, data, página, célula, hash e citações;
9. **Report Editor:** compõe o relatório final no formato solicitado;
10. **Decision Auditor:** registra a decisão humana, premissas e revisão futura.

### 7.2 Regra de independência

O agente que gera a tese não deve ser o único a avaliá-la. O verificador deve receber a tese e as evidências, mas também ter liberdade para consultar fontes e cálculos independentemente.

### 7.3 Padrões de colaboração

- **Sequential handoff:** especialista entrega objeto estruturado ao próximo;
- **Parallel research:** agentes pesquisam dimensões independentes;
- **Critic–reviser:** crítico identifica falhas; autor revisa com justificativa;
- **Debate estruturado:** posições concorrentes com evidências, não debate performático;
- **Ensemble de modelos:** segunda opinião em tarefas de alta materialidade;
- **Arbitragem:** decisão final baseada em critérios explícitos e revisão humana.

### 7.4 Não fazer

- Não criar agentes redundantes que apenas reescrevem o mesmo texto;
- Não tratar consenso entre LLMs como verdade;
- Não delegar decisões financeiras irreversíveis;
- Não permitir que agentes ampliem privilégios ou alterem políticas;
- Não compartilhar dados privados com modelos externos sem política e consentimento;
- Não esconder divergências entre agentes em uma síntese artificialmente harmoniosa.

---

## 8. Linguística, ontologias e compilação semântica

Esta camada é particularmente importante para o projeto: a linguagem não deve ser apenas uma embalagem estética, mas uma interface entre conceitos, dados, operações e decisões.

### 8.1 Vocabulário controlado

Criar um glossário canônico para termos que podem ser confundidos:

- capital, ativo, recurso, exposição, posição, direito, obrigação;
- valor criado, valor capturado, preço, valuation, liquidez;
- hipótese, tese, evidência, sinal, narrativa, inferência;
- receita, grant, bounty, prêmio, equity, token, crédito;
- impacto, adicionalidade, resultado, externalidade;
- confiança, probabilidade, convicção e grau de evidência.

### 8.2 Gramática semântica

Definir relações explícitas:

\[
\text{Actor}
\xrightarrow{\text{allocates}}
\text{Resource}
\xrightarrow{\text{to}}
\text{Opportunity}
\xrightarrow{\text{via}}
\text{Mechanism}
\xrightarrow{\text{produces}}
\text{Outcome}
\]

E separar:

- **criação:** quem ou o que produz valor;
- **captura:** quem recebe o benefício econômico;
- **direito:** qual contrato, licença ou mecanismo dá suporte à captura;
- **liquidez:** como e quando o direito pode ser convertido;
- **risco:** o que pode interromper o mecanismo;
- **evidência:** como se sabe que o mecanismo funciona.

### 8.3 Compilador semântico

Evolução possível:

1. Markdown/Org como entrada humana;
2. parser identifica entidades, relações, status epistêmicos e fontes;
3. validação contra ontologia e schemas;
4. geração de JSON estruturado;
5. geração de relatórios, dashboards e prompts;
6. atualização de grafos e registros;
7. rastreabilidade de volta ao texto e à fonte original.

Não tentar criar uma linguagem total de primeira. Começar com front matter YAML e seções Markdown padronizadas.

### 8.4 Linguagem de incerteza

Toda afirmação material deve ser tipada como:
- fato documentado;
- dado calculado;
- hipótese;
- inferência;
- estimativa;
- opinião atribuída;
- dado sintético;
- desconhecido / não verificado.

A confiança deve ter definição operacional e calibração; não usar percentuais de confiança decorativos.

---

## 9. Quant developer tooling: transformar análise em pesquisa reproduzível

### 9.1 Papel do Quant Developer no projeto

O quant developer não é apenas quem escreve scripts de indicadores. É quem constrói infraestrutura reproduzível para testar hipóteses de investimento, mecanismos econômicos e estratégias de alocação.

Responsabilidades:
- engenharia de dados e proveniência;
- feature engineering e estatística;
- modelagem financeira e quantitativa;
- backtesting e validação fora da amostra;
- análise de sensibilidade e cenários;
- otimização e simulação;
- controle de versões de dados, código e parâmetros;
- monitoramento de drift e falhas;
- documentação de limitações e riscos de modelo.

### 9.2 Stack candidata, escolhida por função

| Função | Opções candidatas | Critério de escolha |
|---|---|---|
| Linguagem principal | Python | Ecossistema de dados e finanças |
| DataFrames | Polars / Pandas | Escala, ergonomia e compatibilidade |
| SQL analítico | DuckDB | Arquivos locais, consultas e baixo atrito |
| Dados tabulares | Parquet / CSV / Arrow | Portabilidade e eficiência |
| Banco transacional leve | SQLite | Estado local e registros |
| Notebooks | Jupyter / marimo | Exploração e comunicação |
| Testes | pytest / Hypothesis | Testes e propriedades |
| Qualidade de dados | Pandera / Great Expectations | Contratos e validações |
| Estatística | SciPy / statsmodels | Inferência e séries temporais |
| ML | scikit-learn / bibliotecas específicas | Apenas quando houver caso de uso |
| Otimização | CVXPY / SciPy | Problemas de alocação bem definidos |
| Backtesting | VectorBT / backtrader ou implementação própria | Avaliar hipóteses e limitações |
| Visualização | Plotly / Matplotlib | Diagnóstico e comunicação |
| Versionamento | Git + manifests de dados | Reprodutibilidade |
| Relatórios | Emacs Org / Quarto / Markdown | Trabalho textual e exportação |

As opções são candidatas, não dependências obrigatórias. O stack deve continuar leve e compatível com o hardware e o orçamento disponíveis.

### 9.3 Protocolo de pesquisa quantitativa

1. Pergunta econômica antes do algoritmo;
2. Mecanismo causal ou hipótese explícita;
3. Dados e universo definidos;
4. Data lineage e tratamento de survivorship/look-ahead bias;
5. Baseline simples;
6. Métricas e benchmark definidos previamente;
7. Divisão temporal correta entre treino, validação e teste;
8. Custos e restrições operacionais;
9. Sensibilidade e robustez;
10. Red Team estatístico;
11. Resultado reproduzível;
12. Registro de decisão e limitações.

### 9.4 Experimentos além de ativos financeiros

O mesmo rigor pode ser aplicado a:
- conversão de OSS em serviços e micro-SaaS;
- taxa de sucesso de grants e bounties;
- custo de aquisição de usuários;
- retenção e uso de ferramentas;
- economia de APIs e licenciamento;
- retorno de tempo e atenção;
- mecanismos de incentivos e governança;
- adicionalidade de projetos de impacto.

Não forçar uma métrica financeira única para fenômenos heterogêneos.

---

## 10. Runtime agnóstico: Claude, Pi Agentic Coder e outras IAs

### 10.1 Separar competência de runtime

Uma Skill descreve o que fazer e como verificar. O runtime descreve como invocar modelos, ferramentas e arquivos. O projeto deve evitar que a competência esteja presa a um único formato proprietário.

### 10.2 Adaptadores

Criar adaptadores conceituais para:
- Claude Skills / Projects / Code;
- Pi Agentic Coder;
- ChatGPT / Codex / Work;
- Gemini;
- agentes CLI e modelos locais;
- APIs de provedores;
- MCP servers e ferramentas especializadas.

Cada adaptador deve implementar:
- envio de instruções;
- inclusão de contexto;
- chamada de ferramentas;
- recebimento de eventos;
- normalização da saída;
- captura de logs;
- tratamento de erros e timeouts;
- política de permissões.

### 10.3 Contrato de saída universal

A saída do modelo deve ser convertida para um envelope comum:

- `status`: success / partial / blocked / failed;
- `summary`: síntese;
- `artifacts`: arquivos e formatos gerados;
- `claims`: afirmações materiais;
- `evidence`: fontes e referências;
- `calculations`: cálculos e parâmetros;
- `uncertainties`: lacunas e incertezas;
- `risks`: riscos e alertas;
- `next_actions`: próximos passos;
- `validation`: testes executados e resultados;
- `runtime_metadata`: modelo, versão, data e custo quando disponíveis.

A camada de domínio não deve depender do formato de resposta nativo de um fornecedor.

### 10.4 Pi Agentic Coder como runtime alternativo

Avaliar Pi como uma opção de execução e desenvolvimento agêntico, sem assumir equivalência automática com Claude Code ou outros ambientes.

Prova de conceito:
1. Escolher uma tarefa delimitada (ex.: atualizar relatório trimestral sintético);
2. Expor apenas os arquivos e ferramentas necessários;
3. Implementar o contrato de tarefa;
4. Executar no runtime Pi;
5. Executar o mesmo contrato em outro runtime;
6. Comparar artefatos, testes, custo, latência, rastreabilidade e intervenção humana;
7. Registrar diferenças e limitações.

Critério de sucesso: mesma especificação de domínio, resultados comparáveis e auditáveis; não identidade textual entre modelos.

---

## 11. Skills como pacotes de competência, não como prompts longos

### 11.1 Anatomia de uma Skill

Cada Skill deve ter:

1. Front matter: nome, descrição, versão, domínio e escopo;
2. Quando usar / quando não usar;
3. Pré-condições e inputs;
4. Contexto necessário;
5. Procedimento passo a passo;
6. Ferramentas permitidas;
7. Output schema;
8. Critérios de qualidade;
9. Falhas comuns e recuperação;
10. Guardrails e aprovação humana;
11. Exemplos positivos e negativos;
12. Fixtures e evals;
13. Referências e dependências.

### 11.2 Tipos de competências

- **Domain Skills:** análise de ações, crédito, macro, venture, ReFi;
- **Engineering Skills:** extração, reconciliação, modelagem, backtesting;
- **Meta Skills:** planejar, decompor, selecionar contexto, revisar;
- **Verification Skills:** auditoria de fontes, matemática, compliance, Red Team;
- **Rendering Skills:** Org, Markdown, HTML, XLSX, apresentações;
- **Operational Skills:** monitoramento, versionamento, logs, gestão de experimentos.

### 11.3 Skills compostas

Uma Skill pode chamar outras, mas deve declarar dependências e contratos. Exemplo:

`update-investment-thesis` = `source-research` + `financial-extraction` + `quant-checks` + `red-team` + `decision-memo`.

A composição não deve esconder erros: cada subetapa retorna estado, evidência e exceções.

---

## 12. Fine-tuning, RAG e memória: escolher a técnica certa

Fine-tuning não é o primeiro passo para “ensinar o modelo a investir”. Antes, é preciso separar o que é conhecimento, o que é procedimento, o que é preferência e o que é comportamento.

| Necessidade | Técnica preferida | Por quê |
|---|---|---|
| Dados de mercado atuais | APIs / conectores / retrieval | Informação muda constantemente |
| Documentos e teses próprias | RAG / busca híbrida | Atualização e citação |
| Preferências do usuário | Perfil estruturado e memória controlada | Baixa latência e revisão |
| Procedimentos repetíveis | Skills / workflows | Versionamento e testes |
| Cálculos financeiros | Código determinístico | Precisão e reprodutibilidade |
| Vocabulário e ontologia | Glossário / schemas / parser | Consistência semântica |
| Estilo de relatórios | Templates e exemplos | Controle explícito |
| Comportamento especializado recorrente | Fine-tuning, somente após avaliação | Pode reduzir custo e variância em tarefas estáveis |

### 12.1 Quando considerar fine-tuning

Somente quando:
- tarefa é recorrente e suficientemente estável;
- há dataset autorizado, representativo e revisado;
- existe baseline de prompting/RAG;
- há métrica de sucesso e conjunto de avaliação separado;
- custo de manutenção e risco de overfitting são aceitáveis;
- existe plano de atualização e rollback.

Não usar fine-tuning para memorizar preços, documentos voláteis, dados pessoais ou regras que mudam frequentemente.

### 12.2 Ciclo de dados para ajuste fino

[
\text{Curadoria}
\rightarrow \text{Rotulagem}
\rightarrow \text{Split}
\rightarrow \text{Baseline}
\rightarrow \text{Treino}
\rightarrow \text{Eval}
\rightarrow \text{Red Team}
\rightarrow \text{Deploy gradual}
\]

Dados de avaliação não podem vazar para o treino. Cada exemplo precisa de proveniência e direitos de uso.

---

## 13. Emacs Org mode como interface de pensamento, pesquisa e relatório

Org mode pode ser um formato central de trabalho humano, não apenas um formato de exportação.

### 13.1 Por que Org

- Outline hierárquico para teses e relatórios;
- TODO states para pipeline e decisões;
- propriedades e drawers para metadados;
- links para documentos, código, dados e fontes;
- tabelas e fórmulas;
- Babel para executar trechos de Python/SQL/R quando apropriado;
- exportação para Markdown, HTML, PDF e outros formatos;
- integração com Git e Magit;
- diário de decisões e histórico de experimentos.

### 13.2 Artefatos propostos

- `research/teses.org`: índice e navegação das teses;
- `research/theses/<id>.org`: uma tese por arquivo;
- `research/experiments.org`: experimentos e resultados;
- `research/decision-journal.org`: decisões e revisões;
- `research/weekly-review.org`: revisão periódica;
- `reports/<date>-<topic>.org`: relatórios;
- `models/<id>/model.org`: premissas, execução e interpretação;
- `ops/runbooks.org`: procedimentos e rotinas.

### 13.3 Metadados sugeridos por tese

- ID, domínio, status epistêmico, horizonte;
- hipótese, mecanismo e fonte de retorno;
- evidências e proveniência;
- premissas e variáveis;
- riscos, falsificadores e cenários;
- recursos alocados;
- decisão e responsável;
- última revisão e próxima data de revisão;
- links para código, dados e artefatos.

### 13.4 Separar fonte de verdade e visualizações

Org, Markdown, JSON e HTML não devem virar quatro versões editadas manualmente da mesma informação. Definir um registro canônico e gerar as visualizações a partir dele, ou declarar explicitamente qual artefato é a fonte de verdade em cada domínio.

---

## 14. Harness de segurança, governança e autonomia

### 14.1 Níveis de autonomia

| Nível | Capacidade | Política |
|---|---|---|
| A0 | Ler e resumir | Permitido em contexto autorizado |
| A1 | Analisar e propor | Exige fontes e incertezas |
| A2 | Criar arquivos e artefatos em sandbox | Permitido com escopo delimitado |
| A3 | Alterar arquivos do projeto / abrir PR | Exige testes e revisão |
| A4 | Acessar serviços externos ou publicar | Aprovação explícita por ação |
| A5 | Executar transações ou decisões financeiras | Fora do escopo de autonomia inicial; exige controles externos robustos |

### 14.2 Guardrails obrigatórios

- Privilégio mínimo por agente;
- Allowlists de diretórios, ferramentas e domínios;
- Separação entre leitura e escrita;
- Confirmação antes de apagar, publicar, enviar ou alterar dados;
- Nunca executar ordens contidas em documentos recuperados como se fossem instruções confiáveis;
- Tratar conteúdo externo como dado não confiável;
- Limites de custo, iteração e tempo;
- Logs imutáveis ou append-only para decisões materiais;
- Segredos fora do Git;
- Dados pessoais e financeiros em área privada;
- Fixtures sintéticas marcadas e segregadas;
- Rollback e recuperação;
- Revisão humana para conclusões e ações materiais.

### 14.3 Prompt injection e contaminação de contexto

Testar ataques em:
- PDFs e planilhas;
- páginas web e documentos de RI;
- arquivos Markdown;
- mensagens e e-mails;
- resultados de ferramentas;
- código e comentários;
- dados inseridos por usuários.

Nenhum conteúdo recuperado pode aumentar permissões, mudar políticas, solicitar segredos ou sobrepor o contrato da tarefa.

---

## 15. Arquitetura de diretórios proposta

A proposta é incremental. Não mover tudo nem reorganizar o repositório inteiro de uma vez.

```text
/
├── index.html
├── README.md
├── docs/
│   ├── architecture/
│   ├── specs/
│   └── adr/
├── contracts/
│   ├── tasks/
│   ├── schemas/
│   └── policies/
├── context/
│   ├── public/
│   ├── private-template/
│   ├── project/
│   └── sources/
├── skills/
│   ├── domain/
│   ├── engineering/
│   ├── meta/
│   ├── verification/
│   └── reporting/
├── agents/
│   ├── orchestrator/
│   ├── workers/
│   └── evaluators/
├── workflows/
│   ├── equity/
│   ├── macro/
│   ├── quant/
│   ├── venture/
│   └── capital-intelligence/
├── src/
│   ├── adapters/
│   ├── context/
│   ├── orchestration/
│   ├── tools/
│   ├── evaluation/
│   └── rendering/
├── research/
│   ├── theses/
│   ├── experiments/
│   └── decisions/
├── reports/
├── data/
│   ├── fixtures/
│   ├── synthetic/
│   └── manifests/
├── tests/
│   ├── unit/
│   ├── schemas/
│   ├── golden/
│   ├── adversarial/
│   ├── agent/
│   └── e2e/
└── ops/
    ├── runbooks/
    ├── observability/
    └── release/
```

A árvore é um alvo possível, não uma migração imediata. O primeiro ciclo pode introduzir apenas `contracts/`, `evals/` e `research/`, mantendo os caminhos existentes.

---

## 16. Roadmap de implementação por fases

### Fase 0 — Inventário e baseline

**Objetivo:** saber o que existe, como funciona e o que não pode ser quebrado.

- Mapear prompts, Skills, scripts, abas, fontes e workflows;
- Identificar duplicações e dependências;
- Classificar artefatos por estado: ativo, legado, experimental, demo;
- Definir baseline de testes e métricas;
- Separar dados sintéticos, demonstração e dados privados;
- Registrar arquitetura atual e decisões existentes.

**Entregáveis:** inventário, mapa de dependências, baseline de evals e ADR inicial.

### Fase 1 — Contratos e schemas

- Definir contrato de tarefa;
- Definir envelope de saída universal;
- Criar schemas para tese, evidência, experimento e decisão;
- Padronizar status epistêmicos;
- Converter dois prompts existentes em tarefas declarativas.

**Critério de saída:** tarefas executáveis em mais de um runtime sem alterar a especificação de domínio.

### Fase 2 — Context engineering

- Criar Context Builder mínimo;
- Separar perfil qualitativo, situação financeira e dados demo;
- Criar manifests de fontes;
- Implementar recuperação por tarefa;
- Adicionar proveniência e validade temporal;
- Criar relatório de contexto utilizado.

**Critério de saída:** cada relatório material declara de quais fontes e context packs depende.

### Fase 3 — Harness e avaliação

- Criar golden datasets sintéticos;
- Adicionar schema tests e property tests;
- Adicionar testes de citações e unidades;
- Criar conjunto adversarial de prompt injection;
- Medir custo, latência, retrabalho e taxa de erro;
- Fazer regressão dos fluxos existentes.

**Critério de saída:** alterações em prompts, Skills e modelos são comparáveis por evals.

### Fase 4 — Runtime agnóstico e quant developer loop

- Escolher uma tarefa de ponta a ponta;
- Implementar adapter para runtime atual;
- Implementar adapter Pi ou outro runtime alternativo;
- Executar mesmo contrato em dois ambientes;
- Gerar relatório Org e JSON;
- Registrar logs e diferenças.

**Critério de saída:** um workflow reproduzível sem dependência de Claude como runtime exclusivo.

### Fase 5 — Multiagentes especializados

- Introduzir orquestrador;
- Separar analista, quant developer e auditor;
- Implementar handoffs com schemas;
- Testar paralelismo e critic–reviser;
- Medir se a especialização melhora o resultado;
- Manter fallback single-agent.

**Critério de saída:** ganho comprovado sobre baseline single-agent, após custo e risco.

### Fase 6 — Linguística e compilação semântica

- Glossário controlado;
- Front matter YAML nos documentos canônicos;
- Parser de teses e evidências;
- Validação ontológica;
- Exportação Org ↔ JSON ↔ HTML/Markdown;
- Grafo de relações entre teses, recursos, evidências e decisões.

**Critério de saída:** os mesmos objetos alimentam análise, relatório e interface sem duplicação manual.

### Fase 7 — Fine-tuning seletivo e otimização

- Identificar tarefas estáveis com volume suficiente;
- Curar dataset autorizado;
- Comparar prompting, RAG e fine-tuning;
- Avaliar generalização e drift;
- Implantar gradualmente, com rollback.

**Critério de saída:** fine-tuning só permanece se superar alternativas simples em métricas relevantes e custo total.

---

## 17. Três provas de conceito prioritárias

### PoC A — Atualização de tese de investimento com auditoria

**Entrada:** tese existente + documentos sintéticos + fontes.

**Pipeline:** Context Builder → extração → reconciliação → atualização quantitativa → Red Team → auditor de fontes → relatório Org.

**Saída:** `thesis-update.org`, JSON de evidências e registro de decisão proposto.

**O que prova:** contratos, contexto, ferramentas, loops, validação e renderização.

### PoC B — Quant research reproducível

**Entrada:** hipótese quantitativa simples e dataset sintético versionado.

**Pipeline:** hipótese → dataset manifest → baseline → backtest sem look-ahead → custos → testes de robustez → relatório.

**Saída:** notebook/script, resultados, gráficos, testes e relatório Org.

**O que prova:** quant developer workflow, código determinístico e harness.

### PoC C — Mesmo workflow em Claude e Pi Agentic Coder

**Entrada:** mesmo contrato, mesmos arquivos, mesmas ferramentas permitidas.

**Pipeline:** executar em runtime A e B → validar schemas → rodar evals → comparar.

**Saída:** matriz de qualidade, custo, latência, falhas e intervenção humana.

**O que prova:** portabilidade e separação entre competência e runtime.

---

## 18. Matriz de priorização

Pontuar cada iniciativa por:

- valor decisório;
- redução de erro;
- reutilização;
- custo de implementação;
- manutenção;
- risco de segurança;
- dependência de fornecedor;
- capacidade de teste;
- compatibilidade com recursos computacionais.

| Prioridade | Iniciativa | Motivo |
|---|---|---|
| P0 | Inventário, contratos, dados demo vs. privados | Integridade e clareza |
| P1 | Task schema + output schema | Portabilidade |
| P1 | Golden tests + validação determinística | Confiabilidade |
| P1 | Context packs e provenance | Auditabilidade |
| P2 | Org mode como formato de relatório | Ergonomia e reprodutibilidade |
| P2 | Runtime adapter Pi | Redução de lock-in |
| P2 | Orquestrador + auditor independente | Qualidade e escala |
| P3 | Compilador semântico e grafo | Reuso de conhecimento |
| P3 | Fine-tuning | Só após dados e evals |

---

## 19. Critérios de sucesso do upgrade

O projeto estará efetivamente mais maduro quando:

1. Uma tarefa financeira ou de capital for descrita por contrato, não por prompt ad hoc;
2. O contexto utilizado for explícito, mínimo e rastreável;
3. O mesmo workflow puder rodar em pelo menos dois runtimes;
4. Cálculos materiais forem determinísticos e testáveis;
5. Relatórios tiverem citações e proveniência verificáveis;
6. Agentes especializados puderem ser substituídos sem quebrar o domínio;
7. Loops tiverem limites, critérios de parada e logs;
8. Org mode, Markdown e JSON puderem ser gerados de forma consistente;
9. Evals detectarem regressões de modelo, prompt, contexto e Skill;
10. A autonomia estiver limitada por políticas explícitas;
11. A complexidade adicionada reduzir custo ou erro demonstravelmente;
12. O sistema aprender com decisões sem transformar resultados isolados em regras universais.

### Métricas mínimas

- taxa de tarefas concluídas com todos os gates;
- taxa de afirmações materiais com fonte verificável;
- erro de cálculo em casos de referência;
- taxa de violação de schema;
- regressões por release;
- custo médio por workflow;
- latência p50/p95;
- intervenção humana por tarefa;
- retrabalho pós-entrega;
- divergência entre runtimes;
- taxa de falsos positivos/negativos;
- percentual de decisões revisadas no prazo.

---

## 20. Antipadrões e metacrítica

| Antipadrão | Por que falha | Contramedida |
|---|---|---|
| Prompt monolítico | Difícil testar, manter e reutilizar | Contratos e subtarefas |
| Context dump | Ruído, custo e contradição | Context packs |
| Multiagente ornamental | Mais custo sem independência | Papéis e métricas explícitos |
| Fine-tuning precoce | Memoriza ruído e cria manutenção | Baseline + evals primeiro |
| Agente que valida a própria saída | Viés de confirmação | Auditor independente |
| Backtest sem controles | Overfitting e look-ahead | Harness quantitativo |
| Modelo como calculadora | Erros numéricos silenciosos | Código determinístico |
| Org como cópia manual | Divergência entre fontes | Fonte canônica + exportação |
| Skill específica de fornecedor | Lock-in | Contratos e adapters |
| Autonomia irrestrita | Ações irreversíveis e prompt injection | Least privilege + human gates |
| Benchmark de linguagem como métrica de investimento | Não mede qualidade econômica | Métricas de domínio e resultados |
| Complexidade por prestígio | Custo de manutenção sem valor | Kill criteria por componente |

**Filosofema:** *A inteligência do sistema não está em quantos agentes falam, mas em quantos erros ele consegue impedir, detectar, explicar e corrigir.*

---

## 21. Integração com o Plano de Upgrade I

O Plano I definiu o que o sistema deve compreender: capital ampliado, oportunidades, mecanismos de criação e captura, risco, impacto e aprendizagem.

Este Plano II define como o sistema deve trabalhar: contratos, contexto, runtimes, Skills, agentes, ferramentas, harness, loops, linguística e artefatos.

| Plano I — Ontologia e decisão | Plano II — Engenharia e execução |
|---|---|
| Oportunidade | Task contract |
| Tese | Context pack + thesis workflow |
| Evidência | Source manifest + provenance |
| Modelo | Quant pipeline + deterministic tests |
| Risco | Risk policy + adversarial eval |
| Decisão | Human approval + decision log |
| Aprendizagem | Evaluation harness + feedback loop |
| Capital ampliado | Domain adapters + multidimensional schemas |
| Impacto | Outcome model + causal evaluation |
| Interface | Org / WebApp / report renderer |

\[
\text{Sistema Completo}
=
\underbrace{\text{Ontologia + Teses + Decisões}}_{\text{Plano I}}
\oplus
\underbrace{\text{Contexto + Harness + Agentes + Tooling}}_{\text{Plano II}}
\]

---

## 22. Próximo passo recomendado

Não implementar a árvore inteira. Fazer primeiro uma vertical slice que atravesse todas as camadas, com escopo pequeno:

**Atualizar uma tese sintética e gerar um relatório Emacs Org auditável, executando o mesmo contrato em dois runtimes, com testes determinísticos e Red Team independente.**

Essa fatia vertical deve demonstrar:
- um contrato de tarefa;
- um Context Pack;
- uma Skill portável;
- um workflow com limites;
- uma ferramenta Python determinística;
- um harness com golden tests;
- dois runtimes;
- um relatório Org;
- logs e proveniência;
- aprovação humana.

Se essa PoC funcionar, o padrão poderá ser replicado para DCF, análise de resultados, macro, crédito, grants, micro-ventures, Web3 e ReFi.

**Síntese final:** o objetivo não é construir “um Claude melhor para investir”. É construir um laboratório portátil de engenharia de inteligência de capital, no qual modelos são motores intercambiáveis, código é o instrumento de precisão, linguagem é a interface semântica, evidência é o lastro e o harness é o sistema imunológico.

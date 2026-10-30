# 🧬 Meta-Prompt Template Chain — Sistema Operacional de Inteligência de Capital

> **Versão:** 1.0 · **Data:** 2026-10-30  
> **Repositório:** `compilatorum/claude-para-investidores`  
> **Tipo:** biblioteca de meta-prompts, contratos de tarefa, cadeias de prompts e protocolos multi-runtime.  
> **Integração:** Engenharia Reversa v1.0 · Arsenal/CPI02 v2.0 · Plano de Upgrade I — Inteligência de Capital · Plano de Upgrade II — Engenharia de Sistemas de IA para Quant Developers.  
> **Finalidade:** transformar os prompts originais P0–P6 e A1–A6 em uma cadeia modular, auditável, expansível e independente de fornecedor, adequada a Claude, Pi Agentic Coder, ChatGPT/Codex, Gemini, agentes locais e outros runtimes compatíveis.  
> **Limite:** este documento especifica workflows e instruções. Não representa recomendação de investimento, suitability, validação de estratégia, aconselhamento regulatório ou autorização para execução financeira autônoma.

---

## 0. Tese central — prompt não é workflow

O repertório original já contém bons padrões: preparação de dados, raio-X, entrevista socrática, Red Team, ranking quantitativo, curadoria de fontes, triagem de notícias, automação, análise documental, DCF e geração de entregáveis. O upgrade proposto não descarta esse repertório: **compila cada prompt em uma unidade de trabalho com contrato, contexto, ferramentas, validação, saída e handoff explícitos**.

A unidade de composição passa a ser a cadeia:

\[
\boxed{
\text{Intent}
\rightarrow \text{Task Contract}
\rightarrow \text{Context Pack}
\rightarrow \text{Prompt Chain}
\rightarrow \text{Tool Calls}
\rightarrow \text{Harness}
\rightarrow \text{Artifact}
\rightarrow \text{Decision Log}
}
\]

**Filosofema:** *Um prompt pede uma resposta; uma cadeia organiza uma investigação. Uma cadeia confiável não elimina o julgamento humano: torna suas premissas visíveis.*

### 0.1 Mudança de paradigma

| Antes | Depois |
|---|---|
| Prompt isolado | Cadeia de tarefas versionada |
| Claude como pressuposto | Runtime intercambiável |
| Contexto colado manualmente | Context Pack mínimo e rastreável |
| Resposta em prosa | Artefato tipado + evidências + pendências |
| “Pense passo a passo” | Procedimento verificável, com cálculos externos quando necessário |
| Agente faz e aprova | Executor separado de validador |
| Relatório final sem linhagem | Proveniência até fonte, página, célula, série ou commit |
| Prompt gigante | Orquestrador + módulos especializados |
| Memória implícita | Estado versionado e consentido |
| Sucesso subjetivo | Quality gates, testes e avaliação |

### 0.2 Princípios invioláveis

1. **Evidência antes de convicção:** nenhuma conclusão factual sem fonte identificável e data.
2. **Fato ≠ inferência ≠ hipótese ≠ opinião:** categorias nunca devem ser fundidas.
3. **Ausência não é zero:** dado ausente, não aplicável, conflitante ou não verificável deve ser tipado.
4. **Código para matemática:** cálculos relevantes devem ser reproduzíveis; não confiar em aritmética mental do LLM.
5. **Não inventar estado do usuário:** perfil qualitativo não equivale a patrimônio, renda, passivos, suitability ou carteira atual.
6. **Dados sintéticos não são dados reais:** fixtures, personas demonstrativas e exemplos devem estar rotulados.
7. **Portabilidade:** o contrato define o trabalho; o adapter traduz para o runtime.
8. **Red Team independente:** quem constrói a tese não deve ser seu único validador.
9. **Reversibilidade:** alterações, ações externas e operações financeiras exigem gates proporcionais.
10. **Complexidade tem custo:** cada agente, ferramenta ou etapa precisa demonstrar utilidade marginal.

---

## 1. Mapa da cadeia-mestra

### 1.1 Camadas funcionais

| Camada | Pergunta | Artefato |
|---|---|---|
| C0 — Intenção | Qual decisão ou investigação motivou a tarefa? | `intent.md` |
| C1 — Contrato | O que entra, o que sai e como será aceito? | `task.yaml` |
| C2 — Contexto | Quais fatos, preferências e documentos são necessários? | `context-pack/` |
| C3 — Planejamento | Qual sequência mínima resolve o problema? | `plan.json` |
| C4 — Execução | Quais agentes, ferramentas e cálculos serão usados? | `run/` |
| C5 — Verificação | Como testar fatos, fórmulas, fontes e coerência? | `validation.json` |
| C6 — Síntese | Como transformar evidência em relatório utilizável? | Org / MD / XLSX / HTML |
| C7 — Decisão | O que foi decidido, por quem, quando e com quais incertezas? | `decision-log.org` |
| C8 — Aprendizagem | O que mudou na hipótese, no processo ou no modelo? | `review.org` |

### 1.2 Cadeia geral

\[
\mathcal{C}_{\text{master}} =
P_{00} \circ P_{01} \circ P_{02} \circ
P_{10} \circ P_{20} \circ P_{30} \circ
P_{40} \circ P_{50} \circ P_{60} \circ P_{70}
\]

- (P_{00}): classificar intenção e risco.
- (P_{01}): resolver lacunas e formular contrato.
- (P_{02}): construir Context Pack.
- (P_{10}): planejar a execução.
- (P_{20}): coletar e normalizar evidências.
- (P_{30}): analisar e calcular.
- (P_{40}): Red Team e auditoria independente.
- (P_{50}): validar e reconciliar.
- (P_{60}): produzir artefatos.
- (P_{70}): registrar decisão, feedback e próximos experimentos.

A composição é condicional: nem toda tarefa precisa de todos os módulos. O orquestrador deve escolher a menor cadeia suficiente.

---

## 2. Meta-prompt raiz — Compiler / Orchestrator

Use este prompt como entrada principal de uma nova tarefa. Ele não deve executar tudo de uma vez; deve classificar, especificar e delegar.

### MP-ROOT — Capital Intelligence Orchestrator

**Papel**  
Atue como Arquiteto de Inteligência de Capital, engenheiro de pesquisa quantitativa e orquestrador de agentes. Seu papel é converter uma intenção humana em um workflow auditável, modular e independente de modelo.

**Contexto**  
O projeto combina análise de investimentos, quant research, engenharia de dados, desenvolvimento de software, micro-ventures, grants, propriedade intelectual, Web3/ReFi, impacto, capital humano e aprendizagem. O objetivo é avaliar e desenvolver opções de criação, preservação e alocação de capital — não reduzir todo valor a preço de mercado.

**Entrada**  
Receba a solicitação do usuário, anexos, arquivos do repositório e contexto explicitamente autorizado. Não presuma que exemplos, personas sintéticas ou dados históricos sejam informações financeiras atuais do usuário.

**Tarefas**
1. Classifique a intenção: `RESEARCH`, `DATA_PREP`, `PORTFOLIO_DIAGNOSTIC`, `THESIS`, `VALUATION`, `QUANT_EXPERIMENT`, `RISK`, `MONITORING`, `CAPITAL_ALLOCATION`, `VENTURE`, `GRANT`, `IMPACT`, `SOFTWARE_ENGINEERING` ou `OTHER`.
2. Determine o nível de risco: informacional, analítico, decisório, operacional ou financeiro.
3. Identifique o que é conhecido, desconhecido, desatualizado, conflitante ou sintético.
4. Formule um contrato de tarefa com objetivo, entradas, contexto, ferramentas, saída, critérios de aceitação, riscos, autonomia e condição de parada.
5. Se faltar dado indispensável, faça somente as perguntas necessárias; não faça entrevista extensa por padrão.
6. Selecione os módulos da cadeia e justifique cada módulo incluído.
7. Defina os agentes necessários. Não crie agentes decorativos.
8. Determine quais etapas podem ser paralelas e quais dependem de resultados anteriores.
9. Exija validação independente para fatos, cálculos, fontes e recomendações de ação.
10. Gere um plano de execução e uma lista de artefatos finais.

**Regras**
- Não invente dados, fontes, métricas, holdings, suitability, patrimônio ou resultados de negócio.
- Não use linguagem de certeza para inferências.
- Não confunda uma hipótese interessante com uma tese corroborada.
- Não faça recomendação personalizada de compra/venda sem mandato, dados atuais e análise apropriada; prefira apresentar trade-offs, cenários e perguntas de decisão.
- Não execute transações, altere arquivos críticos ou publique informações privadas sem aprovação explícita.
- Se o ambiente não tiver uma ferramenta, informe a limitação e proponha alternativa compatível.
- O plano deve funcionar em diferentes runtimes.

**Formato de saída**
1. Resumo da intenção.
2. Contrato da tarefa.
3. Context Pack necessário.
4. Cadeia de módulos selecionada.
5. Agentes e ferramentas.
6. Quality gates.
7. Artefatos de saída.
8. Perguntas pendentes e condição de parada.

**Critério de sucesso**  
Outro runtime deve conseguir executar o contrato sem depender do histórico desta conversa.

---

## 3. Contrato universal de tarefa — Task Contract

Todo prompt especializado deve ser compilável para esta estrutura. Os campos podem ser serializados em YAML/JSON; a representação abaixo é o modelo conceitual.

| Campo | Obrigatório | Regra |
|---|---:|---|
| `task_id` | Sim | Identificador estável, ex. `equity.thesis.redteam` |
| `version` | Sim | SemVer do contrato |
| `intent` | Sim | Problema ou decisão que a tarefa atende |
| `domain` | Sim | Equity, macro, crédito, venture, ReFi etc. |
| `role` | Sim | Competência exigida, não persona teatral |
| `audience` | Sim | Quem usará o resultado |
| `inputs` | Sim | Arquivos, dados, URLs, parâmetros |
| `context_required` | Sim | Contextos canônicos necessários |
| `context_excluded` | Recomendado | Dados irrelevantes ou proibidos |
| `tools_allowed` | Sim | Ferramentas e permissões |
| `tools_forbidden` | Sim | Ações não autorizadas |
| `procedure` | Sim | Etapas, dependências e loops |
| `output_schema` | Sim | Campos e tipos da saída |
| `evidence_policy` | Sim | Fonte, data, localização e linhagem |
| `quality_gates` | Sim | Critérios testáveis de aceitação |
| `risk_policy` | Sim | Limites e alertas |
| `autonomy_level` | Sim | A0–A5 |
| `stop_conditions` | Sim | Quando interromper |
| `human_approval` | Sim | O que exige aprovação |
| `artifact_targets` | Sim | Org, Markdown, JSON, XLSX, HTML etc. |
| `evaluation_cases` | Recomendado | Fixtures/golden tests |
| `owner` / `created_at` | Recomendado | Governança e auditoria |

### 3.1 Envelope de saída comum

Todo agente deve devolver um envelope previsível:

- `status`: `complete`, `partial`, `blocked`, `failed`.
- `task_id` e `contract_version`.
- `summary`: conclusão executiva.
- `facts[]`: fatos com fonte e data.
- `inferences[]`: inferências com racional.
- `hypotheses[]`: hipóteses e falsificadores.
- `calculations[]`: fórmula, inputs, unidade, método, resultado e teste.
- `unknowns[]`: lacunas e conflitos.
- `risks[]`: riscos materiais.
- `artifacts[]`: arquivos e formatos produzidos.
- `validation[]`: testes executados e resultados.
- `handoff`: próxima etapa sugerida.
- `approval_required`: booleano + motivo.

**Regra:** não preencher um campo com uma suposição para parecer completo. Usar `unknown`, `not_available`, `not_applicable` ou `conflicting`.

---

## 4. Context Engineering — Context Pack do investidor-engenheiro

O contexto é composto sob demanda. Não se deve despejar todos os chatlogs, projetos e dados financeiros em toda chamada.

### 4.1 Pacotes de contexto

| Pack | Conteúdo | Regra |
|---|---|---|
| `CTX-IDENTITY` | Preferências qualitativas, estilo de pesquisa e princípios | Não contém dados patrimoniais presumidos |
| `CTX-MANDATE` | Objetivos, horizonte, restrições, liquidez, suitability | Só usar dados explicitamente fornecidos e datados |
| `CTX-PORTFOLIO` | Holdings, quantidades, custos, exposições e passivos | Privado; validar data e origem |
| `CTX-THESIS` | Hipótese, mecanismo, evidências, cenários, falsificadores | Um arquivo por tese |
| `CTX-PROJECT` | Estado do repositório, arquitetura, decisões e roadmap | Git como fonte canônica |
| `CTX-SOURCES` | Hierarquia, URLs autorizadas, licenças e cobertura | Verificar URL e validade |
| `CTX-MARKET` | Séries, preços, eventos e macro | Timestamp, frequência e timezone |
| `CTX-SESSION` | Objetivo da execução, handoffs e pendências | Efêmero e descartável |
| `CTX-EXPERIMENT` | Hipótese experimental, dataset, parâmetros, seed | Reprodutibilidade obrigatória |

### 4.2 Context Builder — prompt

Atue como engenheiro de contexto. Para a tarefa [TASK_ID], monte o menor pacote capaz de preservar a validade da análise.

1. Consulte somente fontes canônicas e autorizadas.
2. Liste cada arquivo/dado utilizado, versão, data, origem e escopo.
3. Separe contexto persistente, transitório e externo.
4. Exclua dados sem relação material com a tarefa.
5. Identifique conflitos e informações vencidas.
6. Não use inferências sobre o usuário para preencher dados financeiros.
7. Produza um manifesto de contexto com hashes quando o runtime permitir.
8. Informe o que ficou de fora e por quê.

Saída: `context-manifest.md` + arquivos referenciados + lista de lacunas.

### 4.3 Regra de precedência

1. Instrução explícita atual do usuário, dentro dos limites de segurança.
2. Dados primários e documentos canônicos válidos para a tarefa.
3. Estado versionado do projeto.
4. Preferências qualitativas explicitamente registradas.
5. Inferências contextualizadas, sempre rotuladas.
6. Dados sintéticos ou exemplos, apenas como demonstração.

A recência não resolve automaticamente conflito de autoridade: um comentário recente não substitui um documento primário.

---

## 5. Linguagem e compilação semântica dos prompts

### 5.1 Gramática funcional

A cadeia deve ser legível em Markdown/Org e convertível em estruturas tipadas:

\[
\text{Prompt DSL}
\rightarrow \text{Parser}
\rightarrow \text{Task Contract}
\rightarrow \text{Context Pack}
\rightarrow \text{Execution Plan}
\rightarrow \text{Artifact}
\]

Vocabulário controlado:
- `FACT`: informação diretamente extraída.
- `INFERENCE`: conclusão derivada de fatos.
- `HYPOTHESIS`: proposição testável.
- `OPINION`: julgamento de terceiro.
- `ASSUMPTION`: premissa adotada para modelagem.
- `PROJECTION`: valor futuro condicionado a premissas.
- `SYNTHETIC`: dado artificial para teste.
- `UNKNOWN`: não conhecido.
- `STALE`: informação vencida.
- `CONFLICTING`: fontes incompatíveis.
- `NOT_APPLICABLE`: não aplicável.

### 5.2 Linguagem de força epistêmica

- “A fonte informa…” → fato atribuído.
- “Os dados sugerem…” → inferência.
- “Uma hipótese é…” → hipótese.
- “O cenário pressupõe…” → premissa.
- “Não foi possível verificar…” → lacuna.
- “A evidência contradiz…” → falsificação parcial/total.
- “Não há base suficiente para concluir…” → suspensão de juízo.

**Proibição:** converter correlação em causalidade, ranking em recomendação, projeção em fato, ou ausência de evidência em evidência de ausência.

### 5.3 Compilador de saída

O mesmo envelope deve alimentar:
- Emacs Org: pesquisa, agenda, links, tabelas, propriedades e diário de decisão;
- Markdown: GitHub, documentação e revisão;
- JSON: integração entre agentes e ferramentas;
- CSV/Parquet: dados tabulares;
- XLSX: modelos e auditoria;
- HTML/SVG: dashboard e visualização;
- PDF/deck: distribuição executiva.

Org pode ser a interface de trabalho humana, mas não deve ser o único formato de intercâmbio entre agentes. Dados estruturados devem continuar disponíveis em JSON/CSV/Parquet.

---

## 6. Prompt Chain P0–P6 — pipeline original reengenheirado

Os prompts originais permanecem reconhecíveis, mas agora são módulos com pré-condições, saídas e gates. A numeração é preservada para compatibilidade com o WebApp.

### P0 — Data Intake, Sanitização e Reconciliação

**Objetivo:** transformar extratos e arquivos brutos em datasets limpos, reconciliados e rastreáveis.

**Prompt adaptado**

Atue como Engenheiro de Dados Financeiros e auditor de dados. Recebi [ARQUIVOS] referentes a [DATA/ESCOPO]. Antes de qualquer análise, faça inventário e preserve os originais.

1. Identifique formato, abas, colunas, tipos, granularidade, moeda, unidade e data de referência.
2. Detecte PII e dados confidenciais; proponha uma cópia sanitizada, sem sobrescrever o original.
3. Atualize preços ou dados voláteis somente se a tarefa autorizar pesquisa e houver fonte adequada; registre mercado, horário, moeda, timestamp e fonte.
4. Reconcilie quantidades, valores, posições, duplicatas e identificadores.
5. Preserve estrutura e formatação quando for requisito.
6. Produza dataset normalizado, dataset sanitizado e relatório de reconciliação.
7. Não ajuste quantidades para forçar igualdade sem registrar a transformação, a razão e o erro residual.
8. Marque cada campo como observado, derivado, estimado, ausente ou sintético.

**Saídas**
- `raw_manifest.json`
- `normalized_positions.csv` ou formato apropriado
- `sanitized_positions.*`
- `reconciliation_report.org`
- `data_quality.json`

**Quality gates**
- Soma das posições reconciliada com o documento de origem, ou diferença explicada.
- Nenhuma PII na cópia destinada a compartilhamento.
- Nenhuma cotação sem timestamp e fonte.
- Arquivo original preservado.
- Transformações reproduzíveis.

**Extensão:** ingestão de ITR/DFP, releases, notas explicativas, transcrições, dados macro, on-chain e datasets alternativos.

### P0b — Anti-prompt / Fronteira irregular

**Objetivo:** demonstrar os limites de uma pergunta vaga, não gerar uma resposta financeira.

Prompt de teste: “Minha carteira está boa?” ou “Quanto está [ATIVO] hoje? Responda sem buscar.”

**Instrução ao avaliador**
1. Execute em ambiente isolado e sem ferramentas.
2. Registre ambiguidades: carteira, objetivo, horizonte, risco, data, mercado e fonte.
3. Avalie se o modelo inventa preço, perfil, holdings ou recomendação.
4. Classifique a resposta: calibrada, genérica, alucinada ou bloqueada corretamente.
5. Compare com a execução usando contrato, contexto e dados.

**Métrica:** taxa de afirmações sem suporte, não eloquência da resposta.

### P1 — Raio-X, Exposição e Entrevista Socrática

**Objetivo:** descrever o estado observado antes de interpretar ou recomendar.

**Prompt adaptado**

Atue como Analista Quantitativo de Portfólio. Use [DATASET_VALIDADO] e [MANDATO, SE EXISTIR].

1. Consolide ativos e contas sem perder a trilha de origem.
2. Classifique por classe, instrumento, emissor, setor, região, moeda, fator e liquidez.
3. Calcule pesos e exposições por ativo, setor, fator, moeda, emissor e look-through de fundos/ETFs quando dados suficientes existirem.
4. Use código para cálculos; declare fórmula, denominador, data e unidade.
5. Identifique concentração direta, indireta, correlacionada e dependência comum.
6. Separe exposição observada de estimativa de look-through.
7. Não recomende compra/venda nesta etapa.
8. Se faltar mandato, faça perguntas curtas sobre objetivo, horizonte, liquidez, aportes, passivos, reserva, restrições e tolerância a perdas; não inferir respostas.
9. Gere relatório descritivo e aguarde respostas antes de avançar para adequação ao mandato.

**Saídas:** tabela de exposições, gráficos, concentração, quality report, perguntas pendentes e arquivo Org.

**Quality gates:** reconciliação, denominadores claros, look-through com cobertura declarada, ausência de recomendação prematura.

### P2 — Red Team da tese e do portfólio

**Objetivo:** procurar razões para a tese estar errada, incompleta, cara ou desatualizada.

**Prompt adaptado**

Atue como analista cético independente. Sua função não é confirmar a narrativa do investidor.

Para cada posição ou tese:
1. Recupere a tese original, data, motivação, premissas e condição de entrada — se documentadas.
2. Identifique eventos e mudanças materiais desde a última revisão.
3. Consulte fontes primárias e secundárias adequadas; cite data, documento e localização.
4. Compare valuation, qualidade, balanço, governança, cenário setorial e custo de oportunidade.
5. Examine sobreposição, correlação, risco de fator, concentração, liquidez e risco de cauda.
6. Procure viés de confirmação, narrativa retrospectiva, ancoragem, sunk cost e extrapolação.
7. Construa a melhor versão do argumento contrário.
8. Liste evidências que invalidariam, enfraqueceriam ou fortaleceriam a tese.
9. Faça perguntas difíceis; não transforme a análise em ordem automática de compra/venda.

**Saída por tese:** tese declarada | fatos recentes | argumentos favoráveis | argumentos contrários | riscos ignorados | falsificadores | perguntas | status epistêmico.

**Quality gates:** fonte primária sempre que disponível; contraponto material; datas; condições de invalidação explícitas.

### P3 — Quant Research, Factors e Ranking

**Objetivo:** operacionalizar lentes quantitativas sem falsa comparabilidade.

**Prompt adaptado**

Atue como Quant Researcher e Quant Developer. Investigue [UNIVERSO] usando [DATASET] e [METODOLOGIA].

1. Defina universo, filtros, período, frequência, benchmark e hipótese antes de calcular.
2. Explique a adequação e as limitações de cada métrica por setor e tipo de empresa.
3. Separe universos que não são comparáveis (ex.: bancos vs. industriais; ETFs vs. ações).
4. Obtenha inputs com fonte, data, unidade e definição.
5. Calcule via Python/SQL, com script, dependências, seed e testes.
6. Trate dados ausentes, outliers, mudanças contábeis e restatements explicitamente.
7. Se houver backtest, controle look-ahead, survivorship, data snooping, custos, slippage, liquidez e viés de seleção.
8. Compare com benchmarks e estratégias simples.
9. Faça sensibilidade e teste fora da amostra quando apropriado.
10. Interprete o ranking como ferramenta de triagem, nunca como recomendação isolada.

**Saídas:** dataset de inputs, notebook/script, ranking, gráficos, metodologia, limitações e testes.

**Quality gates:** reprodutibilidade, validação de dados, cálculo independente, ausência de vazamento temporal, explicação das limitações.

### P4 — Source Intelligence / Curadoria de fontes

**Objetivo:** montar uma malha de fontes por domínio, autoridade e cobertura.

**Prompt adaptado**

Atue como bibliotecário de pesquisa financeira e engenheiro de proveniência.

1. Identifique entidades, fatores, métricas e eventos que precisam ser monitorados.
2. Priorize documentos oficiais e dados primários (CVM, B3, RI, BCB, IBGE, Tesouro, reguladores, órgãos setoriais, filings e datasets licenciados).
3. Adicione jornalismo de apuração como camada de descoberta e contextualização.
4. Trate opinião, redes sociais e conteúdo promocional como leads não verificados.
5. Verifique URL, titular, cobertura, frequência, acesso, paywall, licença e limitações.
6. Mapeie fonte × fator × entidade × evento × periodicidade.
7. Defina regra de corroborar informação material em mais de uma fonte quando necessário.
8. Registre falhas, indisponibilidade e mudanças de endereço.

**Saídas:** `sources.yaml`, matriz de cobertura, hierarquia de fontes, monitoramento e regras de uso.

### P5 — News Triage / Radar de eventos

**Objetivo:** reduzir ruído sem perder eventos relevantes.

**Prompt adaptado**

Atue como analista de eventos e monitoramento de teses. Examine [JANELA_TEMPORAL] em [FONTES_AUTORIZADAS].

Para cada item:
1. Identifique evento, entidade, data de publicação e data efetiva.
2. Verifique se é novo, duplicado, atualização ou rumor.
3. Classifique materialidade e relação com a tese.
4. Separe fato confirmado, interpretação da fonte e inferência própria.
5. Classifique: `ACT`, `WATCH`, `NOISE`, `UNVERIFIED`.
6. Explique em uma frase por que importa ou não importa.
7. Indique qual tese, premissa, métrica ou risco pode ser afetado.
8. Não converta notícia em sinal de negociação sem protocolo validado.

**Saída:** briefing priorizado, lista de ruído, itens não verificados, links, pendências e mudanças de premissas sugeridas.

### P6 — Monitoramento recorrente e aprendizagem

**Objetivo:** transformar monitoramento em revisão de hipóteses, não apenas em clipping.

**Prompt adaptado**

Atue como agente de monitoramento com autonomia limitada. Em cada execução:

1. Leia somente fontes e pastas autorizadas.
2. Compare com o último snapshot e deduplique.
3. Detecte mudanças em fatos, indicadores, premissas e limites.
4. Relacione eventos a teses, decisões e falsificadores.
5. Gere alertas com prioridade e justificativa.
6. Atualize apenas rascunhos ou staging; não altere tese canônica, perfil ou modelo financeiro sem aprovação.
7. Registre fontes, timestamps, arquivos processados, erros e itens ignorados.
8. Se não houver novidade material, informe isso — não fabrique atividade.
9. Crie fila de revisão humana e permita rollback.

**Saídas:** relatório Org semanal, `events.jsonl`, diff de teses, lista de revisão e log de execução.

---

## 7. Prompt Chain A1–A6 — módulos avançados de pesquisa e execução

### A1 — Análise documental de resultados (ITR/DFP/Release)

Atue como analista fundamentalista e engenheiro de dados. Analise [EMPRESA] com base em [DOCUMENTOS] e [PERÍODO].

1. Inventarie documentos, datas, períodos e versões.
2. Extraia demonstrações, notas, indicadores operacionais, guidance e eventos.
3. Cite página, seção, tabela ou nota para cada número material.
4. Reconcile DRE, balanço, fluxo de caixa e indicadores ajustados.
5. Compare trimestre, ano, LTM e histórico, mantendo períodos comparáveis.
6. Diferencie reportado, ajustado pela companhia, calculado e estimado.
7. Identifique mudanças contábeis, não recorrentes, restatements e inconsistências.
8. Atualize drivers e perguntas de diligência; não conclua valuation sem etapa própria.

**Saída:** bridge de resultados, KPI table, fatos vs. inferências, red flags, perguntas e JSON estruturado.

### A2 — Teleconferência e discurso da gestão

Atue como analista de comunicação corporativa e estratégia.

1. Extraia afirmações verificáveis, guidance, metas e riscos mencionados.
2. Compare com o trimestre anterior e com resultados realizados.
3. Identifique mudança de narrativa, omissões, contradições e linguagem vaga.
4. Vincule cada afirmação a timestamp/página/trecho.
5. Separe promessa, intenção, meta, guidance formal e resultado.
6. Gere perguntas de acompanhamento.

**Saída:** matriz `claim → evidence → consistency → implication → follow-up`.

### A3 — Cenários, short thesis e Red Team

Atue como analista independente que constrói a melhor tese contrária.

1. Defina cenário pessimista, base e otimista com premissas explícitas.
2. Modele drivers operacionais, financeiros e setoriais.
3. Construa uma tese contrária forte, sem caricatura.
4. Identifique catalisadores, assimetrias, riscos de liquidez e eventos binários.
5. Liste condições de invalidação para ambos os lados.
6. Não trate short thesis como recomendação de venda ou posição vendida.

**Saída:** matriz de cenários, mapa de catalisadores, tese contrária e monitoramento.

### A4 — Auditoria de DCF e modelos herdados

Atue como auditor quantitativo de modelos financeiros em modo read-only.

1. Mapeie abas, células, fórmulas, links externos, hardcodes e dependências.
2. Verifique consistência temporal e integridade das fórmulas.
3. Audite receita, margens, capex, capital de giro, impostos, dívida e fluxo de caixa.
4. Recalcule Ke, Kd, WACC, valor terminal e ponte EV-equity.
5. Teste sinais, unidades, moedas, períodos, datas e circularidades.
6. Faça sensibilidade e cenários; não imponha precisão artificial.
7. Registre célula, fórmula original, problema, impacto, correção proposta e confiança.
8. Não altere o workbook antes de aprovação explícita.
9. Compare cálculo independente com o modelo e explique diferenças.

**Saída:** auditoria célula a célula, bridge de valuation, sensibilidade, patches propostos e log de QA.

### A5 — Agentes, automações e rotinas

Atue como arquiteto de automação. Projete uma rotina para [OBJETIVO], usando [RUNTIME] e [FERRAMENTAS].

1. Defina trigger, janela, fontes e permissões.
2. Defina idempotência, deduplicação, retry, timeout e tratamento de falhas.
3. Separe leitura, transformação, escrita e publicação.
4. Use staging e revisão humana para alterações relevantes.
5. Registre logs, custos, latência, erros e artefatos.
6. Defina política de retenção e privacidade.
7. Inclua desligamento, rollback e execução manual.
8. Teste com fixtures antes de habilitar agendamento.

**Saída:** workflow spec, permissões, testes, runbook e plano de rollback.

### A6 — Anatomia universal do prompt e geração de Skills

Atue como engenheiro de prompts e designer de competências. Transforme [MÉTODO] em uma Skill reutilizável e testável.

1. Defina nome, escopo, gatilhos de ativação e anti-gatilhos.
2. Converta o método em contrato, procedimento e output schema.
3. Liste contexto obrigatório e ferramentas opcionais.
4. Inclua exemplos positivos, negativos, casos-limite e dados sintéticos.
5. Defina quality gates, avaliação, limites e stop conditions.
6. Separe instruções do modelo de cálculos determinísticos.
7. Crie exemplos de uso em mais de um runtime.
8. Gere `SKILL.md`, testes e documentação de manutenção.

**Saída:** Skill completa + fixtures + checklist de revisão.

---

## 8. Cadeias compostas — além dos prompts originais

### CH-01 — Atualização de tese de investimento

**Quando usar:** resultados trimestrais, fato relevante, mudança macro, alteração de valuation ou evento material.

\[
A1 \rightarrow A2 \rightarrow P4 \rightarrow P5
\rightarrow P2 \rightarrow P3 \rightarrow V1
\]

1. Coletar documentos primários.
2. Extrair e reconciliar fatos.
3. Comparar discurso e realização.
4. Atualizar drivers e premissas.
5. Construir Red Team.
6. Rodar valuation/fatores quando aplicável.
7. Validar evidências e gerar relatório.
8. Submeter alteração da tese à aprovação humana.

**Entregável:** `thesis-update.org`, `thesis-state.json`, evidências e diff da tese anterior.

### CH-02 — Pesquisa quantamental reproduzível

**Quando usar:** fator, ranking, screening, backtest, sinal ou experimento.

1. Formular hipótese e mecanismo.
2. Definir universo e dados disponíveis na data.
3. Criar pipeline de ingestão e validação.
4. Implementar baseline simples.
5. Executar testes de qualidade e vieses.
6. Rodar modelo e sensibilidade.
7. Comparar fora da amostra, quando viável.
8. Fazer Red Team estatístico.
9. Publicar notebook/script, dataset manifest e relatório.

**Entregável:** relatório Org + código + dados versionados/metadados + avaliação.

### CH-03 — Capital ampliado e micro-ventures

**Quando usar:** avaliar serviço, micro-SaaS, OSS, licenciamento, grant, bounty, piloto ou venture.

Atue como analista de venture building e alocação de capital. Avalie [OPORTUNIDADE] sem pressupor que interesse pessoal seja demanda de mercado.

1. Defina problema, usuário, comprador, beneficiário e pagador.
2. Identifique evidência de demanda e substitutos.
3. Diferencie capital necessário, tempo, custo de oportunidade e risco de execução.
4. Mapeie vias de financiamento: bootstrapping, grant, bounty, piloto pago, serviço, SaaS/API, licenciamento, revenue share, crowdfunding ou equity/tokenização.
5. Separe dinheiro não dilutivo, receita, investimento e reconhecimento reputacional.
6. Modele cenários de adoção, margem, recorrência e manutenção.
7. Defina menor experimento informativo e métrica de validação.
8. Analise dependências, distribuição, compliance, segurança e custo operacional.
9. Defina gatilhos de continuar, pivotar ou encerrar.
10. Não invente TAM, clientes, tração, valuation ou probabilidade.

**Saída:** opportunity memo, experimento, unit economics, mapa de financiamento e decision log.

### CH-04 — Grants e financiamento não dilutivo

1. Classifique projeto, maturidade, open-source requirements, geografia e elegibilidade.
2. Busque chamadas oficiais e datas vigentes.
3. Verifique ticket, contrapartida, milestones, propriedade intelectual, reporte e restrições.
4. Mapeie fit por projeto e custo de candidatura.
5. Prepare pacote de evidências e orçamento.
6. Diferencie grant, prize, bounty, accelerator e investimento.
7. Produza tracker com status e próxima ação.
8. Não trate aplicação enviada como financiamento garantido.

### CH-05 — Tokenização, Web3 e incentivos

1. Defina o problema econômico que a tokenização resolveria.
2. Compare alternativa sem token, ledger interno, pontos/reputação, crowdfunding e instrumentos tradicionais.
3. Separe utilidade, governança, propriedade, recompensa e especulação.
4. Analise direitos, transferibilidade, liquidez, concentração, ataques Sybil e incentivos perversos.
5. Avalie segurança, custódia, oráculos, contratos, governança, jurisdição e custos.
6. Proponha primeiro protótipo simulado/off-chain quando suficiente.
7. Exija parecer jurídico/contábil qualificado antes de emissão ou oferta pública.
8. Não prometa liquidez, retorno, valorização ou enquadramento regulatório.

**Regra de parcimônia:** token é uma opção arquitetural, não um requisito de produto.

### CH-06 — Portfolio of Options / Capital Intelligence

Avalie uma oportunidade como opção de alocação de recursos:

- Capital financeiro: caixa, risco, retorno, liquidez.
- Capital cognitivo: atenção, energia, capacidade de aprendizagem.
- Capital intelectual: método, código, IP, conhecimento tácito.
- Capital computacional: dados, ferramentas, infraestrutura.
- Capital relacional: confiança, rede, reputação.
- Capital empreendedor: capacidade de execução e distribuição.
- Capital socioambiental: externalidades, regeneração, impacto.
- Capital experiencial: aprendizagem, autonomia e qualidade de vida.

Para cada dimensão, descreva estoque, fluxo, custo de manutenção, risco de depreciação e possibilidade de conversão. Não force uma unidade monetária comum quando a conversão não for defensável.

### CH-07 — Org-mode Research & Decision Journal

Converta o resultado para Emacs Org com:
- propriedades de identificação e status;
- timestamp, fontes e links;
- tabelas de fatos, premissas e cenários;
- tarefas e pendências;
- links para scripts, datasets e commits;
- seção de decisão e justificativa;
- revisão futura e gatilhos de reavaliação.

**Saída mínima:** `research-note.org`, `decision-log.org`, `sources.org` e arquivos estruturados auxiliares.

---

## 9. Sistema multiagente — papéis e handoffs

Agentes são papéis funcionais, não necessariamente processos ou modelos diferentes. Um runtime pode simular papéis sequencialmente; paralelismo só quando há independência real.

| Agente | Responsabilidade | Não pode |
|---|---|---|
| Orchestrator | Contrato, plano, handoffs e parada | Inventar dados para preencher lacunas |
| Context Curator | Context Pack e proveniência | Incluir dados privados sem necessidade |
| Data Engineer | Ingestão, normalização e qualidade | Alterar fonte bruta |
| Fundamental Analyst | Fatos e drivers da empresa | Confundir narrativa com evidência |
| Quant Developer | Cálculos, código e testes | Ajustar método após ver resultado sem registrar |
| Macro Analyst | Cenários e fatores macro | Apresentar projeções como fatos |
| Thesis Architect | Estrutura da hipótese e falsificadores | Proteger a tese contra refutação |
| Red Team | Melhor argumento contrário | Produzir oposição caricatural |
| Risk Officer | Exposição, liquidez, cauda e limites | Aprovar a própria execução |
| Source Auditor | Verificar origem, data e localização | Usar fonte secundária como primária sem rótulo |
| Report Editor | Clareza e formatos | Alterar substância para melhorar narrativa |
| Decision Auditor | Registrar decisão e avaliar processo | Reescrever retrospectivamente a decisão |

### 9.1 Protocolo de handoff

Cada handoff inclui:
1. tarefa e versão do contrato;
2. resumo do que foi feito;
3. arquivos e fontes utilizados;
4. fatos novos e cálculos;
5. incertezas e conflitos;
6. testes executados;
7. trabalho restante;
8. pergunta específica para o próximo agente.

### 9.2 Independência real

- Red Team recebe tese e evidências, mas deve também procurar evidência externa contrária.
- Source Auditor verifica amostra de afirmações sem depender da explicação do autor.
- Quant Validator recalcula outputs críticos por caminho independente.
- Decision Auditor compara decisão com evidências disponíveis à época, não com o resultado conhecido posteriormente.

---

## 10. Loops de trabalho e critérios de parada

### 10.1 Loops padronizados

| Loop | Ciclo | Condição de saída |
|---|---|---|
| L1 — Plan/Execute/Verify | planejar → executar → testar | gates aprovados ou bloqueio documentado |
| L2 — Research/Synthesize/Red Team | pesquisar → sintetizar → contestar | sem novo achado material após limite definido |
| L3 — Extract/Reconcile | extrair → reconciliar → auditar | diferenças explicadas |
| L4 — Generate/Test/Repair | gerar → testar → corrigir | testes passam ou limite de tentativas |
| L5 — Hypothesis/Experiment/Update | hipótese → experimento → atualização | evidência suficiente ou experimento inconclusivo |
| L6 — Monitor/Alert/Review | monitorar → alertar → revisar | evento resolvido ou escalado |

### 10.2 Budget e stop conditions

Toda execução relevante deve declarar:
- limite de iterações;
- limite de chamadas/ferramentas;
- orçamento de tokens/custo/tempo, quando disponível;
- critério de cobertura;
- critérios de bloqueio;
- gatilho de aprovação humana.

**Não faça loop infinito de “melhore mais”.** Se a melhoria marginal cair abaixo do custo, finalize com limitações documentadas.

---

## 11. Harness e avaliação das cadeias

### 11.1 Camadas de teste

1. **Unit:** parser, cálculos, transformações, validação de schema.
2. **Integration:** dados → scripts → artefatos.
3. **E2E:** fluxo completo no WebApp/CLI.
4. **Golden cases:** exemplos com resultado esperado.
5. **Adversarial:** prompt injection, fonte falsa, dados conflitantes, ausentes e vencidos.
6. **Epistemic:** fato/inferência/hipótese corretamente rotulados.
7. **Financial invariants:** unidades, reconciliação, sinais, períodos, denominadores.
8. **Runtime portability:** mesmo contrato em Claude e Pi, por exemplo.
9. **Regression:** nova versão não quebra tarefas previamente aceitas.

### 11.2 Métricas sugeridas

| Dimensão | Métrica |
|---|---|
| Factualidade | % de afirmações materiais rastreáveis |
| Proveniência | % de números com fonte, data e localização |
| Reconciliação | diferenças não explicadas |
| Matemática | divergência contra cálculo independente |
| Calibração | confiança vs. taxa de acerto |
| Cobertura | itens relevantes encontrados / conjunto de referência |
| Robustez | desempenho em casos adversariais |
| Portabilidade | taxa de sucesso por runtime |
| Eficiência | custo, latência e tokens por tarefa aceita |
| Utilidade | tempo humano economizado e retrabalho |
| Aprendizagem | mudanças justificadas de hipótese após evidência |

Não existe uma métrica única que prove qualidade de investimento. E2E verde comprova apenas os caminhos testados.

### 11.3 Prompt de avaliação independente

Atue como avaliador independente. Receba contrato, entradas, resultado e critérios esperados. Não refaça a tarefa para justificar o resultado.

1. Verifique cada gate.
2. Audite amostra de fatos e números.
3. Recalcule métricas críticas.
4. Identifique afirmações sem suporte.
5. Procure falhas de escopo, unidade, temporalidade e causalidade.
6. Teste se a saída atende ao consumidor final.
7. Classifique: `PASS`, `PASS_WITH_WARNINGS`, `FAIL`, `BLOCKED`.
8. Justifique cada falha com evidência.

---

## 12. Runtimes, adapters e portabilidade

### 12.1 Contrato comum, adapters diferentes

| Runtime | Uso potencial | Adapter deve normalizar |
|---|---|---|
| Claude | documentos longos, Skills, análise e artefatos | tools, Projects, formato de saída |
| Pi Agentic Coder | execução agentic em terminal e código | permissões, shell, contexto e ferramentas |
| ChatGPT/Codex | análise, programação e ferramentas conectadas | tool calls, arquivos, outputs |
| Gemini | documentos e ecossistema Google, conforme acesso | conectores, limites e schemas |
| Modelos locais | privacidade, custo marginal e experimentos | contexto, quantização, tool calling e avaliação |
| APIs/MCP | integração e execução programática | autenticação, schema, logs e rate limits |

### 12.2 Teste de portabilidade

Escolha uma tarefa não sensível e reproduzível:
- mesmo contrato;
- mesmos arquivos sintéticos;
- mesmo Context Pack;
- mesmas ferramentas equivalentes;
- mesmo output schema;
- mesmos testes.

Compare:
- qualidade factual;
- completude;
- custo e latência;
- taxa de falha;
- necessidade de correção humana;
- consistência do formato.

**Não compare modelos com prompts, dados ou ferramentas diferentes e atribua a diferença ao modelo.**

### 12.3 Prompt Adapter

Converta o contrato canônico para as convenções do runtime, preservando:
- objetivo;
- restrições;
- ferramentas autorizadas;
- schema;
- evidências;
- stop conditions;
- autonomia.

O adapter não pode remover guardrails para fazer a tarefa “funcionar”.

---

## 13. Skills como pacotes de competência

Uma Skill é uma competência operacional, não uma coleção de instruções genéricas.

Estrutura mínima:
- nome e descrição;
- escopo e anti-escopo;
- gatilhos;
- entradas e dependências;
- contexto requerido;
- procedimento;
- ferramentas e permissões;
- output schema;
- quality gates;
- casos de teste;
- exemplos;
- limitações;
- versão e changelog.

### 13.1 Biblioteca proposta

- `skill.data-intake`
- `skill.portfolio-xray`
- `skill.thesis-redteam`
- `skill.equity-results`
- `skill.valuation-dcf-audit`
- `skill.quant-research`
- `skill.source-intelligence`
- `skill.event-radar`
- `skill.grant-screening`
- `skill.microventure-underwriting`
- `skill.tokenization-design-review`
- `skill.impact-and-regenerative-capital`
- `skill.org-reporting`
- `skill.decision-audit`

Cada Skill deve ter pelo menos um caso positivo, um caso negativo e um caso adversarial.

---

## 14. Fine-tuning, RAG, Skills e código determinístico

Escolha a técnica pelo tipo de problema:

| Necessidade | Técnica preferida |
|---|---|
| Conhecimento que muda e precisa de fonte | RAG / recuperação |
| Procedimento estável e reutilizável | Skill / prompt versionado |
| Cálculo exato e repetível | Código determinístico |
| Integração com sistemas | API / MCP / adapter |
| Memória de estado e decisões | Banco/arquivos versionados |
| Formato de tarefa | Schema / DSL |
| Comportamento de estilo ou classificação recorrente | Avaliar fine-tuning, após dataset e baseline |
| Conhecimento privado de projeto | Context Pack com controle de acesso |

**Não fine-tunar para compensar ausência de dados, fontes ou harness.** Exigir dataset autorizado, curadoria, baseline, conjunto de avaliação separado, análise de regressão e justificativa econômica.

---

## 15. Emacs Org mode — interface de pesquisa e decisão

Org é uma excelente superfície de trabalho para leitura, navegação, agenda, revisão e composição de relatórios. O objetivo é permitir que o sistema produza artefatos úteis ao fluxo do pesquisador, sem aprisionar a lógica em um formato proprietário.

### 15.1 Tipos de documento

- `inbox.org`: captura de hipóteses e perguntas.
- `research-index.org`: índice e links de pesquisa.
- `theses.org`: índice de teses.
- `thesis-<id>.org`: tese individual.
- `experiments.org`: experimentos e resultados.
- `decision-log.org`: decisões e justificativas.
- `weekly-review.org`: revisão periódica.
- `sources.org`: fontes e cobertura.
- `runbooks.org`: procedimentos operacionais.
- `opportunities.org`: grants, bounties, pilotos e ventures.

### 15.2 Modelo de nota Org

- Propriedades: ID, STATUS, DOMAIN, CREATED, UPDATED, OWNER, CONFIDENCE, REVIEW_DATE.
- Seções: pergunta, hipótese, fatos, inferências, método, cálculos, cenários, Red Team, riscos, decisão, pendências, fontes.
- Links: arquivo-fonte, página, célula, script, commit e relatório.
- TODOs: próxima ação, responsável e prazo.
- Histórico: registrar alteração de premissa e razão.

### 15.3 Regra de integridade

Relatório Org é uma visão legível do resultado; dados estruturados e scripts são a base para reprodução. Não editar manualmente um número no relatório sem corrigir o dado ou cálculo de origem.

---

## 16. Governança, privacidade e autonomia

### 16.1 Níveis de autonomia

| Nível | Permissão |
|---|---|
| A0 | Apenas explicar e planejar |
| A1 | Ler fontes e arquivos autorizados |
| A2 | Calcular, transformar e gerar artefatos em staging |
| A3 | Propor alterações em arquivos versionados, sem publicar |
| A4 | Executar ações externas reversíveis após aprovação |
| A5 | Operações irreversíveis ou financeiras — não habilitar por padrão |

### 16.2 Controles

- princípio do menor privilégio;
- allowlist de fontes, pastas, APIs e comandos;
- segregação de dados privados, sintéticos e públicos;
- proteção contra prompt injection em documentos e páginas;
- revisão humana antes de publicar ou compartilhar;
- logs sem exposição desnecessária de PII;
- backup e rollback;
- limites de execução;
- política de retenção;
- revisão periódica de credenciais e permissões.

### 16.3 Separação de perfis e dados

O perfil qualitativo do investidor não é suitability. O arquivo demonstrativo de persona Rafael e os dados sintéticos do E2E não representam a situação financeira do usuário. Holdings, patrimônio, renda, passivos, reserva, horizonte e limites quantitativos só podem vir de informação explicitamente fornecida, atualizada e autorizada.

---

## 17. Arquitetura de diretórios sugerida

A implementação pode evoluir incrementalmente; não é necessário criar tudo de uma vez.

- `prompts/`
  - `root-orchestrator.md`
  - `chains/`
  - `modules/p0-p6/`
  - `modules/a1-a6/`
  - `composites/`
- `contracts/`
  - `schemas/`
  - `tasks/`
  - `policies/`
- `context/`
  - `profiles/`
  - `mandates/`
  - `projects/`
  - `theses/`
  - `sources/`
- `skills/`
- `agents/`
- `adapters/`
- `workflows/`
- `harness/`
  - `fixtures/`
  - `golden/`
  - `adversarial/`
  - `evals/`
- `scripts/`
- `reports/`
  - `org/`
  - `markdown/`
  - `html/`
- `logs/`
- `docs/`

A estrutura real deve respeitar o repositório atual e evitar duplicar arquivos que já cumprem essas funções.

---

## 18. Plano de implementação incremental

### Fase 0 — Inventário e rastreabilidade
- Mapear prompts atuais, abas, Skills, scripts e testes.
- Criar IDs e relacionar P0–P6/A1–A6 com arquivos existentes.
- Identificar duplicatas, divergências e instruções desatualizadas.
- Não reescrever tudo.

### Fase 1 — Contrato universal
- Criar schema mínimo de Task Contract.
- Definir envelope de saída.
- Converter P1 ou A1 como primeiro caso.
- Validar com dados sintéticos.

### Fase 2 — Context Packs
- Separar perfil qualitativo, mandato, carteira, tese, projeto e sessão.
- Criar manifest de proveniência.
- Garantir separação entre persona demonstrativa e contexto real.

### Fase 3 — Harness mínimo
- Criar fixtures, golden cases e testes de schema.
- Testar fatos, cálculos, citações e lacunas.
- Adicionar um caso adversarial.

### Fase 4 — Prompt Chain
- Implementar MP-ROOT.
- Converter P0–P6 em módulos versionados.
- Criar um workflow composto de atualização de tese.

### Fase 5 — Runtime adapters
- Executar o mesmo contrato em Claude e Pi Agentic Coder.
- Comparar resultados sob condições controladas.
- Documentar incompatibilidades.

### Fase 6 — Org renderer e Decision Log
- Gerar relatório Org e JSON estruturado.
- Ligar fontes, scripts, dados e commits.
- Criar protocolo de revisão.

### Fase 7 — Multiagente seletivo
- Introduzir Source Auditor e Red Team independente.
- Medir ganho de qualidade e custo.
- Só então adicionar outros agentes.

### Fase 8 — Fine-tuning e otimização
- Avaliar apenas quando houver volume de exemplos autorizados e benchmark confiável.
- Comparar com prompt/RAG/Skills/código.
- Manter fallback determinístico.

---

## 19. Três provas de conceito prioritárias

### PoC-1 — Atualização de tese com trilha completa
**Entrada:** conjunto sintético de ITR, release, tese anterior e fontes.  
**Cadeia:** A1 → A2 → P2 → P4 → validator → Org renderer.  
**Critério:** cada número material rastreável; fatos e inferências separados; Red Team com falsificadores; diff de tese.

### PoC-2 — Pesquisa quantamental reproduzível
**Entrada:** dataset histórico sintético ou público com timestamp.  
**Cadeia:** P0 → P3 → quant validator → Red Team estatístico → Org renderer.  
**Critério:** cálculo reproduzível, ausência de look-ahead, testes e limitações explícitas.

### PoC-3 — Claude vs. Pi Agentic Coder
**Entrada:** mesmo Task Contract, Context Pack e fixtures.  
**Cadeia:** MP-ROOT → adapter Claude / adapter Pi → evaluator independente.  
**Critério:** comparar factualidade, completude, portabilidade, custo, latência e retrabalho humano.

---

## 20. Metacrítica — modos de falha e antídotos

| Anti-pattern | Por que falha | Antídoto |
|---|---|---|
| Mega-prompt universal | Mistura objetivos, contexto e critérios | Orquestrador + módulos |
| Prompt chain longa por padrão | Aumenta custo e erro acumulado | Menor cadeia suficiente |
| Agentes em excesso | Paralelismo ornamental e conflitos | Papéis com contrato e teste |
| RAG sem proveniência | Recupera texto sem validar autoridade | Fonte, data, escopo e citação |
| Fine-tuning precoce | Congela padrões antes de conhecer o erro | Baseline e eval primeiro |
| Ranking tratado como decisão | Métrica parcial vira autoridade | Contexto, limites e julgamento |
| Backtest otimizado | Data snooping e overfitting | OOS, walk-forward e baseline |
| Contexto total | Ruído, custo e exposição | Context Pack seletivo |
| Relatório bonito sem auditabilidade | Persuasão substitui evidência | Linhagem e QA |
| Automação sem rollback | Erros propagam-se silenciosamente | Staging, logs e gates |
| Tokenização por entusiasmo | Complexidade supera utilidade | Comparar alternativas sem token |
| Confundir projeto com tração | Narrativa vira falsa validação | Evidência de usuário, receita e retenção |

### 20.1 Filosofema de síntese

\[
\text{Inteligência de Capital}
\neq
\text{Quantidade de Prompts}
\]

\[
\text{Valor do Sistema}
\approx
\text{Qualidade da Evidência}
\times
\text{Reprodutibilidade}
\times
\text{Capacidade de Revisão}
\]

A expressão é heurística, não uma métrica empírica. Se qualquer fator se aproxima de zero, a confiança no resultado também deve cair.

---

## 21. Critérios de conclusão e manutenção

Uma cadeia só pode ser marcada como pronta quando:
- contrato versionado;
- entradas e saídas definidas;
- contexto necessário documentado;
- ferramentas e permissões declaradas;
- critérios de parada e aprovação definidos;
- pelo menos um teste positivo e um adversarial;
- proveniência e limitações registradas;
- formato de relatório testado;
- runtime alternativo documentado, quando portabilidade for requisito;
- responsável e changelog definidos.

Revisar contratos quando:
- fonte ou API muda;
- métrica muda de definição;
- runtime muda comportamento;
- falha relevante é encontrada;
- regra regulatória aplicável muda;
- novo dado revela viés;
- custo de execução supera utilidade.

---

## 22. Próxima ação recomendada

Não converter todos os prompts simultaneamente. Começar por **uma fatia vertical**:

1. MP-ROOT classifica “atualizar uma tese”.
2. O Task Contract define entradas, contexto e saída.
3. Context Builder recupera tese, fontes e documentos.
4. A1 extrai fatos e reconcilia números.
5. P2 executa Red Team.
6. Validator verifica fontes e números.
7. Org Renderer gera relatório.
8. Decision Log registra pendências e aprovação.

Executar primeiro com fixtures sintéticas; depois comparar dois runtimes. Só ampliar quando o teste demonstrar ganho.

**Síntese final:** P0–P6 e A1–A6 deixam de ser uma coleção de prompts para Claude e tornam-se uma biblioteca de protocolos de pesquisa e engenharia. Claude, Pi, ChatGPT ou qualquer outro agente são executores substituíveis; o ativo durável do projeto passa a ser o método versionado, a proveniência, o harness e o histórico de decisões.

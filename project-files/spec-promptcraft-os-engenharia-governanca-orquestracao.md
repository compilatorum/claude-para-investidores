# 🧭 Promptcraft OS — Especificação Integrada de Engenharia, Governança e Orquestração de Prompts

> **Versão:** 1.0 · **Data:** 2026-10-31  
> **Repositório:** compilatorum/claude-para-investidores  
> **Tipo:** especificação funcional, conceitual e técnica para um sistema vivo de promptcraft.  
> **Integração:** Plano de Upgrade I — Inteligência de Capital; Plano de Upgrade II — Engenharia de Sistemas de IA; Meta-Prompt Template Chain; Postman API Platform Blueprint; Machinations Simulation Blueprint; Radar de Nichos Compatíveis.  
> **Status:** blueprint de produto e arquitetura; não implica implementação operacional.  
> **Princípio de entrega:** começar pelo visível (mock/demo navegável), validar o modelo mental e aprofundar por fatias verticais.

---

## 0. Tese central — o melhor prompt encapsula a alma do problema

Um prompt não é apenas uma instrução textual. É uma **interface linguística para um contrato de intenção, contexto, método, transformação e avaliação**. Pode ser tratado como arquétipo, função, comando, formulário, componente de software, instrumento hermenêutico ou chave de uma jornada — desde que a metáfora produza decisões de design testáveis.

> **Filosofema:** “O melhor prompt é aquele que encapsula a alma do problema.”
>
> A alma do problema não é um segredo místico: é sua estrutura essencial — intenção, tensão, contexto, restrições, critérios de sucesso e transformação desejada.

\[
\boxed{Promptcraft = Intent + Context + Method + Constraints + Output Contract + Evaluation}
\]

A evolução proposta:
- Prompt isolado → **ativo versionado e governado**;
- Texto livre → **formulário adaptativo e contrato estruturado**;
- Biblioteca de snippets → **Prompt Hub / Prompt Catalog pesquisável**;
- Prompt gigante → **arquitetura modular, fractal e roteável**;
- “Act as…” → **competência, protocolo, ferramenta e permissão explícitos**;
- Resposta subjetivamente boa → **testes, métricas, logs e avaliação comparativa**;
- Prompting manual → **PromptForge: geração, descoberta, composição e melhoria assistidas**;
- Conversa opaca → **metaconversa com limites, proveniência e reflexão observável**;
- Coleção estática → **repositório vivo JSON + Markdown + tags + templates + testes**.

**Tese de engenharia:** o sistema deve preservar a intenção e o método quando mudam modelo, runtime, agente, interface ou domínio.

## 1. Objetivos e não objetivos

### 1.1 Objetivos
1. Catalogar, criar, descobrir, recomendar, compor, executar, testar, comparar e versionar prompts.
2. Transformar prompts em componentes reutilizáveis de software e funções de workflows.
3. Oferecer formulários de entrada adaptativos: *prompt forms as frontend forms*.
4. Separar instruções, contexto persistente, contexto da tarefa, memória recuperada e dados transitórios.
5. Permitir prompt routing e arquiteturas modulares em múltiplos runtimes (Claude, Pi Agentic Coder, ChatGPT/Codex, Gemini, Roo Code, modelos locais e APIs).
6. Criar promptchains com handoffs tipados e rastreáveis.
7. Tornar governança, segurança, avaliação, custos e drift partes nativas do ciclo de vida.
8. Explorar prompts como arquétipos, comandos, experiências narrativas, instrumentos socráticos e interfaces lúdicas sem confundir metáfora com evidência.
9. Gerar saídas úteis ao trabalho: Markdown, Emacs Org mode, JSON, YAML, relatórios, formulários, artefatos de código e APIs semânticas.
10. Apoiar experimentação e avaliação de LLMs, incluindo otimização sistemática e comparações entre modelos.

### 1.2 Não objetivos
- Não é um prompt único universal nem um “prompt perfeito”.
- Não é uma promessa de que prompting supera fine-tuning, RAG, ferramentas, código ou mudança de modelo.
- Não deve solicitar nem armazenar chain-of-thought privado. Deve registrar racionales concisos, evidências, decisões, verificações e incertezas observáveis.
- Não é terapia, diagnóstico clínico, aconselhamento médico ou substituto de profissional.
- Não é mecanismo para manipular usuários, induzir dependência emocional ou explorar vulnerabilidades.
- Não executa ações externas, altera arquivos, movimenta recursos ou publica conteúdo sem permissões e gates adequados.
- Não presume que todos os prompts precisem de agentes, chains, JSON ou camadas.

## 2. Modelo mental: prompt como arquétipo, função e interface

### 2.1 Três perspectivas complementares

| Perspectiva | Pergunta | Uso |
|---|---|---|
| **Arquétipo** | Que padrão de transformação este prompt representa? | Descoberta, navegação, RPG, famílias de prompts |
| **Função** | Que entradas recebe, que transformação realiza e que saída promete? | Composição, testes, APIs, monorepo |
| **Interface** | Como uma pessoa ou agente configura e aciona essa transformação? | Formulários, comandos, UX, agentes |

Um arquétipo não é essência universal nem categoria psicológica rígida. É um padrão provisório que ajuda a reconhecer semelhanças entre tarefas. Deve poder ser renomeado, dividido, combinado ou descartado.

\[
P : (I,C,M,R) \rightarrow (O,E,H)
\]
Onde I = intenção; C = contexto; M = método; R = restrições; O = saída; E = evidências/estado de avaliação; H = handoff.

### 2.2 Prompt como comando
Cada prompt executável deve possuir identificador, nome, intenção, schema de entrada, instruções e método, ferramentas permitidas, schema de saída, critérios de aceitação, permissões e risco, versão e dependências, exemplos e testes.

Um comando não é apenas uma frase imperativa. É uma operação com contrato e semântica definida.

### 2.3 Prompt forms as frontend forms
O formulário é a interface de configuração do prompt, não um questionário obrigatório em toda interação.

Comportamento adaptativo:
1. Começar com a intenção em linguagem natural.
2. Inferir campos prováveis e mostrar apenas os que mudam materialmente a execução.
3. Perguntar uma lacuna crítica por vez quando possível.
4. Exibir campos avançados sob demanda.
5. Permitir valores parciais, defaults transparentes e “não sei”.
6. Pré-visualizar o prompt compilado e o Context Pack.
7. Distinguir campos fornecidos, inferidos e recuperados.
8. Permitir revisar, executar, salvar como variante ou descartar.

Exemplo: formulário de diagnóstico de tese com pergunta, ativo/empresa, horizonte, evidências disponíveis, restrições, tipo de análise e profundidade. Campos financeiros pessoais nunca devem ser inventados nem preenchidos com dados de personas demonstrativas.

**Frontend inicial:** mock com cartões, filtros, busca, formulário condicional, preview do prompt, botão “simular execução” e painel de resultado sintético. O mock deve exibir claramente que a execução é simulada.

## 3. Ontologia e taxonomia de prompts

A classificação deve ser multi-eixo. Não forçar cada prompt a uma única gaveta.

### 3.1 Eixos de classificação

| Eixo | Exemplos |
|---|---|
| Intenção | descobrir, explicar, diagnosticar, ensinar, criar, transformar, avaliar, decidir, monitorar |
| Arquétipo | Socrático, Tutor, Cartógrafo, Oráculo, Artesão, Red Team, Sintetizador, Curador, Simulador |
| Profundidade | rápido, exploratório, analítico, especialista, recursivo |
| Temporalidade | system, sessão, projeto, tarefa, turno, efêmero |
| Interação | formulário, diálogo, comando, workflow, agente, API |
| Composição | standalone, modular, chain, router, fractal, recursivo |
| Domínio | finanças, quant, software, pesquisa, psicopedagogia, journaling, design |
| Risco | baixo, moderado, alto, crítico |
| Saída | texto, Org, JSON, tabela, código, gráfico, plano, decisão |
| Evidência | sem fonte, fonteada, calculada, experimental, revisada |
| Runtime | Claude, Pi, ChatGPT, Gemini, Roo, local, API, agnóstico |
| Estado | rascunho, experimental, aprovado, depreciado, arquivado |

### 3.2 Prompt Tags Arquetípicas
- #tutor: tutoria, explicação, aprendizagem guiada;
- #socratic: perguntas que refinam hipóteses e explicitam premissas;
- #diagnostic: diagnóstico de problema, situação ou caminho — não diagnóstico clínico;
- #oracle: exploração simbólica, cenários e perguntas geradoras;
- #cartographer: mapeamento de domínio, relações, opções e lacunas;
- #synthesizer: síntese e decantação de informação;
- #red-team: crítica, falsificação e teste de robustez;
- #craft: produção estética, narrativa e artefatos;
- #care: autocuidado não clínico, limites e organização de ações seguras;
- #somatic-reflection: reflexão corporal/autoetnográfica opcional, sem inferir doença;
- #journey: roteiro de jornada, RPG e progressão;
- #meta: metaconversa, metacognição e revisão de processo;
- #research: pesquisa e avaliação de fontes;
- #experiment: desenho experimental e avaliação de LLM;
- #integration: integrar frameworks, ontologias e métodos;
- #automation: execução controlada de workflows.

Tags são facetas, não rótulos identitários do usuário. Não inferir traços psicológicos estáveis a partir de uma resposta isolada.

### 3.3 Tipos funcionais
- **Prompt de tutoria:** ensina por diagnóstico pedagógico, scaffolding, exemplos, prática e feedback.
- **Prompt de diagnóstico:** identifica estado, sintomas operacionais, hipóteses, causas alternativas e próximos testes.
- **Prompt discovery:** converte necessidade vaga em candidatos de prompt e experimentos.
- **Prompt de síntese:** integra fontes e preserva divergências.
- **Prompt de integração de frameworks:** mapeia conceitos, pressupostos, compatibilidades, conflitos e tradução operacional.
- **Prompt metacognitivo:** inspeciona premissas, vieses, confiança e alternativas sem alegar acesso transparente ao pensamento interno do modelo.
- **Prompt de journaling:** perguntas periódicas para registrar experiências, decisões e padrões; posts sociais são sementes opcionais, não fonte clínica.
- **Prompt de experimentação:** define hipótese, conjunto de testes, variáveis, métricas, baselines e critérios de parada.
- **Prompt de autocuidado:** organiza ações de baixo risco, consentidas e adaptáveis; não substitui avaliação profissional.
- **Prompt de diagnóstico de caminho:** compara rotas, custos, compatibilidade, evidências e pequenos experimentos reversíveis.

## 4. Prompt IDE / CASE / CAD — ambiente de autoria

Propor ambiente integrado de criação e manutenção: **Prompt IDE** (edição e execução), **Prompt CASE** (Computer-Aided Software Engineering aplicado a prompts) e **Prompt CAD** (composição visual de módulos e cadeias).

### 4.1 Componentes
1. Prompt Catalog: catálogo navegável, filtros, busca semântica e tags.
2. Prompt Hub: descoberta, recomendações, coleções, novidades e workflows.
3. Prompt Editor: editor Markdown/Org/JSON/YAML com preview.
4. Prompt Form Builder: editor visual de campos, condicionais e defaults.
5. Prompt Graph: grafo de módulos, dependências, routers e handoffs.
6. Prompt Diff: comparação entre versões e variantes.
7. Prompt Playground: execução controlada em diferentes modelos.
8. Prompt Linter: validação estática de estrutura, variáveis, permissões e ambiguidades.
9. Prompt Test Lab: datasets, rubricas, avaliações e baselines.
10. Prompt Logs: histórico de execuções, custos, modelos, resultados e feedback.
11. Prompt Query: linguagem de consulta para localizar e combinar prompts.
12. Prompt Recommender: recomenda prompts e workflows com justificativa e confiança.
13. Governance Console: revisão, aprovação, depreciação e auditoria.
14. Org Exporter: relatórios, checklists e registros para Emacs Org mode.

### 4.2 UX: começar pelo visível
**Demo V0 — sem backend obrigatório:** dashboard com 6–8 arquétipos; biblioteca filtrável; detalhe com metadados; formulário dinâmico; preview compilado; grafo de uma chain; execução simulada com fixture; comparação visual de duas versões.

**V1:** persistência em repositório Git, import/export JSON/Markdown e validação de schema.  
**V2:** adapters para dois runtimes, logs reais, testes automatizados e avaliação comparativa.  
**V3:** roteamento, RAG/context retrieval, recomendações e API semântica.  
**V4:** otimização, telemetria, feedback multimodal e melhoria recursiva supervisionada.

Não construir um IDE completo antes de validar que catálogo + formulário + preview + execução simples resolvem uma tarefa recorrente.

## 5. Metadados, catálogo e repositório vivo

### 5.1 Formato canônico
Adotar JSON/YAML para metadados estruturados e Markdown para instruções legíveis. O registro deve ser versionável, diffável e exportável.

Campos mínimos:
- id estável; name; summary; description;
- version; status (draft, experimental, approved, deprecated);
- archetypes[]; tags[]; domains[];
- intent; when_to_use; when_not_to_use;
- input_schema; output_schema;
- context_policy;
- instructions ou referência ao arquivo Markdown;
- tools[]; permissions; risk_level;
- runtime_compatibility[]; dependencies[]; chain_interfaces;
- examples[]; tests[]; evaluation;
- owner; created_at; updated_at; changelog;
- source_refs[]; provenance; license.

### 5.2 Estrutura proposta
- prompts/registry/ — índice e manifests;
- prompts/archetypes/ — padrões arquetípicos;
- prompts/templates/ — templates parametrizados;
- prompts/chains/ — cadeias e workflows;
- prompts/routers/ — regras de roteamento;
- prompts/forms/ — schemas de formulários;
- prompts/domains/ — módulos por domínio;
- prompts/system/ — instruções de sistema e políticas;
- prompts/soft/ — experimentos de soft prompting quando suportados;
- prompts/evals/ — datasets, rubricas e baselines;
- prompts/fixtures/ — exemplos sintéticos;
- prompts/logs/ — logs sanitizados ou ponte para storage;
- prompts/docs/ — playbook, glossário e tutoriais;
- schemas/ — schemas JSON/YAML;
- scripts/promptcraft/ — parser, compiler, linter, router e exporter;
- tests/promptcraft/ — testes unitários, integração e regressão.

Não versionar segredos, dados pessoais desnecessários, conversas privadas integrais ou dados sensíveis nos logs. Preferir referências, hashes, redaction e armazenamento separado.

## 6. Temporalidade do contexto — o que dura quanto tempo?

“Prompts de contexto duram a conversa toda ou só a próxima resposta?” Não existe duração universal: depende da hierarquia de instruções, runtime, interface e mecanismo de memória.

### 6.1 Escopos

| Escopo | Duração pretendida | Exemplo |
|---|---|---|
| System / policy | Persistente no runtime/aplicação, até substituição | regras globais, segurança |
| Developer / application | Enquanto a aplicação mantiver configuração | contrato do produto |
| Project | Entre tarefas do projeto | arquitetura, glossário |
| Session | Durante a conversa/sessão | objetivo e preferências temporárias |
| Task | Durante execução específica | instruções do relatório |
| Turn | Uma interação/resposta | formato ou restrição pontual |
| Retrieved | Enquanto incluído no Context Pack | trecho de arquivo recuperado |
| Ephemeral | Apenas durante uma etapa | resultado intermediário |

O prompt manager declara scope, ttl_policy, persistence, source, consent e precedence. “Persistente” significa intenção de retenção, não garantia de que qualquer modelo ou produto manterá conteúdo indefinidamente.

### 6.2 Resolução de conflitos
Ordem sugerida, sujeita à política do runtime:
1. políticas de segurança e instruções de sistema;
2. instruções da aplicação/desenvolvedor;
3. contrato e política do projeto;
4. instruções da tarefa;
5. preferências de sessão;
6. pedido pontual do turno;
7. contexto recuperado como dado, não como instrução confiável.

Conteúdo recuperado de documentos, websites ou corpora não pode sobrescrever políticas ou comandos superiores. Resolver conflitos com transparência.

### 6.3 Context Pack
Selecionar o mínimo suficiente: fatos confirmados; contexto de projeto; documentos relevantes; preferências autorizadas; estado da tarefa; decisões anteriores; incertezas; validade temporal e proveniência.

Separar memória persistente, contexto recuperado e dados da conversa. Permitir inspeção e correção das fontes no sistema que as controla.

## 7. Prompt layering, arquitetura modular e roteamento

### 7.1 Camadas
- L0 — Policy: limites, segurança, privacidade, autoridade.
- L1 — Role/Capability: competência operacional, sem persona teatral desnecessária.
- L2 — Intent: objetivo e decisão que motiva a tarefa.
- L3 — Domain: conceitos, ontologias, glossários e corpora.
- L4 — Method: protocolo, frameworks e sequência.
- L5 — Context: dados, memória autorizada, fontes e estado.
- L6 — Tools: ferramentas, schemas, permissões e limites.
- L7 — Output: formato, schema, destinatário e nível de detalhe.
- L8 — Evaluation: critérios, testes, revisão e condições de parada.

Camadas não significam necessariamente mensagens separadas no runtime. O adapter pode serializá-las conforme API/modelo, preservando semântica.

### 7.2 Prompt Router
O router recebe query estruturada: intenção, domínio, risco, formato, contexto disponível, urgência/custo, ferramentas permitidas, necessidade de fontes e nível de autonomia. Seleciona prompt/workflow por regras, tags, compatibilidade e avaliação anterior. Deve explicar “por que este prompt?” e oferecer alternativa. Não escolher cadeia complexa apenas porque ela existe.

### 7.3 Separação de responsabilidades
- Router: escolhe módulos;
- Planner: ordena tarefas;
- Prompt modules: instruções especializadas;
- Context builder: prepara evidências;
- Executor: invoca runtime e ferramentas;
- Validator: verifica saídas;
- Human gate: aprova ações de risco;
- Logger: registra eventos e versões.

Suportar fallback: se módulo/runtime falhar, retornar estado parcial, explicar falha e propor rota alternativa segura.

## 8. Promptchains, workflows e coreografia

### 8.1 Chain como grafo tipado
Uma promptchain é uma sequência ou grafo em que a saída de uma etapa alimenta a próxima. Cada nó declara entradas, saídas, pré-condições, pós-condições, erros e handoff.

\[
P_1 \rightarrow O_1 \rightarrow P_2 \rightarrow O_2 \rightarrow P_3
\]

Handoff estruturado: task_id; status; summary; artifacts; evidence_refs; assumptions; open_questions; confidence; next_action; validation_results.

### 8.2 Padrões
- linear: A → B → C;
- fan-out/fan-in: A → (B,C,D) → E;
- revisão adversarial: Builder → Red Team → Reconciler;
- iterativa: Draft → Evaluate → Revise, com limite;
- condicional: Router → branch;
- hierárquica: Planner → subchains;
- recursiva: síntese → lacunas → nova consulta, com budget e parada;
- humana: etapa exige aprovação antes de continuar.

### 8.3 Promptchain de Síntese — exemplo
1. Extrator: identifica afirmações, fontes, entidades e lacunas.
2. Normalizador: padroniza conceitos sem apagar divergências.
3. Cartógrafo: constrói relações e hipóteses.
4. Red Team: procura contraevidências e alternativas.
5. Sintetizador: produz síntese com níveis de evidência.
6. Tutor: explica resultado e testa compreensão.
7. Logger: registra decisão, versão e perguntas futuras.

Pular etapas desnecessárias e interromper quando evidência for insuficiente.

### 8.4 Engenharia de Prompts Fractal
Aplicar a mesma estrutura em escalas: micro (instrução), meso (prompt modular), macro (chain) e meta (sistema que cria/avalia chains). Recursão nunca infinita: cada escala tem contrato, profundidade máxima, budget e critério de parada.

## 9. Prompt mechanics e engenharia como arte hermenêutica

A tarefa é interpretar a intenção sem reduzi-la à literalidade:
1. **Epoché:** suspender primeira interpretação e identificar ambiguidades.
2. **Contextualização:** situar pergunta no domínio, momento e finalidade.
3. **Distinção:** separar literal, metafórico, tácito, normativo e operacional.
4. **Explicitação:** converter pressupostos em campos e hipóteses.
5. **Composição:** selecionar método, módulos e forma de saída.
6. **Validação:** verificar se a resposta atende ao problema real.
7. **Revisão:** permitir correção da interpretação pelo usuário.

Prompt mechanics, como mecânica da linguagem, investiga como ordem, verbos, exemplos, restrições, contraste, analogias, tags e formatos alteram comportamento. Tratar afirmações causais como hipóteses experimentais, não leis universais.

### 9.1 PromptForge — criador de mágicas de linguagem
Laboratório que propõe estilos a partir de alquimia linguística (transmutação de intenção em forma), ludolinguagem (regras, jogos e restrições criativas), engenharia reversa de manuais (extrair procedimentos), analogias entre domínios, padrões em corpora e feedback avaliado.

O Forge propõe, explica e testa variantes; não canoniza automaticamente estilos inventados. Cada estilo tem nome, definição, caso de uso, contraindicações, exemplo, teste e proveniência.

### 9.2 Flare prompts
“Flare prompt” é tratado como rótulo experimental, não padrão universal estabelecido: prompt curto de ativação que ilumina dimensão, tensão ou pergunta esquecida antes de iniciar uma chain. Exemplo: “Qual premissa invisível, se falsa, invalida este plano?”. O catálogo permite renomear/substituir o termo conforme uso e evidência.

### 9.3 Aesthetic Prompt Design
A estética reforça legibilidade, ritmo, imaginação e compreensão. Símbolos e metáforas devem preservar instruções inequívocas, critérios de sucesso, limites, distinção entre metáfora e fato, acessibilidade e opção de desativar o tema.

## 10. RPG de prompts — seção como jornada navegável

Uma interface RPG pode tornar descoberta e aprendizagem envolventes sem gamificar vulnerabilidades nem transformar a pessoa em “personagem diagnosticado”.

- Mundo/Mapa: domínios e áreas de conhecimento.
- Guildas: coleções por função.
- Arquétipos/Classes: Tutor, Cartógrafo, Oráculo, Artesão, Guardião, Cético.
- Missões: problemas ou tarefas reais.
- Chaves: prompts que destravam etapas metodológicas.
- Relíquias: fontes, frameworks, datasets e artefatos.
- Oficinas: IDE, Playground e Test Lab.
- Diário de bordo: logs e decisões.
- Provas: robustez, Red Team e avaliação.
- XP: progresso em competências verificáveis, não “valor pessoal”.
- Árvore de habilidades: competências e pré-requisitos.
- Campanhas: chains longas com checkpoints e saída reversível.

Cada prompt pode ser uma chave iniciática, mas a interface mostra função concreta, entradas, riscos e resultado esperado. O símbolo convida; o contrato esclarece.

**Jornada: Diagnóstico de Caminho:** convocar intenção → mapear situação → explicitar restrições → gerar rotas → avaliar evidências/custos → escolher experimento reversível → registrar aprendizagem.

**Jornada: Decantação Poética:** recolher fragmentos → identificar imagens/tensões → explorar interpretações → condensar texto → revisar atribuições.

**Jornada: Pesquisa Quantamental:** formular tese → buscar evidências → construir modelo → testar hipóteses → Red Team → registrar decisão e invalidação.

## 11. Metacognição, metaconversa e reflexão

### 11.1 Prompts autoreflexivos híbridos
Combinar análise cognitiva, perguntas socráticas, revisão de premissas e síntese. A IA pergunta sobre o pensamento do usuário sem presumir que conhece sua mente.

Perguntas:
1. Que hipótese estou tratando como fato?
2. Que evidência poderia me fazer mudar de ideia?
3. Qual alternativa plausível ainda não considerei?
4. Que parte vem do contexto e que parte é projeção minha?
5. Onde confundo coerência narrativa com evidência?
6. Qual próxima ação pequena e reversível?

### 11.2 Metaconversa
Revisar o próprio diálogo: a pergunta foi compreendida? A resposta preservou a intenção? Houve excesso de abstração/confiança/complexidade? Que contexto foi usado, inferido ou ignorado? Que informação mudaria materialmente a resposta? Devemos continuar, resumir, mudar método ou encerrar?

### 11.3 Três perguntas críticas permanentes
- Que mitos fundadores esta arquitetura reproduz?
- Que sombras (Jung) estamos projetando nas IAs?
- Como equilibrar eficiência algorítmica com a “alma do sistema”?

São instrumentos de crítica cultural e hermenêutica, não diagnósticos psicológicos do usuário ou da IA. A IA não deve alegar possuir inconsciente, intenção humana ou acesso privilegiado à psique de alguém.

### 11.4 Feedback multimodal
Aceitar feedback textual, ratings, correções, exemplos, áudio/imagem fornecidos pelo usuário e diagramas de fluxo do processo. Não alegar acesso a pensamento interno. Visualizações representam estados observáveis: etapas, dependências, decisões, fontes, incertezas, revisões e handoffs.

## 12. Psicopedagogia, comportamento e integração somática — guardrails

Prompts podem apoiar aprendizagem, auto-observação e organização de experiências. No contexto psicopedagógico-comportamental:
- usar scaffolding, prática deliberada, feedback específico e metacognição;
- distinguir observação, interpretação e hipótese;
- evitar rotular personalidade, neurotipo ou condição clínica;
- não usar tokens, streaks ou recompensas para criar compulsão;
- não inferir vulnerabilidade, diagnóstico ou risco clínico automaticamente;
- permitir pausar, ignorar perguntas e encerrar a jornada;
- não tratar narrativa gerada como memória factual.

**Autocuidado / somático / autoetnográfico:** convidar a descrever sensações voluntariamente, contexto, necessidades percebidas e ações simples de regulação. Não prescrever tratamento, induzir exposição a trauma, fazer diagnóstico ou interpretar sinais corporais como prova de condição. Em sofrimento intenso, risco ou sintomas persistentes, orientar apoio humano qualificado e serviços apropriados.

## 13. Roo Code Modes, “Act as” e agentes no ciclo de programação

“Act as…” é principalmente uma instrução de papel/estilo. Um modo de agente em ambiente de programação tende a combinar papel com workflow, ferramentas, permissões, contexto e comportamento de execução — a implementação varia por produto e versão.

| Elemento | “Act as…” | Mode / Agent workflow |
|---|---|---|
| Papel | Persona ou competência declarada | Função operacional |
| Ferramentas | Não concede ferramentas por si só | Pode integrar ferramentas disponíveis |
| Permissões | Não define controles reais | Pode participar do modelo de permissões |
| Estado | Geralmente textual | Pode manter estado e handoffs |
| Execução | Não executa por semântica própria | Pode ler/editar/testar conforme ambiente |
| Verificação | Só se instruída | Pode incluir etapas e ferramentas de teste |
| Governança | Dependente do prompt | Pode integrar políticas do produto |

**Por que agentes?** Separar planejamento, implementação, teste, revisão, documentação e integração; permitir especialização, paralelismo e validação independente. Não porque agentes sejam sempre melhores. Um modo simples basta para tarefa pequena; agentes agregam valor quando há múltiplas fases, contexto extenso, ferramentas, critérios de aceitação e revisão.

Agente não é sinônimo de prompt longo: é componente de execução com contrato, estado, ferramentas, limites e avaliação. Não presumir equivalência exata entre Roo Code Modes e qualquer framework sem conferir documentação da versão usada.

## 14. Prompt engineering avançado: soft prompts, DSPy e otimização

### 14.1 Explicit prompting versus soft prompting
- **Hard/explicit prompt:** texto legível editado por humanos.
- **Soft prompt:** embeddings ou parâmetros aprendidos inseridos no modelo, normalmente exigindo suporte e processo técnico de treinamento/otimização.
- **Prefix/prompt tuning:** famílias de técnicas de adaptação eficiente; não equivalem a escrever instruções mais elaboradas.

Soft prompts não são normalmente portáveis como Markdown entre fornecedores. Manter separados artefatos de texto e parâmetros aprendidos.

### 14.2 DSPy
DSPy é uma abordagem/framework de programação e otimização de pipelines com LM: especifica módulos, assinaturas e métricas, podendo otimizar instruções ou demonstrações com exemplos e avaliação. Não é botão mágico; depende de dataset, métrica, avaliador, budget e validação fora da amostra.

Fluxo: definir tarefa/assinatura → baseline → dataset representativo e splits → métrica útil → otimização → comparação → testes de robustez/regressão → congelar versão e registrar resultados.

### 14.3 Prompt cache tuning
Cache depende do runtime/provedor e de regras de prefixo, estabilidade e duração. Separar conteúdo estável (instruções/contexto comum) de conteúdo variável (query/dados novos). Medir cache hit, latência, custo e efeitos de mudanças. Nunca sacrificar atualização, privacidade ou correção para aumentar cache hits.

### 14.4 Prompt recommendation in AI code assistants
Recomendar comandos, prompts, Skills, modos e agentes com base em tarefa, repositório, linguagem, ferramentas e risco. Mostrar explicação e compatibilidade; não recomendar agentes com privilégios elevados automaticamente. Uma recomendação útil pode ser “não use agente: este comando simples basta”.

## 15. Prompt metrics, linter e testes

### 15.1 Métricas
| Dimensão | Métrica possível |
|---|---|
| Qualidade | rubrica humana, taxa de aceitação, correção factual |
| Consistência | variância entre execuções, aderência ao schema |
| Robustez | desempenho em casos adversariais e entradas incompletas |
| Utilidade | tempo poupado, retrabalho, taxa de conclusão |
| Eficiência | tokens, custo, latência, cache hit |
| Segurança | violações, vazamento, ações não autorizadas |
| Proveniência | afirmações com fontes e rastreabilidade |
| Portabilidade | qualidade por runtime/modelo |
| Drift | mudança de desempenho ao longo do tempo |
| Experiência | clareza, esforço, abandono, satisfação |

Métricas não devem ser otimizadas isoladamente. Score alto pode mascarar erros ou rubrica mal desenhada.

### 15.2 Prompt Linter
Verificar placeholders sem definição/default; variáveis ambíguas; conflito de instruções; ausência de schema de saída; instruções vagas sem critério; permissões excessivas; dependências incompatíveis; loops sem parada; dados sensíveis desnecessários; prompt injection em conteúdo tratado como instrução; saída sem distinção fato/inferência; falta de exemplos/testes; metadados incompletos; risco não classificado.

O linter não prova que o prompt é bom; detecta defeitos conhecidos.

### 15.3 Testes
Unitários (renderização, interpolação, schemas, roteamento); golden tests; regressão; adversariais; cross-model; avaliação humana; workflow (handoffs, retries, timeout e parada); privacy/security; drift (reexecução periódica). Guardar versão do prompt, modelo, parâmetros, dataset e rubrica. Resultado de um modelo não generaliza automaticamente a outro.

## 16. Prompt drift e gestão do ciclo de vida

Prompt drift é mudança ou deterioração de comportamento por alterações em modelo, contexto, dados, ferramentas, instruções, usuários ou critérios.

- model drift: atualização do modelo;
- context drift: mudança do contexto recuperado;
- data drift: mudança da distribuição de entradas;
- instruction drift: edição acumulada;
- goal drift: deslocamento do objetivo;
- evaluation drift: mudança de rubrica/baseline;
- usage drift: mudança no uso.

Ciclo:
\[
Draft \rightarrow Discover \rightarrow Design \rightarrow Test \rightarrow Review \rightarrow Approve \rightarrow Release \rightarrow Monitor \rightarrow Revise/Deprecate
\]

### 16.1 Versionamento
SemVer para contratos/interfaces quando compatível; versão de conteúdo para ajustes de instrução; changelog com motivação, impacto, testes e compatibilidade; branches para experimentos; tags para releases; rollback; depreciação com prazo e substituto.

Alteração de schema, permissões, semântica de saída ou comportamento de risco pode exigir major. Ajuste editorial sem mudança contratual pode ser patch, se testes confirmarem.

### 16.2 Governança
Definir quem cria/edita/aprova/publica/deprecia; quais prompts usam ferramentas ou dados sensíveis; quais tarefas exigem revisão humana; logs, retenção e consentimento; reporte de falhas; proteção contra injection/abuso; rollback; revisão periódica de prompts de alto impacto.

## 17. Prompt logs, query e descoberta

### 17.1 Logs
Registrar metadados, não necessariamente conversa integral:
run_id; prompt_id; prompt_version; runtime/modelo/parâmetros; timestamp/duração/custo; hashes/referências de contexto; ferramentas/permissões; status/erros/validações; feedback; artefatos/decisões; versão do avaliador.

Redigir segredos e minimizar dados pessoais. Definir retenção e exportação.

### 17.2 Prompt Query
Consulta inicial por domínio, arquétipo, tag, intenção, risco, runtime, formato, status, compatibilidade, métrica mínima e dependências. Exemplo: “encontre prompt socrático de diagnóstico de caminho, risco baixo, exportável para Org e compatível com dois runtimes”.

### 17.3 Prompt discovery e Prompt Playbook
O Playbook ensina a escolher entre prompt, Skill, agente, script, RAG ou fine-tuning; transformar pergunta em contrato; decompor tarefas; desenhar exemplos; avaliar qualidade; identificar drift; publicar/manter; evitar prompt bloat.

**Ficha para analisar exemplo do PromptGenius:** identificar objetivo, estrutura, variáveis, técnicas, limitações, dependência de modelo, licença e como reproduzir/testar. Não atribuir recursos específicos ao produto sem verificar documentação e versão. Exemplo didático genérico: transformar “ajude-me a estudar valuation” em formulário com nível, empresa, método, dados e formato; compilar em prompt tutor; executar; avaliar se ensina corretamente e identifica lacunas. Separar o que foi observado no produto da reconstrução didática.

## 18. API semântica e triggers de promptchains

Propor API semântica que recebe evento/contexto e recomenda ou dispara chain autorizada.

### 18.1 Contrato conceitual
Entrada: query/evento; context_refs; domain; intent; risk; preferências explicitamente autorizadas; runtime_constraints; trigger_policy.

Resposta: selected_prompt; chain_plan; structured_prompt; suggested_response/preview; symbolic_token; required_inputs; permissions; evaluation_plan; provenance; execution_mode (preview, simulate, execute).

“Token simbólico” é inicialmente identificador/ícone/representação semântica, não token financeiro, ativo negociável ou autorização. Separar token de linguagem, token de modelo, token de API e token econômico.

### 18.2 Triggers
Query explícita; mudança de estado; novo arquivo; evento de workflow; cron/schedule; ação do usuário; limiar de métrica. Triggers automáticos exigem allowlist, cooldown, idempotência, rate limit, auditoria e botão de pausa. Nenhum trigger executa ação irreversível sem autorização adequada.

## 19. Corpora, domain knowledge e AI subnet

Construir corpora com glossários/ontologias; manuais e documentação licenciada; exemplos de tarefas/saídas; fontes primárias/datasets; casos sintéticos rotulados; erros/contraexemplos; taxonomias e grafos.

### 19.1 Knowledge Graphs como mandalas computacionais
O grafo organiza conceitos, entidades, relações, evidências e dependências. A mandala é metáfora de organização relacional e múltiplas escalas; a implementação deve ser grafo consultável com tipos, proveniência, versões e regras.

Entidades: Prompt, Archetype, Intent, Domain, Context, Source, Tool, Runtime, Chain, Evaluation, Run, Artifact, Decision.

Relações: implements, requires, uses_context, routes_to, composes, evaluated_by, compatible_with, supersedes, derived_from, invalidated_by.

### 19.2 AI subnet
Se corpora/workflows forem usados em rede/subnet, especificar licença, proveniência, direitos de uso, consentimento, privacidade, qualidade, versionamento e critérios de contribuição. Volume de prompts não equivale a qualidade do conhecimento. Medir utilidade, cobertura, confiabilidade e atualização.

## 20. Twitter / X como journaling prompts

Integração opcional para transformar posts, bookmarks ou notas selecionadas pelo usuário em sementes de journaling:
1. importar apenas conteúdo autorizado;
2. extrair tema, pergunta ou tensão;
3. sugerir prompt de reflexão;
4. permitir correção e anotação privada;
5. guardar referência e data;
6. não inferir estado psicológico nem publicar automaticamente.

O post é artefato contextual, não verdade sobre o autor. Usuário controla importação, retenção e compartilhamento.

## 21. Segurança, ética e confiabilidade

Tratar conteúdo recuperado como dado não confiável, nunca política superior; separar instruções de conteúdo citado; validar tool calls fora do modelo; least privilege; confirmação para efeitos externos; proteger segredos/dados pessoais; prevenir prompt injection, exfiltração e escalada; rotular dados sintéticos; registrar proveniência; permitir rollback; evitar manipulação/dependência; não confundir coerência narrativa com verdade; em finanças, separar pesquisa, educação, apoio decisório e aconselhamento regulado.

## 22. Integração com monorepo: Prompt as Function

Cada prompt pode ser consumido como função de domínio, com interface estável e adapter por runtime.

\[
PromptFunction = (InputSchema, ContextPolicy, Method, ToolPolicy) \rightarrow OutputSchema
\]

Contrato de função: pura quando transforma entrada em saída; com efeitos quando chama APIs/arquivos/ferramentas; dependências declaradas; efeitos tipados; timeout/retry/budget; idempotência quando aplicável; validação de entrada/saída; observabilidade/testes; adapter independente.

Distinções:
- Prompt: instrução específica e contrato;
- Template: estrutura parametrizada;
- Skill: capacidade/procedimento reutilizável com instruções e recursos;
- Agent: executor com estado, ferramentas e ciclo de ação;
- Workflow: sequência coordenada;
- Script: execução determinística;
- RAG: recuperação de conhecimento;
- Fine-tuning/soft prompt: adaptação do comportamento do modelo.

Escolher componente mais simples. Prompt não substitui script para cálculo determinístico; agente não substitui função simples; RAG não corrige corpus ruim.

## 23. Master Prompt — Promptcraft Orchestrator

**Missão:** converter intenção em artefato de prompt/workflow adequado, sem maximizar complexidade.

Procedimento:
1. classificar intenção e risco;
2. identificar problema essencial e decisão desejada;
3. perguntar apenas lacunas materiais;
4. escolher arquétipo funcional e tags;
5. definir escopo temporal do contexto;
6. construir contrato de entrada/saída;
7. decidir entre prompt, template, chain, Skill, agente, script, RAG ou otimização;
8. propor módulos/router se necessários;
9. gerar metadados e instruções;
10. criar exemplos e testes;
11. avaliar variantes quando autorizado;
12. registrar versão, proveniência e limitações;
13. sugerir próximo experimento reversível.

Saída: interpretação da intenção; solução mínima; prompt/workflow compilado; campos/contexto; tags/arquétipos; versão/status; critérios de aceitação; riscos/limitações; testes; changelog.

**Regra de parada:** se prompt curto, pergunta de esclarecimento ou ferramenta determinística resolver, não construir chain.

## 24. Roadmap de implementação

| Fase | Entrega | Critério de aceite |
|---|---|---|
| P0 — Demo visível | Hub, catálogo, cartões, tags, detalhe e mock | usuário entende a proposta |
| P1 — Authoring | Editor, formulário adaptativo, preview e export | criar/exportar prompt válido |
| P2 — Registry | JSON/YAML + Markdown, schemas e Git | diff/versionamento reproduzíveis |
| P3 — Linter & tests | linter, fixtures, golden tests e regressão | detectar erros conhecidos |
| P4 — Chains | grafo, handoffs e execução controlada | chain simples auditável |
| P5 — Runtime adapters | dois runtimes independentes | mesmo contrato com saídas comparáveis |
| P6 — Logs & governance | logs, permissões, aprovação, rollback e drift | auditoria/reversão demonstráveis |
| P7 — Discovery & Forge | recomendações e geração de variantes | melhoria contra baseline |
| P8 — Semantic API | query, triggers e integração | endpoint testado e controlado |
| P9 — Multimodal & graph | feedback multimodal e knowledge graph | dados observáveis e rastreáveis |

### 24.1 Primeiro vertical slice
**Prompt de Diagnóstico de Tese → Promptchain de Síntese → relatório Emacs Org**:
1. catálogo contém prompt tutor e diagnóstico;
2. formulário coleta tese, pergunta, fontes e formato;
3. context builder recupera documentos autorizados;
4. chain extrai evidências, sintetiza e faz Red Team;
5. output gera Org com fatos, hipóteses, lacunas e fontes;
6. testes verificam schema, citações, handoff e status epistemológico;
7. logs registram versão e runtime;
8. humano revisa antes de qualquer decisão de investimento.

## 25. Definition of Done

- catálogo pesquisável e filtrável;
- prompt com metadados, versão e status;
- formulário gera entrada validada;
- preview separa instruções e contexto;
- import/export funcional;
- linter detecta erros estruturais;
- testes comparáveis;
- chain transmite handoffs tipados;
- logs preservam proveniência sem coleta excessiva;
- governance define permissões e rollback;
- pelo menos um workflow real útil e revisado por humano;
- documentação distingue mock, simulação e execução real.

## 26. Metacrítica — riscos de uma arquitetura que se apaixona por si mesma

1. **Prompt bloat:** camadas podem piorar foco/custo. Mitigação: menor cadeia suficiente.
2. **Arquetipização excessiva:** metáforas viram taxonomia rígida. Mitigação: tags revisáveis e multi-eixo.
3. **Recursão sem fim:** metaprompts otimizam indefinidamente. Mitigação: budget, parada e avaliação externa.
4. **Métrica como fetiche:** score não é qualidade universal. Mitigação: métricas múltiplas e avaliação humana.
5. **Confusão entre memória e contexto:** conteúdo recuperado pode estar desatualizado. Mitigação: escopo, timestamp, proveniência e precedência.
6. **Agente por moda:** agentes adicionam estado, risco e custo. Mitigação: comparar com baseline simples.
7. **Estética como verniz:** design não prova utilidade. Mitigação: testar tarefa e compreensão.
8. **Reflexão como pseudo-diagnóstico:** metacognição pode produzir narrativas falsas. Mitigação: linguagem hipotética, alternativas e validação humana.
9. **Automação prematura:** triggers ampliam erros. Mitigação: preview, simulação, aprovação e rollback.
10. **Dependência de fornecedor:** recursos variam entre modelos. Mitigação: contratos canônicos e adapters.

### 26.1 Princípios de melhoria contínua
- **Simplicidade essencial:** começar pela menor representação que preserva intenção.
- **Complexidade justificável:** adicionar camadas apenas diante de falha observada ou requisito concreto.
- **Aprendizagem falsificável:** toda melhoria supera baseline em critérios explícitos, não apenas soa sofisticada.

> **Filosofema final:** “Cada pergunta é um ritual de worldmaking — mas um ritual responsável deixa rastros: intenção, evidência, limites, revisão e liberdade para mudar de ideia.”
>
> **Síntese:** promptcraft é a engenharia da interface entre linguagem e ação. Seu produto não é a frase mais eloquente, mas uma transformação útil, contextualizada, testável, governável e revisável.

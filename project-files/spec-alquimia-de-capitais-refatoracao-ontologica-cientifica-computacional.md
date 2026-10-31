# ⚗️ Spec — Alquimia de Capitais
## Refatoração ontológica, científica e computacional

> Versão 1.0 · 2026-10-31 · Repositório: compilatorum/claude-para-investidores  
> Natureza: blueprint de arquitetura e pesquisa. Não é implementação, recomendação de investimento ou autorização de execução financeira.

## 0. Tese fundadora

Evoluir o sistema de análise de investimentos para uma **Alquimia de Capitais**: uma arquitetura que investiga como recursos heterogêneos são reconhecidos, combinados, transformados, protegidos, distribuídos e regenerados.

A alquimia é uma metáfora operacional e hermenêutica, não uma afirmação de causalidade esotérica. Ela organiza perguntas sobre matéria-prima, conhecimento, processo, catalisador, recipiente, energia, impurezas, produto, perdas e transmutação.

\[
\boxed{\text{Recursos}\xrightarrow{\text{conhecimento + mecanismo}}\text{Capacidades}\xrightarrow{\text{coordenação + execução}}\text{Valor criado}\xrightarrow{\text{direitos + mercado}}\text{Valor capturado}\xrightarrow{\text{reinvestimento}}\text{Capital regenerado}}
\]

**Filosofema:** *Capital não é apenas aquilo que se possui; é aquilo que se consegue mobilizar, transformar e preservar sem destruir as condições de sua própria continuidade.*

A transformação será estudada nas escalas micro (decisão/operação), meso (empresa/projeto/protocolo), macro (mercado/ecossistema/território) e meta (linguagens, modelos, instituições e epistemologias).

### Objetivos

1. Modelar capitais financeiros e não financeiros sem reduzi-los a uma unidade monetária artificial;
2. Explicar mecanismos de transformação e captura de valor;
3. Integrar conhecimento tácito, narrativas, crenças, preços, incentivos e reflexividade;
4. Unir quant research, quant development, análise fundamentalista e economia comportamental;
5. Tratar decisões e operações como hipóteses testáveis, inclusive não agir;
6. Simular alocação, governança e coordenação;
7. Distinguir valor criado, capturado, distribuído, externalizado e regenerado;
8. Preservar proveniência, incerteza, contraditório e auditabilidade.

**Não é:** promessa de monetização, teoria unificada de todos os capitais, motor de previsão infalível, verniz científico para especulação, score universal de pessoas ou licença para agentes executarem transações.

---

## 1. Genealogia intelectual: seis lentes complementares

As referências são lentes de investigação, não dogmas. Esta spec não presume que as obras defendam uma doutrina única nem substitui sua leitura.

### 1.1 Quants: *Quants: The Alchemists of Wall Street*

A matemática aplicada, modelos, dados e infraestrutura computacional podem transformar observações em estimativas, estratégias e decisões.

**Operacionalização:** cada modelo declara objetivo, dados, premissas, domínio de validade, erro, custos e falhas. A vantagem pode estar nos dados, execução, infraestrutura e disciplina, não apenas no algoritmo. Competição e crowding podem erodir o edge.

**Pergunta:** qual transformação computacional produz melhoria incremental, replicável e economicamente relevante frente a um baseline simples?

### 1.2 *Os Magos Desconhecidos*

Conhecimento relevante pode ser tácito, distribuído, especializado ou invisível à descrição institucional dominante.

**Operacionalização:** registrar know-how como observação situada, hipótese ou heurística; mapear comunidades de prática e redes de confiança; distinguir segredo legítimo de informação privilegiada indevida; elicitar, documentar e triangular conhecimento.

**Pergunta:** quais conhecimentos não codificados melhoram decisões, em que contexto e como validá-los sem destruir sua contextualidade?

### 1.3 George Soros — *The Alchemy of Finance*

A reflexividade descreve como participantes interpretam a realidade e agem sobre ela, podendo alterar a própria realidade que tentam compreender.

**Operacionalização:** modelar feedback entre percepção, crença, financiamento, preço, comportamento e fundamentos; separar função cognitiva de função participante; registrar narrativas, posições, fluxos e mecanismos de reforço ou reversão.

\[
P_t\rightarrow B_t\rightarrow A_t\rightarrow F_{t+1}\rightarrow P_{t+1}
\]

Percepção, crença, ação e fundamentos interagem. O esquema é hipótese causal, não identidade universal.

### 1.4 *Cabala do Dinheiro*

Dinheiro e valor também são objetos simbólicos, culturais e institucionais. Moeda, dívida, troca, confiança, legitimidade e significado não se reduzem ao suporte monetário.

**Operacionalização:** estudar dinheiro como unidade de conta, meio de troca, reserva de valor, obrigação e símbolo institucional; distinguir valor econômico, de uso, simbólico, social e moral. Referências cabalísticas/esotéricas são repertório hermenêutico, não evidência causal de performance. Numerologia ou geometria sagrada não serão sinais financeiros sem teste independente.

**Pergunta:** como significados compartilhados e instituições tornam objetos e promessas reconhecíveis como dinheiro e valor?

### 1.5 Peter L. Bernstein — *Against the Gods*

A história do risco é o desenvolvimento de instrumentos intelectuais, matemáticos e institucionais para lidar com futuros incertos.

**Operacionalização:** distinguir risco mensurável, incerteza profunda, ambiguidade e ignorância; registrar limites das distribuições estimadas; estudar probabilidade, seguros, diversificação, derivativos e solvência; estabelecer limites antes de otimizar retorno.

**Pergunta:** que parte da incerteza é mensurável, qual exige prudência e qual deve permanecer fora do modelo?

### 1.6 Rory Sutherland — *Alchemy: The Surprising Power of Ideas That Don't Make Sense*

Comportamento, percepção, contexto, heurísticas e significado podem produzir resultados que modelos lineares não antecipam.

**Operacionalização:** investigar framing, sinalização, conveniência, status, pertencimento, fricção e experiência; tratar ideias contraintuitivas como hipóteses; testar efeitos heterogêneos e colaterais; distinguir valor percebido, disposição a pagar, uso, retenção e resultado econômico.

**Pergunta:** que variável psicológica, simbólica ou contextual explica comportamento tratado como irracional pelo modelo convencional?

### 1.7 Matriz de integração

| Lente | Instrumento | Risco de abuso | Controle |
|---|---|---|---|
| Quants | Estatística e computação | Falsa precisão | Baselines e validação |
| Conhecimento tácito | Elicitação e triangulação | Elitismo/opacidade | Proveniência e contraditório |
| Soros | Feedback e cenários | Narrativa circular | Hipóteses rivais |
| Cabala do dinheiro | Hermenêutica e história | Símbolo confundido com causa | Separação epistemológica |
| Bernstein | Probabilidade e stress | Ilusão de controle | Limites e prudência |
| Sutherland | Experimentos e design | Anedota como lei | Replicação |

---

## 2. Ontologia ampliada: o que está sendo transmutado?

A entidade central deixa de ser apenas ativo, carteira ou trade. Passa a ser **CapitalResource**, associada a capacidades, direitos, compromissos, mecanismos e resultados.

| Domínio | Recursos | Conversões possíveis | Limites |
|---|---|---|---|
| Financeiro | Dinheiro, liquidez, crédito | Juros, dividendos, equity, financiamento | Não elimina risco |
| Cognitivo | Atenção, tempo, energia | Decisão, foco, aprendizagem | Não é infinitamente escalável |
| Intelectual | Conhecimento, método, pesquisa | IP, licenciamento, produto | Contexto e titularidade |
| Computacional | Código, dados, infraestrutura | API, software, produtividade | Manutenção e obsolescência |
| Relacional | Confiança, colaboração, redes | Distribuição, parceria | Não é propriedade sobre pessoas |
| Humano | Competências, experiência, julgamento | Trabalho e inovação | Pessoa não é ativo fungível |
| Empreendedor | Protótipos, validação e execução | Receita, contratos, opções | Protótipo não prova mercado |
| Cultural/simbólico | Linguagem, reputação, legitimidade | Atenção, confiança, adoção | Métricas podem gerar perversidade |
| Institucional | Regras, contratos, governança | Coordenação e previsibilidade | Captura e assimetria |
| Socioambiental | Ecossistemas, território e recursos | Resiliência, bem-estar, impacto | Não presumir substituibilidade |
| Experiencial | Prática e experimentos | Conhecimento incorporado | Aprendizagem exige transferência |
| Opcionalidade | Reversibilidade, acesso, flexibilidade | Capacidade futura de agir | Custo e expiração |

Cada recurso possui unidade, titularidade, escassez, perecibilidade, convertibilidade, externalidades e limites próprios. A moeda pode comparar decisões específicas, mas não será denominador ontológico obrigatório.

### Relações fundamentais

OWNS, ALLOCATES, ENABLES, TRANSFORMS, COMBINES_WITH, SUBSTITUTES_FOR, DEPENDS_ON, CAPTURES, DISTRIBUTES_TO, EXTERNALIZES_TO, REGENERATES, DEPLETES, MEASURES, GOVERNS e SIGNALS. Cada relação registra fonte, contexto, período, confiança e contestabilidade.

### Estoques, fluxos e capacidades

- Estoque: recurso acumulado em um instante;
- Fluxo: entrada, saída ou transformação por unidade de tempo;
- Capacidade: possibilidade de produzir ou mobilizar fluxos futuros.

\[
K_{t+1}=K_t+I_t-D_t-L_t
\]

Molde contábil: K é estoque, I adição/investimento, D depreciação e L perdas. Cada domínio exige definição própria e pode não admitir agregação escalar.

**Capital não é sinônimo de valor:** recurso é mobilizável; capital é recurso organizado para produzir capacidades; valor criado é benefício frente a contrafactual; valor capturado é parcela apropriada; valor distribuído é alocação entre partes; valor regenerado recompõe condições futuras; custo externalizado é encargo transferido a terceiros.

---

## 3. Processo alquímico: pipeline operacional

A sequência é metáfora de processo, não lei natural.

### Nigredo — decomposição e diagnóstico
Desagregar narrativas em claims; identificar recursos, restrições, dívidas, dependências e externalidades; detectar premissas ocultas; separar dados, inferências, opiniões e símbolos.

**Artefatos:** mapa de recursos/dependências, claim ledger, risk register e baseline.  
**Gate:** objeto, unidade de análise e dados essenciais definidos.

### Albedo — purificação e proveniência
Qualificar fontes, remover duplicações, estabelecer data-base e lineage, separar evidência primária de comentário, registrar incertezas e construir argumento contrário.

**Artefatos:** evidence ledger, source manifest, data contract e red-team memo.  
**Gate:** claims críticos possuem fonte ou status explícito de hipótese.

### Citrinitas — iluminação e modelagem
Construir mecanismo causal, identificar agentes/incentivos/restrições, mapear feedbacks, comparar hipóteses, construir cenários e escolher baseline simples.

**Artefatos:** causal graph, system map, model card e hypothesis registry.  
**Gate:** declarar limites e condições de invalidação.

### Rubedo — realização e captura
Executar experimento, protótipo, piloto ou operação autorizada; medir custos e resultados; verificar direitos econômicos e distribuição; comparar com contrafactual.

**Artefatos:** experiment run, transaction log, value-capture map e postmortem.  
**Gate:** sem evidência de uso, pagamento ou mecanismo demonstrado, não declarar captura validada.

### Regeneratio — reinvestimento e continuidade
Reinvestir com critérios explícitos; preservar liquidez, conhecimento, infraestrutura e relações; medir depreciação; reduzir dependências; rever governança; encerrar mecanismos destrutivos.

**Artefatos:** regeneration ledger, maintenance budget e resilience report.  
**Gate:** crescimento de indicador não prova regeneração se houver consumo oculto de recursos.

\[
Nigredo\rightarrow Albedo\rightarrow Citrinitas\rightarrow Rubedo\rightarrow Regeneratio
\]

O processo não é linear: novas evidências podem exigir retorno a qualquer estágio.

---

## 4. Reflexividade, narrativas e alquimia comportamental

Modelo mínimo:

\[
N_t\rightarrow B_t\rightarrow A_t\rightarrow(F_{t+1},P_{t+1},G_{t+1})\rightarrow N_{t+1}
\]

N é narrativa; B crença; A ação/alocação; F fundamentos; P preço/valor percebido; G governança. Feedback pode reforçar, balancear, atrasar, saturar ou romper. Reflexividade exige mecanismo identificável, não apenas movimento de preço.

Cada narrativa monitorada registra claim, origem, emissores, público, evidências favoráveis e contrárias, incentivos, difusão, decisões associadas, mecanismo de alteração dos fundamentos, condições de ruptura e risco de manipulação.

Biblioteca comportamental: framing, sinalização, reputação, identidade, pertencimento, conveniência, fricção, aversão à perda, reciprocidade, status, familiaridade, escassez percebida, ritual, surpresa e efeito de rede.

Cada mecanismo contém definição, contexto, previsão observável, moderadores, explicações rivais, riscos de manipulação, experimento e limites éticos.

**Metacrítica:** narrativa não é necessariamente mentira; fundamento não é necessariamente independente da narrativa. Investigar quando a narrativa descreve, coordena, distorce ou transforma a realidade.

---

## 5. Conhecimento tácito e os “magos”

| Tipo | Exemplo | Tratamento |
|---|---|---|
| Explícito | Relatório, código, contrato, dataset | Versionar e citar |
| Tácito | Heurística prática | Contexto e limites |
| Procedural | Saber executar | Workflow e exceções |
| Relacional | Saber cooperar/consultar | Consentimento e reciprocidade |
| Institucional | Regras formais e informais | Distinguir norma e prática |
| Corporificado | Habilidade incorporada | Observar sem reduzir a texto |
| Emergente | Insight sem explicação | Hipótese exploratória |

**Protocolo:** capturar contexto; pedir exemplos e contraexemplos; identificar pistas; reconstruir ações e alternativas; distinguir regra consciente de intuição; definir domínio de validade; triangular com dados/especialistas; testar novos casos; preservar autoria e dissenso; atualizar ou arquivar.

Não explorar informação confidencial, segredo comercial alheio ou informação privilegiada para vantagem indevida. Conhecimento reservado não é sinônimo de conhecimento ilícito.

---

## 6. Engenharia quantitativa e edge

Pipeline: aquisição de dados → contratos e lineage → limpeza/corporate actions → features → especificação do modelo → baseline/ablation → separação temporal treino-validação-teste → walk-forward/out-of-sample → custos/slippage/capacidade → robustez/regimes → Red Team → reprodutibilidade → decision memo.

\[
Edge_{net}=Benefit_{incremental}-Fees-Slippage-Impact-Data-Compute-Maintenance-Risk
\]

Edge só é declarado frente a baseline, período, universo, custos e restrições. Resultado histórico não garante persistência.

Controles: survivorship bias, look-ahead bias, data leakage, selection bias, multiple testing, p-hacking, regime shift, non-stationarity, autocorrelação, overfitting, slippage, spread, market impact, capacity, crowding, benchmark inadequado, incerteza de parâmetros, erros de implementação e risco de modelo/dados.

Cada conclusão decompõe observação de fonte, transformação determinística, cálculo estatístico, regra simbólica, interpretação contextual, inferência de IA, julgamento humano e decisão autorizada. LLM apoia pesquisa e síntese; não é fonte primária nem calculadora confiável sem verificação.

---

## 7. Governança de smart money

“Smart money” não é identidade conferida por riqueza, status ou fama. Avaliar histórico documentado, qualidade de evidência, gestão de risco, alinhamento de incentivos, horizonte, transparência de conflitos e robustez ajustada a custos/risco. Desempenho passado não prova habilidade persistente.

Separar direitos de propor, deliberar, votar, vetar, executar, custodiar, auditar, distribuir, alterar parâmetros e encerrar.

\[
Propor\neq Avaliar\neq Aprovar\neq Executar\neq Custodiar\neq Auditar
\]

Token, reputação, contribuição, capital investido e expertise não concedem automaticamente os mesmos direitos.

Simular: one-person-one-vote, token-weighted voting, quadratic voting, conviction voting, delegação, comitês, multisig, futarchy, grants retroativos, matching funds, crowdfunding, revenue sharing, bounties, microtarefas e mercados de previsão.

Avaliar concentração, plutocracia, Sybil, captura, apatia, manipulação, coordenação, accountability e distribuição. Simular permissões antes de conectar wallets, contratos ou contas reais.

---

## 8. Regeneração, externalidades e antirruína

Uma oportunidade não é regenerativa porque usa essa palavra. Investigar estoque restaurado, recursos consumidos, beneficiários, custos suportados, contrafactual, adicionalidade, permanência, reversibilidade, dependência de subsídio e internalização de custos.

Painel multidimensional: fluxo financeiro líquido/solvência/runway; tempo de decisão/retrabalho; reuso/replicação/licenças; disponibilidade/custo/latência; reciprocidade/colaboração; uso/retenção/pagamento/margem; outcome/adicionalidade/permanência; participação/concentração de poder.

Salvaguardas: limites de perda, liquidez, runway, diversificação de dependências, reversibilidade, redundância, opções de saída, custos fixos baixos, testes pequenos e proteção de custódia/contraparte.

---

## 9. Arquitetura-alvo: Capital Alchemy OS

| Camada | Responsabilidade | Componentes candidatos |
|---|---|---|
| L0 Ontologia | Capitais, recursos, agentes e direitos | CapitalResource, Capability, Right, Actor |
| L1 Evidence | Fontes, claims e proveniência | SourceRegistry, EvidenceLedger |
| L2 Knowledge | Teses, narrativas e heurísticas | ThesisRegistry, NarrativeMap |
| L3 Mechanisms | Transformação, captura e distribuição | MechanismGraph, ValueCaptureMap |
| L4 Quant Engine | Dados, estatística e modelos | DataPipeline, FeatureStore, ModelRegistry |
| L5 Simulation | Cenários e governança | ScenarioEngine, MechanismSimulator |
| L6 Experiment | Protocolos, runs e resultados | ExperimentRegistry, RunLedger |
| L7 Allocation | Comparação e decisões | OpportunityEngine, AllocationProposal |
| L8 Governance | Direitos, aprovações e auditoria | PolicyEngine, ApprovalWorkflow |
| L9 Interface | WebApp, Org, relatórios e GenUI | UI, OrgExporter, API |
| L10 Learning | Pós-mortem e regeneração | DecisionJournal, LearningLoop |

Fluxo: Inquiry → Evidence → Ontology → Mechanism → Model → Experiment → Governance → Allocation → Outcome → Learning.

Entidades mínimas: CapitalResource, CapitalStock, CapitalFlow, Capability, Actor, Right, Opportunity, Mechanism, Narrative, Claim, Evidence, Thesis, Experiment, ExperimentRun, AllocationProposal, Decision, ValueCapture, Distribution, Externality, RegenerationEvent, GovernanceRule e Risk.

Toda entidade crítica contém ID estável, timestamp, versão, autor/origem, namespace, proveniência, estado epistêmico, confiança justificada, escopo temporal, permissões, relações e histórico.

Namespaces: demo (personas fictícias), synthetic (dados artificiais), research (pesquisa pública), personal (dados fornecidos e autorizados) e production (dados operacionais reais, se existirem). Não publicar dados pessoais, secrets ou chaves. Não confundir persona demonstrativa com situação financeira real.

---

## 10. Integração com os artefatos existentes

Esta spec integra, mas não substitui:
- plano-upgrade-inteligencia-de-capital.md — ontologia ampliada e decisão;
- plano-upgrade-ii-engenharia-de-sistemas-ia-quant-developer.md — execução, contratos e harness;
- meta-prompt-template-chain-inteligencia-de-capital.md — compilação de intenção em tarefa;
- spec-promptcraft-os-engenharia-governanca-orquestracao.md — interface linguística e orquestração;
- spec-laboratorio-ciencia-computacional-quant-research-governanca-smart-money.md — método científico;
- machinations-simulation-blueprint.md — simulação;
- teses-de-investimento.md — teses e falsificadores;
- radar-nichos-compativeis.md — descoberta de oportunidades;
- postman-api-platform-blueprint.md — contratos e testes;
- perfil-investidor-joao.md — preferências qualitativas, sob controle de privacidade.

Esta spec define metáfora integradora, ontologia e processo. Specs especializadas mantêm autoridade sobre seus métodos. Conflitos geram ADR, não duplicação silenciosa.

---

## 11. Roadmap incremental

**P0 — Inventário:** mapear código, scripts, skills, UI, dados e documentos; identificar duplicações; glossário; auditar namespaces; ADRs. Aceitação: mapa rastreável sem reescrita precipitada.

**P1 — Ontologia:** schemas de CapitalResource, Capability, Opportunity, Mechanism, Claim, Evidence, Thesis, Experiment e Decision; IDs, enums, versionamento, fixtures sintéticas e testes. Aceitação: schemas determinísticos e documentação.

**P2 — Evidências:** claim ledger, fontes, narrativas, mecanismos, falsificadores, hipóteses rivais e exportação Org. Aceitação: tese auditável até a fonte e argumento contrário.

**P3 — Laboratório:** pipeline alquímico, protocolos, runs, análise quantitativa/qualitativa/comportamental, postmortem e learning loop. Aceitação: experimento sintético completo, inclusive resultado nulo.

**P4 — Simulação/governança:** recursos, fluxos, agentes abstratos, incentivos, direitos e cenários adversos. Aceitação: simulações identificadas, parametrizadas e limitadas.

**P5 — Interface/alocação:** comparação multidimensional, grafo de transformação, UI modular e feature flags. Aceitação: mecanismo, evidência, incerteza e captura legíveis.

**P6 — Integrações:** OpenAPI, Postman, adaptadores de agentes, Org exporter, CI, logs, observabilidade e aprovação humana. Aceitação: contrato comum em dois runtimes com logs.

**P7 — Validação externa:** entrevistas, testes cegos, pilotos, disposição a pagar e revisão independente. Aceitação: evidência externa separada de opinião e demonstração técnica.

---

## 12. Experimento vertical prioritário

**Pergunta:** o mapa explícito de recursos → mecanismos → captura → distribuição → regeneração melhora a análise frente a uma ficha convencional?

- A (baseline): análise centrada em ativo, risco, retorno e tese;
- B (intervenção): ontologia de capitais e mapa de transformação;
- Unidade: pequeno conjunto de oportunidades sintéticas/públicas;
- Avaliação: completude, rastreabilidade, mecanismos, riscos omitidos, captura, tempo e custo;
- Revisão: avaliador independente/Red Team com critérios prévios;
- Saída: relatório comparativo em Org.

Hipóteses: B identifica mais mecanismos; separa melhor criação/captura; reduz omissões de externalidades; aumenta tempo/complexidade; seu ganho depende da classe de oportunidade. São hipóteses, não resultados.

Escopo mínimo: uma oportunidade de software/serviço, uma financeira convencional e uma de grant. Nenhuma transação real é necessária.

---

## 13. Métricas sem score universal

\[
\mathbf{V}(o)=[V_f,V_c,V_i,V_{comp},V_r,V_e,V_s,V_o]
\]

Vetor de dimensões financeira, cognitiva, intelectual, computacional, relacional, empreendedora, socioambiental e opcionalidade. Não pressupõe unidade comum.

Usar vetores, fronteiras de Pareto, cenários, dominância parcial, restrições não compensatórias, preferências declaradas e sensibilidade. Score composto exige pesos, escalas, normalização e compensações explícitos; mostrar sempre o painel original.

---

## 14. Prompt mestre para agentes

**Papel:** arquiteto de Alquimia de Capitais, quant researcher, quant developer e auditor epistemológico.

**Missão:** analisar oportunidade como transformação de recursos em capacidades, valor criado, capturado, distribuído e regenerado.

**Procedimento:** definir objeto/escala; identificar capitais; separar estoque/fluxo/capacidade; mapear atores/direitos/incentivos; decompor narrativas em claims; vincular evidências; modelar mecanismos e hipóteses rivais; analisar reflexividade; estimar riscos/custos/externalidades; identificar criação/captura/distribuição; avaliar regeneração/depleção; propor experimento mínimo; declarar limites; produzir Org/Markdown e dados estruturados; submeter a Red Team.

**Proibições:** não converter metáforas em fatos; não inventar dados; não tratar riqueza/reputação como competência; não confundir interesse e demanda; não tratar token como equity/direito sem contrato; não precificar toda dimensão humana; não omitir custos; não executar transações sem autorização.

**Saída:** objeto/pergunta; mapa de capitais; mecanismo; narrativas/reflexividade; evidências/lacunas; criação/captura/distribuição; riscos/externalidades; regeneração/depleção; experimento; falsificadores; decisão provisória; limites.

---

## 15. Metacrítica

| Falha | Sintoma | Salvaguarda |
|---|---|---|
| Metáfora excessiva | Vocabulário sem mecanismo | Operacionalização e teste |
| Fetiche quantitativo | Score parece objetivo | Unidade, proxy e incerteza |
| Esoterização | Símbolo como causa | Separar hermenêutica e evidência |
| Elitismo epistêmico | “Mago” incontestável | Proveniência e falsificadores |
| Narrativa circular | Crença valida a si mesma | Hipóteses rivais |
| Reducionismo financeiro | Tudo vira preço | Unidades plurais |
| Moralização regenerativa | Intenção vira impacto | Contrafactual e adicionalidade |
| Tecnossolucionismo | Modelo substitui instituição | Direitos e accountability |
| Complexidade ornamental | Framework sem uso | Remover módulo inútil |
| Otimização prematura | Score sem demanda | Validar problema e usuário |

**Filosofema:** *A pedra de toque de um modelo não é explicar tudo; é revelar onde falha.*

## 16. Definition of Done

A refatoração estará implementada quando ontologia e schemas estiverem testados; estoque/fluxo/capacidade diferenciados; claims e evidências rastreáveis; mecanismos e captura explícitos; capitais não financeiros mantiverem unidades próprias; experimentos tiverem protocolo/resultados/limites; simulações forem identificadas; governança separar propor/avaliar/aprovar/executar/auditar; externalidades e regeneração documentadas; dados pessoais e sintéticos segregados; fluxo reproduzível em mais de um runtime; testes e Red Team cobrirem o vertical slice; e usuários externos validarem necessidade antes de declarar product-market fit.

## 17. Síntese

\[
\boxed{\text{Alquimia de Capitais}=\text{Ontologia}+\text{Evidência}+\text{Mecanismos}+\text{Experimentação}+\text{Governança}+\text{Regeneração}}
\]

A matemática oferece instrumentos; o conhecimento tácito, pistas; a reflexividade, feedbacks; a hermenêutica, significados; a história do risco, prudência; a economia comportamental, variáveis invisíveis. Nenhuma lente basta isoladamente.

**Filosofema final:** *Não transformar chumbo em ouro por decreto; descobrir, com método, quais combinações de recursos, conhecimento e confiança podem produzir valor — e quais custos não devem ser escondidos no cadinho.*

## Referências de enquadramento

- *Quants: The Alchemists of Wall Street* — matemática aplicada aos mercados.
- *Os Magos Desconhecidos* — conhecimento reservado, tácito ou pouco visível.
- George Soros, *The Alchemy of Finance* — reflexividade.
- *Cabala do Dinheiro* — dimensão simbólica e esotérica do dinheiro e do valor.
- Peter L. Bernstein, *Against the Gods: The Remarkable Story of Risk* — probabilidade e gestão do risco.
- Rory Sutherland, *Alchemy: The Surprising Power of Ideas That Don't Make Sense* — comportamento, percepção e valor contraintuitivo.

**Nota bibliográfica:** títulos e atribuições foram mantidos conforme fornecidos. Antes de bibliografia acadêmica formal, completar autor, edição, ano e editora de cada obra, especialmente das referências sem autoria/edição inequívoca.

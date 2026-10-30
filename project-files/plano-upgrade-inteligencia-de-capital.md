# 🧭 Plano de Upgrade — Claude para Investidores → Sistema de Inteligência e Alocação de Capital

> **Versão:** 1.0 · **Data:** 2026-10-30  
> **Repositório:** `compilatorum/claude-para-investidores`  
> **Natureza:** plano arquitetural e de execução; não é recomendação de investimento, política pessoal de alocação nem declaração de suitability.  
> **Objetivo:** fechar o gap entre o sistema efetivamente implementado no repositório e o universo de problemas, teses e formas de investimento desenvolvidos nas conversas do usuário.

---

## 0. Tese central do upgrade

O repositório evoluiu de uma engenharia reversa de ferramentas de IA para análise de investimentos em um conjunto que já contém:

- WebApp com modos v1.0/v2.0 e 17 abas;
- prompts analíticos, scripts Python e geração de dados sintéticos;
- Skills para análise de ITR/DFP, Red Team, DCF/valuation, radar de fatos e compliance;
- documentação de formação e arquitetura de IA;
- memória qualitativa do investidor;
- catálogo de teses em diferentes classes de ativos e formas de capital.

Entretanto, o sistema ainda está organizado predominantemente em torno do **analista de uma carteira financeira convencional**. O contexto intelectual do usuário aponta para algo mais amplo: um sistema de inteligência que compare oportunidades de alocação de dinheiro, tempo, atenção, conhecimento, software, propriedade intelectual, relações, reputação, capacidade empreendedora e recursos socioambientais.

**Direção do upgrade:**

[
\text{Analisador de Carteira}
\longrightarrow
\text{Sistema de Inteligência de Capital}
\longrightarrow
\text{Sistema de Decisão e Aprendizagem}
]

O sistema não deve tentar monetizar tudo nem transformar toda dimensão da vida em preço. Deve tornar explícitos os recursos alocados, os mecanismos de criação e captura de valor, os riscos, as evidências, as externalidades e os custos de oportunidade.

**Filosofema:** *Investir é comprometer recursos presentes para ampliar possibilidades futuras; inteligência de capital é saber o que está sendo comprometido, por qual mecanismo e sob quais condições a decisão deixa de fazer sentido.*

---

## 1. Diagnóstico do estado atual

### 1.1 O que já existe — preservar e reutilizar

| Camada | Artefatos observados | Papel atual | Decisão |
|---|---|---|---|
| Interface | `index.html`, WebApp 17 abas | Interface de análise financeira e construção de prompts | Preservar; evoluir por módulos |
| Engenharia de prompts | `ENGENHARIA_REVERSA_V1_MASTERCLASS.md`, `UPGRADE_V2_ARSENAL_E_FORMACAO_COMPLETA.md` | Método de trabalho com IA | Reaproveitar como camada de execução, não como ontologia total |
| Testes | Playwright, dados sintéticos, relatório E2E | Verificação de fluxos e estados da UI | Ampliar para testes semânticos, financeiros e de segurança |
| Dados | scripts P0/P1/P3/A4 e datasets sintéticos | Sanitização, consolidação, ranking e auditoria de DCF | Manter; desacoplar dados de demonstração dos dados reais |
| Skills | ITR, Red Team, DCF, radar, compliance | Análise de ações e carteira brasileira | Preservar como domínio especializado |
| Memória | `perfil-investidor-joao.md` | Preferências, filosofia e estilo | Manter como memória qualitativa |
| Teses | `teses-de-investimento.md` | Biblioteca de hipóteses | Evoluir para registro vivo, versionado e ligado a evidências |
| Fontes | `project-files/fontes.md` | Hierarquia de fontes para carteira demonstrativa | Separar fontes gerais, fontes por domínio e fontes por ativo |

### 1.2 Diagnóstico crítico

O README descreve uma implementação extensa, mas a cobertura E2E de 23/23 testes representa a aprovação dos fluxos testados — **não prova, por si só, correção econômica, validade das hipóteses, qualidade de dados, robustez estatística ou adequação de recomendações**.

Há também um problema de configuração: `project-files/perfil.md` contém um perfil demonstrativo (Rafael, 42 anos, R$ 300 mil, limites e posições exemplificadas). Esse conteúdo não pode ser interpretado como a situação financeira do usuário. O mesmo cuidado se aplica a tickers, taxas, limites, metas, números e dados de carteira usados em fixtures.

### 1.3 Gaps de primeira ordem

1. **Ontologia estreita:** carteira financeira é o centro; capital ampliado aparece em documentos, mas não como objeto operacional do sistema.
2. **Separação insuficiente entre pessoa, demonstração e experimento:** memória qualitativa, dados sintéticos e situação real precisam de namespaces e controles distintos.
3. **Teses sem ciclo de vida completo:** o catálogo descreve hipóteses, mas ainda precisa de proveniência, evidências, atualização, dependências, decisão, resultado e calibração.
4. **Ausência de um motor unificado de alocação:** não há uma camada comum para comparar uma ação, um título, um grant, um micro-SaaS, uma contribuição open source ou um projeto de impacto.
5. **Captura de valor pouco formalizada:** é necessário separar criação de valor, beneficiário, pagador, titularidade, direito econômico, liquidez e captura pelo investidor/contribuidor.
6. **Capital empreendedor e não financeiro pouco operacionalizado:** projetos, serviços, microtarefas, IP, grants, pilotos e receitas precisam de pipeline e contabilidade próprios.
7. **Reflexividade e conhecimento tácito ainda não são módulos de decisão:** narrativas, crenças, redes, sinais qualitativos e conhecimento não codificado precisam de tratamento explícito sem falsa objetividade.
8. **Risco transversal incompleto:** risco financeiro, técnico, jurídico, de governança, custódia, contraparte, execução, concentração de atenção e custo de manutenção devem conversar entre si.
9. **Ausência de um diário de decisões e de aprendizagem integrado:** falta fechar o circuito hipótese → decisão → resultado → revisão.
10. **Arquitetura de IA centrada em prompts:** falta uma camada de orquestração que escolha ferramenta, agente, fonte, teste e nível de autonomia conforme a tarefa.

---

## 2. Modelo-alvo: ontologia de capital e oportunidades

### 2.1 Domínios de capital

O sistema deve aceitar múltiplas classes de recursos sem presumir que todas sejam fungíveis ou comparáveis em uma única unidade monetária.

| Domínio | Recursos alocados | Formas possíveis de retorno | Métricas / evidências |
|---|---|---|---|
| Financeiro | Dinheiro, liquidez, crédito | Juros, dividendos, valorização, preservação, opcionalidade | Retorno líquido, risco, liquidez, drawdown, custo |
| Cognitivo | Atenção, tempo, energia mental | Melhor decisão, foco, redução de incerteza | Tempo poupado, decisões melhoradas, fadiga, custo de contexto |
| Intelectual | Pesquisa, método, know-how, corpus | IP, licenciamento, autoridade demonstrada, produto | Proveniência, originalidade, reutilização, adoção, pagamento |
| Computacional | Código, dados, automação, infraestrutura | Software, API, produtividade, serviço | Confiabilidade, custo total, latência, reutilização, usuários |
| Relacional | Confiança, colaboração, rede | Distribuição, acesso, cooperação, oportunidades | Reciprocidade, conversões, parcerias, resultados |
| Empreendedor | Protótipos, execução, validação | Receita, participação, contratos, opções de crescimento | Problema validado, uso, retenção, margem, receita |
| Socioambiental | Trabalho, recursos naturais, financiamento | Impacto, resiliência, serviços ecossistêmicos, valor público | Adicionalidade, permanência, MRV, resultados e contrafactual |
| Experiencial | Experimentos, vivências, prática | Conhecimento incorporado e capacidade transferível | Aprendizagem aplicada, mudança de capacidade, transferência |

**Regra de modelagem:** não converter automaticamente reputação, pontos, tokens, impacto, aprendizagem ou código em dinheiro. Registrar dimensões em unidades próprias e, quando houver conversão econômica, explicitar o mecanismo e a evidência.

### 2.2 Tipos de oportunidade

Cada oportunidade deve ser classificada em uma ou mais classes:

- Ativo financeiro negociado;
- Crédito, dívida ou estrutura de financiamento;
- Participação societária ou micro-venture;
- Projeto open source, software, API ou propriedade intelectual;
- Serviço, curadoria, consultoria especializada ou produto;
- Grant, bounty, prêmio, mecenato, crowdfunding ou financiamento público;
- Protocolo, DAO, mecanismo DeFi ou infraestrutura Web3;
- Ativo tokenizado, direito econômico ou licença;
- Projeto socioambiental, ReFi ou bem público;
- Competência, aprendizagem, ferramenta ou relação estratégica.

### 2.3 Taxonomia de fontes de capital

Não tratar fontes de financiamento como equivalentes:

| Fonte | O que representa | O que não representa automaticamente |
|---|---|---|
| Receita de cliente | Pagamento por valor entregue | Grant ou investimento |
| Grant | Capital de desenvolvimento sob regras do programa | Receita recorrente ou equity |
| Bounty | Pagamento condicionado a uma entrega | Emprego ou demanda recorrente |
| Prêmio | Reconhecimento e capital condicionado a critérios | Mercado validado |
| Piloto pago | Evidência de disposição a pagar | Retenção ou escala |
| Licenciamento | Remuneração pelo uso de IP/direitos | Transferência total de propriedade |
| Revenue sharing | Participação contratual em receitas | Retorno garantido |
| Crowdfunding/mecenato | Apoio coletivo a uma finalidade | Direito financeiro, salvo estrutura explícita |
| Equity | Participação societária e direitos associados | Liquidez ou controle |
| Token | Unidade definida por protocolo/contrato | Ação, moeda, receita, propriedade ou direito de resgate |
| Crédito | Obrigação de pagamento | Capital sem custo ou risco |

---

## 3. Frameworks intelectuais que devem se tornar mecanismos operacionais

### 3.1 Alquimia do Capital — conhecimento tácito, narrativas e reflexividade

Formalizar o circuito:

[
\text{Conhecimento tácito}
\rightarrow \text{Narrativas}
\rightarrow \text{Crenças}
\rightarrow \text{Alocações}
\rightarrow \text{Preços / incentivos}
\rightarrow \text{Realidade modificada}
\rightarrow \text{Novo conhecimento}
]

Referências como Soros, Polanyi, Taleb, Graham, Fama/French, Shiller e Rory Sutherland devem funcionar como lentes concorrentes, não como autoridades que substituem evidência.

Requisitos:
- Distinguir fundamento, percepção, narrativa, posicionamento e fluxo;
- Registrar quem acredita, quem age, quem financia e quem captura;
- Detectar causalidade reversa e reflexividade;
- Diferenciar sinal qualitativo, proxy mensurável e fato confirmado;
- Preservar conhecimento tácito sem transformá-lo prematuramente em regra;
- Registrar o que faria a interpretação mudar.

### 3.2 Quantamental e neurossimbólico

Combinar:
- Dados quantitativos e séries temporais;
- Fundamentos econômicos e financeiros;
- Documentos e evidências primárias;
- Conhecimento tácito e interpretação contextual;
- Regras simbólicas, ontologias e relações causais;
- Modelos estatísticos e probabilísticos;
- Revisão humana e Red Team.

O sistema deve explicar **qual parte da conclusão veio de dado, cálculo, regra, interpretação humana ou saída de modelo**. LLM não é fonte factual nem oráculo infalível.

### 3.3 Risco, antirruína e assimetria

Expandir o risco para além da volatilidade:
- Perda permanente de capital;
- Risco de liquidez e venda forçada;
- Alavancagem e risco de contraparte;
- Risco de custódia, smart contract, oracle e governança;
- Risco regulatório, fiscal e contratual;
- Risco de modelo, dados, backtest e automação;
- Risco de concentração em fatores, ecossistemas e fontes de renda;
- Risco operacional, reputacional e de manutenção;
- Risco de dispersão cognitiva e custo de oportunidade;
- Risco de ruína por dependências correlacionadas em cenários extremos.

Convexidade e antifragilidade só podem ser afirmadas quando a estrutura de payoff e os mecanismos justificarem a afirmação.

### 3.4 Impacto e economia regenerativa

Incorporar RWI/Impact-Weighted Accounts e práticas de mensuração de impacto como lentes. Separar:
- Intenção;
- Insumo;
- Atividade;
- Produto/entrega;
- Resultado;
- Impacto;
- Adicionalidade;
- Atribuição e contrafactual;
- Permanência e reversibilidade.

Não tratar ESG, carbono, regeneração ou impacto declarado como prova de impacto real.

---

## 4. Matriz de gaps → capacidades → entregáveis

| ID | Gap | Capacidade-alvo | Entregável proposto | Prioridade |
|---|---|---|---|---|
| G-01 | Dados demonstrativos misturados com configuração pessoal | Namespaces e proveniência | `config/README.md`, `project-files/perfil-demo.md`, política de dados | P0 |
| G-02 | Perfil qualitativo sem política de investimento executável | IPS/mandato versionado | `project-files/politica-de-investimento.md` | P0 |
| G-03 | Dados financeiros reais ausentes ou não estruturados | Importação segura e validação | `project-files/situacao-financeira.md`, `carteira-atual.md` como templates vazios | P0 |
| G-04 | Fontes especializadas misturadas | Registro de fontes por domínio | `project-files/fontes-por-dominio.md` | P0 |
| G-05 | Teses estáticas | Ciclo de vida epistêmico | `project-files/registro-de-teses.md` + schema | P1 |
| G-06 | Sem motor comum de triagem | Comparação multidimensional | `frameworks/matriz-alocacao-capital.md` | P1 |
| G-07 | Capital empreendedor pouco modelado | Pipeline venture/grants | `project-files/pipeline-de-oportunidades.md` | P1 |
| G-08 | Reflexividade e narrativas dispersas | Observatório de narrativas | `skills/observatorio-reflexividade/SKILL.md` | P1 |
| G-09 | Conhecimento tácito sem método | Captura e validação de heurísticas | `skills/captura-conhecimento-tacito/SKILL.md` | P2 |
| G-10 | Risco transversal fragmentado | Registro de riscos e dependências | `frameworks/risk-register.md` | P1 |
| G-11 | Impacto sem cadeia causal completa | Teoria da mudança e MRV | `skills/avaliacao-impacto-regenerativo/SKILL.md` | P2 |
| G-12 | Sem ciclo de decisão auditável | Diário e post-mortem | `project-files/diario-de-decisoes.md` | P1 |
| G-13 | Ausência de avaliação de desempenho do processo | Calibração e attribution | `analytics/decision-quality.md` | P2 |
| G-14 | Skills centradas em ações e carteira | Skills por classe de oportunidade | Novas Skills por domínio | P2 |
| G-15 | Arquitetura de prompts sem roteamento semântico | Orquestrador por intenção e risco | `skills/capital-intelligence-router/SKILL.md` | P2 |
| G-16 | Testes verificam fluxo, não validade | Testes de domínio e invariantes | `tests/domain/`, `tests/fixtures/` | P1 |
| G-17 | Sem arquitetura de dados comum | Modelo canônico de oportunidade, tese, evidência e decisão | `schemas/` | P1 |
| G-18 | UI orientada a abas fixas | Workspaces por tarefa e domínio | Evolução incremental de `index.html` | P3 |

---

## 5. Arquitetura funcional proposta

### 5.1 Camadas

1. **Interface / Workspaces:** pesquisa, carteira, teses, venture studio, risco, impacto, diário e monitoramento.
2. **Orquestração:** identifica intenção, domínio, risco, dados necessários e Skill apropriada.
3. **Conhecimento:** perfil, política, teses, fontes, ontologias, histórico e documentos.
4. **Evidências:** ingestão, proveniência, validação, classificação, atualização e rastreabilidade.
5. **Modelos:** valuation, fatores, cenários, risco, cashflow, unit economics, impacto e mecanismos de token.
6. **Decisão:** comparação, custo de oportunidade, adequação, reversibilidade, alocação e aprovação humana.
7. **Execução:** monitoramento, experimentos, entregas, contratos, grants, pilotos e repositórios.
8. **Aprendizagem:** diário, resultados, post-mortem, calibração e revisão de hipóteses.

### 5.2 Modelo de dados canônico

Começar com entidades simples e relacionáveis, sem impor banco de dados ou infraestrutura prematuramente:

- `Opportunity`: oportunidade de alocação;
- `Thesis`: hipótese causal;
- `Evidence`: fonte, dado, documento ou observação;
- `ResourceAllocation`: recurso comprometido;
- `ValueMechanism`: como valor é criado;
- `CaptureMechanism`: como o valor chega a quem aloca;
- `Risk`: evento, exposição, severidade e mitigação;
- `Scenario`: conjunto coerente de premissas;
- `Decision`: decisão tomada e alternativas rejeitadas;
- `Experiment`: teste, custo, resultado e aprendizado;
- `FundingSource`: grant, bounty, receita, equity, crédito, doação etc.;
- `ImpactOutcome`: resultado e evidência de impacto;
- `Actor`: pessoa, organização, protocolo, DAO, cliente ou contraparte;
- `Asset`: ativo, direito, software, IP ou instrumento;
- `Relationship`: dependência, propriedade, colaboração, exposição ou causalidade.

Campos transversais obrigatórios:
- ID estável;
- Estado;
- Criado em / atualizado em;
- Autor ou origem;
- Fonte e referência;
- Grau de confiança justificado;
- Limitações;
- Relações com outros objetos;
- Histórico de mudanças.

### 5.3 Estados epistêmicos e operacionais

Manter distinção entre:
- `CONFIRMADO_PELO_USUARIO`;
- `OBSERVADO_EM_DOCUMENTO`;
- `DADO_PRIMARIO_VERIFICADO`;
- `INFERIDO_COM_RESSALVA`;
- `HIPOTESE_DE_PESQUISA`;
- `EVIDENCIA_PRELIMINAR`;
- `TESE_EM_VALIDACAO`;
- `TESE_CORROBORADA`;
- `TESE_REFUTADA`;
- `EM_OBSERVACAO`;
- `NAO_AVALIADO`;
- `DADO_SINTETICO`;
- `DADO_DESATUALIZADO`.

Não confundir estado epistêmico com estágio comercial (ideia, protótipo, piloto, cliente, receita, escala).

---

## 6. Workstreams e plano de execução

### Fase 0 — Integridade, privacidade e configuração (P0)

**Objetivo:** impedir que a expansão propague premissas demonstrativas ou dados incorretos.

Entregas:
1. Auditar referências a `perfil.md`, Rafael, CLIENTE-RAF-01, R$ 300.000, tickers e limites exemplificativos.
2. Renomear ou classificar os dados demonstrativos como fixtures, sem apagar a capacidade de demonstração.
3. Criar templates vazios para situação financeira, carteira e restrições reais.
4. Separar `perfil-investidor-joao.md` (preferências qualitativas) de política de investimento e suitability.
5. Criar política de privacidade: não colocar dados patrimoniais, identificadores, extratos ou credenciais em repositório público.
6. Marcar valores de mercado e taxas com data, fonte, moeda e natureza (observado, exemplo, estimativa).

**Critério de aceite:** nenhum agente ou Skill pode assumir que o perfil demonstrativo é o perfil real; dados pessoais ausentes devem permanecer ausentes.

### Fase 1 — Núcleo de decisão e proveniência (P1)

**Objetivo:** criar a espinha dorsal comum para todas as classes de oportunidade.

Entregas:
1. Modelo canônico de Opportunity, Thesis, Evidence, Decision, Risk e Experiment.
2. Registro de teses com histórico, evidências, dependências, falsificadores e próxima ação.
3. Diário de decisões com hipótese inicial, alternativas, custo de oportunidade, aprovação e resultado.
4. Matriz de alocação multidimensional, sem score agregado automático.
5. Registro transversal de risco.
6. Hierarquia de fontes por domínio: finanças, macro, tecnologia, Web3, impacto, grants e negócios.
7. Testes de domínio para estados, unidades, proveniência, datas e consistência.

**Critério de aceite:** uma oportunidade pode ser rastreada desde sua origem até evidência, decisão, compromisso de recursos e resultado posterior.

### Fase 2 — Capital empreendedor, grants e IP (P1/P2)

**Objetivo:** incorporar a estratégia de construção de valor e financiamento não tradicional.

Entregas:
1. Pipeline de grants, bounties, hackathons, programas, crowdfunding, mecenato, pilotos e clientes.
2. Registro de requisitos, elegibilidade, deadline, esforço, entregável, direitos, obrigações e probabilidade qualitativa de sucesso.
3. Separação entre capital de desenvolvimento, capital de cliente, receita recorrente, prêmio, crédito, equity e doação.
4. Modelo de microtarefas com escopo, estimativa, dependências, evidência de conclusão, preço, direitos e possibilidade de transferência quando juridicamente válida.
5. Pipeline de OSS → dogfooding → serviço/curadoria → piloto pago → micro-SaaS/API → licenciamento.
6. Módulo de IP: autoria, proveniência, licença, ownership, access, attribution e economic rights.
7. Caso de uso ValueCurator/Compilatorum como laboratório experimental, sem presumir tração ou demanda.

**Critério de aceite:** o sistema consegue comparar uma grant e um piloto pago sem chamar ambos de receita, e explicita direitos e custos associados.

### Fase 3 — Inteligência de mercado ampliada (P2)

**Objetivo:** ampliar a cobertura além de ações brasileiras.

Domínios a implementar de forma modular:
- Macro, regimes, inflação, juros, moedas e liquidez global;
- Ações, qualidade, value, fatores e valuation;
- Renda fixa, crédito, duration, spreads e risco de recuperação;
- ETFs, fundos, diversificação internacional e look-through;
- Commodities, energia, infraestrutura e ativos reais;
- IA, semicondutores, cloud, dados e infraestrutura computacional;
- Software, open source, APIs, micro-SaaS e IP;
- Venture capital, angel, private markets e participações ilíquidas;
- Criptoativos, Bitcoin, DeFi, stablecoins, staking, protocolos e DAOs;
- Tokenização, mecanismos de incentivo, bonding curves e desenho de tesouraria;
- ReFi, carbono, biodiversidade, água, solo e infraestrutura regenerativa;
- Grants, bens públicos digitais e financiamento coletivo.

**Critério de aceite:** cada domínio tem um método específico, fontes apropriadas, riscos próprios e critérios de invalidação; nenhum domínio é reduzido a uma mesma fórmula de valuation.

### Fase 4 — Reflexividade, conhecimento tácito e impacto (P2)

**Objetivo:** operacionalizar as dimensões hermenêuticas e socioambientais.

Entregas:
1. Observatório de narrativas e reflexividade: atores, crenças, linguagem, incentivos, fluxo e evidência.
2. Captura de conhecimento tácito: contexto, heurística, caso, exceção, domínio de validade e teste.
3. Ontologia/grafo de relações entre atores, projetos, ativos, narrativas, fontes e mecanismos de valor.
4. Avaliação de impacto com cadeia causal, adicionalidade, permanência, MRV e atribuição.
5. Separação entre reputação, influência, contribuição, propriedade e direito econômico.
6. Avaliação de externalidades e custos de coordenação.

**Critério de aceite:** o sistema consegue registrar uma observação qualitativa sem promovê-la automaticamente a fato ou sinal negociável.

### Fase 5 — Orquestração, interface e aprendizagem contínua (P3)

**Objetivo:** integrar os módulos em um sistema coerente e ergonômico.

Entregas:
1. Router que seleciona Skill e modelo conforme tarefa, risco e evidência exigida.
2. Workspaces que mostrem apenas o contexto necessário para a tarefa.
3. Painel de portfólio ampliado com visões separadas: financeiro, projetos, capital intelectual, financiamento, risco e impacto.
4. Alertas por mudança de mecanismo, evidência ou condição de invalidação — não apenas por preço.
5. Métricas de qualidade decisória: calibração, erros, tempo até evidência, custo por aprendizado e revisão de premissas.
6. Exportação de relatórios e dados em formatos portáveis.
7. Auditoria de permissões e confirmação humana para ações externas.

**Critério de aceite:** o usuário consegue ir de uma pergunta a uma decisão documentada, com proveniência, limitações e próximos passos, sem depender de uma sequência manual de prompts desconectados.

---

## 7. Novas Skills sugeridas

Criar apenas quando o modelo canônico e os critérios de domínio estiverem definidos.

| Skill | Responsabilidade | Não deve fazer |
|---|---|---|
| `capital-intelligence-router` | Classificar intenção, risco, domínio e fluxo | Emitir recomendação sem evidência |
| `macro-regime-analysis` | Regimes, juros, inflação, liquidez, moedas e cenários | Prever ponto exato de virada |
| `quantamental-research` | Integrar fundamentos, fatores, dados e julgamento | Confundir score com verdade |
| `private-credit-analysis` | Estrutura, covenants, liquidez, recuperação e downside | Tratar yield como retorno garantido |
| `venture-microbusiness-underwriting` | Problema, cliente, unit economics, canais e risco de execução | Presumir TAM como demanda |
| `grants-and-funding-intelligence` | Descobrir e comparar capital não dilutivo e programas | Tratar aprovação como certa |
| `ip-and-open-source-economics` | Licenças, direitos, captura, distribuição e monetização | Confundir uso com disposição a pagar |
| `web3-mechanism-analysis` | Tokenomics, governança, treasury, incentivos e segurança | Tratar token como equity ou caixa |
| `reflexivity-observatory` | Narrativas, crenças, posicionamento e feedback | Usar sentimento isolado como sinal |
| `tacit-knowledge-capture` | Extrair e testar heurísticas contextuais | Converter intuição em regra sem teste |
| `regenerative-impact-underwriting` | Teoria da mudança, adicionalidade e MRV | Confundir intenção com impacto |
| `portfolio-of-capital-review` | Revisar dependências entre capitais e projetos | Somar dimensões incomensuráveis |
| `decision-journal-auditor` | Comparar decisão, premissa, resultado e calibração | Reescrever retrospectivamente a tese |

Cada Skill deve declarar: finalidade, escopo, pré-condições, entradas, fontes, procedimento, saídas, estados epistêmicos, limitações, riscos, validação e critérios de escalonamento humano.

---

## 8. Matriz de avaliação de oportunidades

Não criar um ranking universal que some tudo em uma nota. Usar uma ficha multicritério com dimensões separadas:

1. **Mecanismo:** como o valor é criado?
2. **Captura:** quem paga, quem recebe e quais direitos existem?
3. **Evidência:** qual é a fonte mais forte e o que ainda é inferência?
4. **Retorno:** qual fluxo ou benefício pode ser produzido?
5. **Risco:** como se perde, inclusive de forma permanente?
6. **Liquidez:** como sair, resgatar ou reaproveitar?
7. **Reversibilidade:** é possível testar em escala pequena?
8. **Horizonte:** quando custos e benefícios aparecem?
9. **Dependências:** quais atores, plataformas, protocolos e fatores são críticos?
10. **Custo total:** financeiro, fiscal, jurídico, técnico, operacional e cognitivo.
11. **Impacto:** quem se beneficia e quais externalidades existem?
12. **Aprendizagem:** o teste reduz incerteza ou produz capacidade reutilizável?
13. **Adequação:** é compatível com restrições efetivamente confirmadas?
14. **Alternativa:** o que acontece se não agir?

A saída deve ser um vetor de decisão, não uma falsa precisão:

[
\mathcal{D}(o)=
(\text{mecanismo},\text{evidência},\text{captura},\text{risco},
\text{liquidez},\text{custo},\text{impacto},\text{aprendizagem},\text{adequação})
]

Critérios desconhecidos devem permanecer desconhecidos. Uma oportunidade com alto valor potencial, mas sem mecanismo de captura, pode ser pesquisa ou bem público — não necessariamente investimento financeiro.

---

## 9. Protocolos de decisão e aprendizagem

### 9.1 Ciclo de oportunidade

1. Capturar a oportunidade e sua origem.
2. Classificar domínio, tipo de capital e fonte de financiamento.
3. Escrever a hipótese causal em uma frase.
4. Identificar beneficiário, pagador e mecanismo de captura.
5. Reunir evidências primárias e fontes independentes.
6. Construir steelman e red team.
7. Modelar cenários, custos e riscos.
8. Comparar com a alternativa de não agir.
9. Definir experimento mínimo e reversível.
10. Registrar decisão, responsável, orçamento e gatilhos.
11. Observar resultados e efeitos não previstos.
12. Atualizar a tese, inclusive para refutá-la.

### 9.2 Diário de decisões

Campos mínimos:
- ID e data;
- Oportunidade e tese;
- Estado epistêmico;
- Evidências disponíveis no momento;
- Premissas e incertezas;
- Alternativas consideradas;
- Recursos comprometidos;
- Perda máxima ou custo máximo aceitável, quando aplicável;
- Critérios de sucesso;
- Condições de invalidação;
- Decisão e justificativa;
- Resultado posterior;
- Diferença entre previsão e resultado;
- Aprendizado e revisão.

### 9.3 Métricas de processo

- Tempo entre hipótese e primeira evidência relevante;
- Custo por experimento informativo;
- Percentual de teses com falsificador explícito;
- Percentual de decisões com fontes rastreáveis;
- Taxa de revisão/refutação de teses;
- Calibração de probabilidades quando forem utilizadas;
- Retorno líquido ajustado a custos, quando mensurável;
- Conversão de protótipos em pilotos e pilotos em clientes;
- Receita recorrente versus capital pontual;
- Reutilização de IP, código e conhecimento;
- Custo de manutenção por ativo/projeto;
- Resultados de impacto e qualidade da atribuição.

Não otimizar métricas isoladas. Métricas são instrumentos de diagnóstico e podem gerar comportamento perverso.

---

## 10. Dados, privacidade e governança

### 10.1 Separação obrigatória de ambientes

- `demo/`: dados sintéticos e exemplos explicitamente rotulados;
- `project-files/public/`: princípios, métodos e artefatos não sensíveis;
- `project-files/private/`: templates e dados pessoais, fora do repositório público;
- `research/`: fontes, hipóteses e evidências públicas;
- `experiments/`: pilotos, projetos e resultados;
- `schemas/`: estruturas de dados sem informação pessoal.

A separação acima é uma proposta lógica; a implementação física deve respeitar a visibilidade pública do GitHub. Dados financeiros pessoais, extratos, documentos de identidade, credenciais e segredos não devem ser enviados a um repositório público.

### 10.2 Regras de proveniência

Cada dado deve informar:
- Origem e URL/documento;
- Data de publicação e data de consulta;
- Período econômico a que se refere;
- Unidade, moeda e convenção;
- Método de extração ou transformação;
- Estado de validação;
- Limitações e possíveis conflitos;
- Se é real, estimado, sintético ou ilustrativo.

### 10.3 Guardrails

- Nenhuma recomendação individual sem dados atuais e restrições confirmadas.
- Nenhuma posição, patrimônio, renda, horizonte ou tolerância numérica inferidos.
- Nenhum uso dos dados de Rafael como dados do usuário.
- Nenhum token tratado automaticamente como moeda, ação, equity ou direito de receita.
- Nenhuma grant tratada como receita recorrente ou aprovação provável sem base.
- Nenhum TVL, volume incentivado, seguidores ou commits tratados isoladamente como demanda.
- Nenhum backtest sem custos, vieses, universo, período e metodologia documentados.
- Nenhuma correlação histórica apresentada como hedge garantido.
- Nenhuma estimativa gerada por IA apresentada como dado primário.
- Ações externas, transações, publicação, assinatura ou movimentação de ativos exigem autorização humana explícita.

---

## 11. Estratégia de implementação: evitar o monólito e a dispersão

**Princípio:** máximo denominador comum nos dados e protocolos; especialização nos métodos de cada domínio.

Não reescrever o WebApp inteiro nem criar 15 Skills antes de validar o núcleo.

Ordem recomendada:
1. Resolver P0 (integridade e separação dos dados);
2. Implementar schemas mínimos e diário de decisões;
3. Transformar o catálogo de teses em registro rastreável;
4. Implementar matriz de alocação e pipeline de oportunidades;
5. Adicionar primeiro o domínio empreendedor/grants/IP, que conecta o sistema às experiências e projetos já existentes;
6. Expandir para reflexividade, Web3 e impacto;
7. Só então ampliar interface e automações.

### 11.1 O que não fazer agora

- Não migrar para banco de dados, microserviços ou infraestrutura distribuída antes de estabilizar os schemas.
- Não criar token negociável para representar reputação, pesquisa ou contribuição sem utilidade, direitos, governança e demanda demonstrados.
- Não construir um dashboard de dezenas de métricas antes de existir decisão recorrente que ele melhore.
- Não duplicar Skills com prompts semelhantes.
- Não automatizar alocação, compra, venda, assinatura ou transferência de ativos.
- Não confundir cobertura funcional do WebApp com validação de investimento.
- Não expandir o catálogo de teses apenas para aumentar quantidade; priorizar evidência e falsificação.

---

## 12. Plano de testes e definição de pronto

### 12.1 Testes funcionais

- Importação, validação e sanitização;
- Separação de ambientes demo/privado/público;
- Criação e atualização de teses;
- Vínculo de evidências e fontes;
- Registro de decisões e experimentos;
- Comparação entre classes de oportunidades;
- Exportação e portabilidade;
- Permissões e confirmação humana.

### 12.2 Testes semânticos e financeiros

- Unidades e moedas incompatíveis;
- Fluxos pontuais versus recorrentes;
- Valor bruto versus líquido;
- Equity versus dívida versus grant versus receita;
- Token versus direito econômico;
- Retorno nominal versus real;
- Liquidez anunciada versus liquidez realizável;
- Causalidade versus correlação;
- Dado observado versus estimativa versus dado sintético;
- Cenário versus previsão;
- Impacto declarado versus resultado adicional.

### 12.3 Testes adversariais

- Perfil demonstrativo contaminando perfil real;
- Fonte promocional tratada como evidência independente;
- Narrativa confundida com fundamento;
- Modelo alucinado sem proveniência;
- Falsa diversificação por ativos correlacionados;
- Oportunidade sem mecanismo de captura;
- Grant confundida com cliente;
- Reputação confundida com receita;
- Crescimento tecnológico confundido com retorno de ativo;
- Projeto complexo sem usuário ou pagador;
- Métrica de impacto otimizada em detrimento do resultado real.

### 12.4 Critérios globais de pronto

O upgrade estará suficientemente maduro quando:
1. Dados reais, sintéticos e demonstrativos estiverem inequivocamente separados;
2. O modelo canônico cobrir ativos financeiros e oportunidades não financeiras;
3. Teses tiverem estados, evidências, falsificadores e histórico;
4. Decisões puderem ser auditadas retrospectivamente;
5. Grants, receita, equity, crédito, tokens e doações tiverem semântica distinta;
6. Riscos financeiros, técnicos, jurídicos e operacionais forem rastreáveis;
7. Skills declararem limites e fontes;
8. Testes cobrirem semântica e integridade, não apenas interface;
9. O sistema souber dizer “não sei”, “não há evidência” e “não agir”;
10. Nenhuma automação crítica puder comprometer recursos sem autorização humana.

---

## 13. Relação com os artefatos existentes

| Artefato atual | Evolução proposta |
|---|---|
| `project-files/perfil-investidor-joao.md` | Preservar como perfil qualitativo; referenciar política e restrições separadamente |
| `project-files/teses-de-investimento.md` | Manter como catálogo inicial; criar registro vivo e IDs estáveis |
| `project-files/perfil.md` | Reclassificar como perfil demonstrativo/sintético ou fixture |
| `project-files/fontes.md` | Preservar para o caso demonstrativo; criar fontes gerais e por domínio |
| `index.html` | Evoluir incrementalmente para workspaces multidomínio |
| `scripts/` | Acrescentar funções reutilizáveis com testes e contratos explícitos |
| `skills/` | Preservar Skills atuais e adicionar novas por domínio após schemas |
| `TESTES_E2E...` | Complementar com testes de domínio, segurança, semântica e qualidade analítica |
| `UPGRADE_V2...` | Manter como especificação da arquitetura original de IA financeira |

### Novos arquivos recomendados — ordem sugerida

**Primeiro lote (núcleo):**
- `project-files/politica-de-investimento.md`
- `project-files/situacao-financeira.template.md`
- `project-files/carteira-atual.template.md`
- `project-files/diario-de-decisoes.md`
- `project-files/pipeline-de-oportunidades.md`
- `frameworks/matriz-alocacao-capital.md`
- `schemas/opportunity.schema.json`
- `schemas/thesis.schema.json`
- `schemas/evidence.schema.json`

**Segundo lote (inteligência ampliada):**
- `project-files/fontes-por-dominio.md`
- `frameworks/risk-register.md`
- `frameworks/alquimia-do-capital.md`
- `skills/grants-and-funding-intelligence/SKILL.md`
- `skills/venture-microbusiness-underwriting/SKILL.md`
- `skills/ip-and-open-source-economics/SKILL.md`
- `skills/reflexivity-observatory/SKILL.md`
- `skills/regenerative-impact-underwriting/SKILL.md`

Os arquivos são propostas; não devem ser criados em lote sem revisão dos schemas, dependências e critérios de aceite.

---

## 14. Síntese estratégica

O repositório não precisa abandonar sua competência atual em análise financeira. Precisa deixar de presumir que toda oportunidade de investimento se apresenta como um ticker, uma carteira ou um preço-alvo.

A arquitetura desejada integra três escalas:

1. **Mercado:** ativos, empresas, fatores, crédito, macroeconomia e protocolos;
2. **Empreendimento:** software, IP, serviços, grants, microtarefas, pilotos e mecanismos de captura;
3. **Pessoa/ecossistema:** tempo, conhecimento, atenção, relações, autonomia, impacto e resiliência.

A unidade de análise passa a ser a **oportunidade de alocação de recursos**, com método específico para cada domínio e um protocolo comum de evidência, risco, custo de oportunidade, decisão e aprendizagem.

[
\boxed{
\text{Inteligência de Capital}
=
\text{Ontologia}
+
\text{Evidência}
+
\text{Mecanismo}
+
\text{Risco}
+
\text{Decisão}
+
\text{Aprendizagem}
}
]

**Filosofemas finais**

- *Mapa não é território: o modelo deve representar a incerteza, não escondê-la.*
- *Capital sem mecanismo de captura pode ser contribuição, bem público ou opção — mas não deve ser chamado automaticamente de investimento rentável.*
- *A melhor automação não é a que decide tudo; é a que torna as decisões verificáveis, reversíveis e corrigíveis.*
- *A regeneratividade do sistema depende de feedback real, não de uma narrativa de autorreprodução.*

**Recomendação de execução:** começar pela Fase 0 e pelo núcleo da Fase 1. Depois, priorizar o pipeline de grants, micro-ventures, IP e serviços, conectando o sistema financeiro tradicional à estratégia real de construção de valor. Só expandir a interface e as automações quando os objetos, estados e protocolos estiverem estáveis.

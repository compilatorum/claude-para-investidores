# 🧪 Spec — Laboratório de Ciência Computacional, Quant Research & Governança de Smart Money

> **Versão:** 1.0 · **Data:** 2026-10-31  
> **Repositório:** `compilatorum/claude-para-investidores`  
> **Tipo:** especificação científica, metodológica, arquitetural e experimental para evolução do sistema.  
> **Linha provisória de pesquisa:** **Engenharia Simbólica de Portfólios Regenerativos em Ecossistemas Inteligentes Descentralizados**.  
> **Natureza:** blueprint de pesquisa e engenharia; não constitui estratégia validada, recomendação de investimento, parecer jurídico, nem autorização para execução financeira autônoma.

---

## 0. Tese fundadora

Transformar o projeto em um **laboratório de programação científica para finanças computacionais**, no qual cada tese, operação financeira, alocação de recursos, mecanismo de governança ou experimento de produto seja representado como uma hipótese explícita, com evidências, protocolo, critérios de validação, riscos, resultados e possibilidade de replicação.

A unidade fundamental deixa de ser apenas o ativo ou o relatório. Passa a ser o **experimento rastreável**:

\[
\boxed{
\text{Pergunta}
\rightarrow \text{Hipótese}
\rightarrow \text{Protocolo}
\rightarrow \text{Dados}
\rightarrow \text{Experimento}
\rightarrow \text{Validação}
\rightarrow \text{Replicação}
\rightarrow \text{Decisão}
\rightarrow \text{Aprendizagem}
}
\]

O laboratório conecta:

- **Quant Research:** formulação e teste de hipóteses quantitativas;
- **Quant Analysis:** interpretação financeira, econômica e estatística;
- **Quant Development:** engenharia de dados, modelos, backtests, simulações, APIs e testes;
- **Computational Finance:** métodos numéricos, otimização, séries temporais, risco e microestrutura;
- **Design Science Research (DSR):** construção e avaliação de artefatos que resolvem problemas relevantes;
- **Autoetnografia simbiótica:** documentação reflexiva da interação humano–IA–ferramentas, sem confundir relato subjetivo com evidência causal;
- **Metaciência:** avaliação da qualidade, reprodutibilidade e incentivos da própria pesquisa;
- **Governança experimental:** análise de como regras, direitos, incentivos e informação distribuem poder, risco e valor em organizações e DAOs.

**Filosofema:** *Cada operação é uma pergunta feita ao mundo com recursos reais em jogo. A ciência começa quando registramos, antes do resultado, o que esperamos observar e o que nos faria mudar de ideia.*

### 0.1 O que este sistema não deve ser

- Um gerador de sinais de compra e venda com verniz científico;
- Um backtest factory que seleciona a melhor curva retrospectivamente;
- Um oráculo de mercado baseado em fluência textual de LLMs;
- Um laboratório que transforma correlação em causalidade;
- Um agente com permissão irrestrita para movimentar dinheiro, assinar transações ou alterar parâmetros críticos;
- Uma DAO fictícia apresentada como governança real;
- Uma gamificação que converte toda experiência humana em pontos, produtividade ou preço;
- Uma colagem de frameworks sem contratos, critérios de interoperabilidade ou justificativa de custo.

### 0.2 Relação com os documentos canônicos

Esta especificação complementa, não substitui:

- `project-files/teses-de-investimento.md`: universo de hipóteses e estados epistêmicos;
- `project-files/plano-upgrade-inteligencia-de-capital.md`: ontologia ampliada de capital e decisão;
- `project-files/plano-upgrade-ii-engenharia-de-sistemas-ia-quant-developer.md`: contratos, contexto, agentes, harness e execução;
- `project-files/meta-prompt-template-chain-inteligencia-de-capital.md`: cadeia de prompts e contratos;
- `project-files/spec-promptcraft-os-engenharia-governanca-orquestracao.md`: engenharia e governança de prompts;
- `project-files/machinations-simulation-blueprint.md`: simulação de fluxos, recursos e mecanismos;
- `project-files/radar-nichos-compativeis.md`: hipóteses de nichos, descoberta e validação de demanda.

**Regra de integração:** a tese define *o que investigar*; esta spec define *como investigar, experimentar, programar, validar e aprender*; o Promptcraft OS define *como orquestrar linguagem e tarefas*; o harness define *como impedir que uma resposta plausível passe por resultado verificado*.

---

## 1. Mandato científico e linhas de inquiry

### 1.1 Linha principal

**Engenharia Simbólica de Portfólios Regenerativos em Ecossistemas Inteligentes Descentralizados**

Pergunta abrangente:

> Como projetar, testar e governar sistemas computacionais que alocam capital financeiro e não financeiro em condições de incerteza, combinando métodos quantitativos, conhecimento contextual, inteligência híbrida, mecanismos descentralizados e critérios de regeneratividade?

A pergunta é deliberadamente ampla e deve ser decomposta em linhas investigáveis, cada uma com escopo e critérios próprios.

### 1.2 Linhas de pesquisa candidatas

| ID | Linha de inquiry | Pergunta de pesquisa | Artefato / método |
|---|---|---|---|
| LQ-01 | Quantamental e evidência | A combinação de dados, fundamentos e contexto melhora decisões fora da amostra? | Pipeline quantamental, ablação, walk-forward |
| LQ-02 | Hipóteses de investimento | O registro prévio de hipótese e falsificadores reduz decisões inconsistentes? | Ledger de teses/operações, estudo longitudinal |
| LQ-03 | Governança de smart money | Quais regras de alocação, veto, delegação e prestação de contas produzem decisões robustas? | Simulação de mecanismos, DAO sandbox |
| LQ-04 | Economia experimental | Como incentivos, informação e direitos alteram contribuição, coordenação e captura de valor? | Jogos, surveys, experimentos controlados |
| LQ-05 | IA experimental | Em quais tarefas IA aumenta qualidade, velocidade ou cobertura sem elevar erros críticos? | Benchmark, avaliação cega, comparação de modelos |
| LQ-06 | Engenharia de pesquisa | Quais pipelines tornam pesquisas financeiras reproduzíveis e auditáveis? | Data lineage, CI, notebooks e relatórios |
| LQ-07 | Portfólios regenerativos | Como comparar retornos financeiros, resiliência, externalidades e capital não financeiro sem falsa fungibilidade? | Ontologia multidimensional, MCDA |
| LQ-08 | UX/DX/LX/IX/SXD | Como interfaces simbólicas alteram compreensão, confiança calibrada e qualidade da decisão? | Estudos UX, logs consentidos, testes de usabilidade |
| LQ-09 | Ciência aberta e DeSci | Como DAOs, repositórios e protocolos podem financiar, revisar e replicar pesquisa? | Mapeamento de ecossistema, piloto de governança |
| LQ-10 | Autoetnografia simbiótica | Como documentar a evolução do trabalho humano–IA sem confundir experiência com causalidade? | Diário reflexivo, análise temática, triangulação |

Uma linha só entra em execução quando possui: pergunta delimitada, justificativa, literatura inicial, unidade de análise, método, dados acessíveis, riscos éticos e critério de encerramento.

### 1.3 Engenharia da pergunta certa

Antes de pesquisar, perguntar:

1. Qual decisão ou fenômeno queremos compreender?
2. Para quem o resultado será útil?
3. Qual é a unidade de análise: ativo, operação, carteira, pessoa, protocolo, proposta, DAO, experimento ou interação?
4. O que já se sabe e o que permanece incerto?
5. Qual mecanismo causal ou descritivo está sendo proposto?
6. Quais explicações rivais são plausíveis?
7. Qual observação distinguiria as explicações?
8. Quais dados seriam necessários e como serão obtidos?
9. O que não será possível concluir?
10. Qual é o menor teste capaz de reduzir incerteza relevante?

Modelo **PICOT/PECO adaptável**:
- **P**opulação / contexto;
- **I**ntervenção / exposição;
- **C**omparador;
- **O**utcome / resultado;
- **T**empo / horizonte.

Para pesquisa qualitativa, usar variantes como contexto–fenômeno–participantes–processo–significado. Não forçar desenho clínico em toda pergunta financeira ou sociotécnica.

**Prompt de follow-up — lapidar pergunta:**
> Atue como orientador metodológico e Red Team. Converta esta ideia em até três perguntas de pesquisa concorrentes. Para cada uma, especifique unidade de análise, mecanismo, variáveis observáveis, explicações rivais, método viável, dados necessários, limitações e condição de refutação. Escolha a pergunta mais estreita que preserve a relevância do problema.

---

## 2. Framework científico: epistemologia operacional

### 2.1 Escada de transformação

| Nível | Definição operacional | Exemplo financeiro | Pergunta de qualidade |
|---|---|---|---|
| Dados | Observações brutas com origem e timestamp | Preços, volumes, balanços, propostas DAO | São íntegros, completos e comparáveis? |
| Informação | Dados contextualizados | Tendência setorial, mudança de margem, fluxo de tesouraria | O contexto é correto e temporalmente válido? |
| Conhecimento | Relações, modelos ou regras inferidas | Hipótese de que capex em smart grids reduz custo futuro | Há evidência, mecanismo e limites? |
| Inteligência | Capacidade de selecionar ação sob contexto e restrições | Comparar cenários e escolher teste ou não agir | A recomendação considera incerteza e custo? |
| Sabedoria | Julgamento prudencial sobre consequências e valores | Considerar comunidades, externalidades e risco sistêmico | Quem se beneficia, quem suporta o dano e quem decide? |
| Mistério | Reconhecimento explícito do que permanece desconhecido | Incerteza radical, emergência, reflexividade | O sistema preserva o não sabido sem inventar certeza? |

A sequência não é uma escada automática. Mais dados não garantem conhecimento; conhecimento técnico não garante sabedoria. “Mistério” designa limite epistemológico e abertura investigativa, não evidência sobrenatural nem licença para afirmações não testáveis.

### 2.2 Lógica, epistemologia, gnosiologia e logologia

O sistema deve explicitar quatro planos:

- **Lógico:** validade das inferências, consistência, contradições e regras;
- **Epistemológico:** critérios pelos quais uma afirmação conta como conhecimento científico;
- **Gnosiológico:** relação entre sujeito, experiência, objeto e conhecimento;
- **Logológico / linguístico:** como termos, categorias, prompts, narrativas e formatos estruturam o que pode ser percebido e pesquisado.

Toda conclusão deve declarar o tipo:
`OBSERVACAO | CALCULO | INFERENCIA | HIPOTESE | INTERPRETACAO | OPINIAO | DECISAO`.

### 2.3 Ciclo científico completo

[
H_0 \rightarrow P \rightarrow D \rightarrow E \rightarrow V \rightarrow R \rightarrow U
]

- **H₀:** hipótese registrada antes do teste;
- **P:** protocolo e plano de análise;
- **D:** dados versionados e documentados;
- **E:** execução do experimento;
- **V:** validação técnica, estatística e substantiva;
- **R:** replicação independente ou em novo período/contexto;
- **U:** atualização da tese e decisão.

O ciclo inclui resultados nulos, falhas, desvios de protocolo e resultados contraditórios. Não apagar experimentos que “não funcionaram”.

### 2.4 Estados epistêmicos integrados ao catálogo

Reutilizar a taxonomia existente:
`INTERESSE_DECLARADO`, `HIPOTESE_DE_PESQUISA`, `EVIDENCIA_PRELIMINAR`, `TESE_EM_VALIDACAO`, `TESE_CORROBORADA`, `TESE_REFUTADA`, `EM_OBSERVACAO`, `NAO_AVALIADA`.

Adicionar estados do experimento:
`RASCUNHO`, `PREREGISTRADO`, `EM_COLETA`, `EM_EXECUCAO`, `CONCLUIDO`, `FALHOU_TECNICAMENTE`, `INCONCLUSIVO`, `REPLICACAO_PENDENTE`, `REPLICADO`, `ARQUIVADO`.

**Importante:** uma tese corroborada não implica uma operação lucrativa; um experimento bem executado pode produzir resultado nulo; um backtest positivo não demonstra causalidade nem persistência futura.

---

## 3. Cada operação financeira como hipótese

### 3.1 Unidade canônica: Operation-as-Hypothesis

Toda operação real ou simulada deve ser precedida por um registro de hipótese. A operação não é somente uma ordem; é um compromisso de recursos associado a uma crença verificável.

**Contrato mínimo da operação:**

| Campo | Descrição |
|---|---|
| `operation_id` | ID único e imutável |
| `thesis_id` | Tese do catálogo relacionada |
| `hypothesis_id` | Hipótese específica que justifica a operação |
| `instrument` | Ativo, contrato, participação, grant, crédito, token ou recurso |
| `decision_timestamp` | Momento da decisão |
| `information_cutoff` | Último instante de informação permitido |
| `side_and_intent` | Comprar, vender, manter, financiar, contribuir, votar, não agir |
| `expected_mechanism` | Como se espera criar/capturar valor |
| `expected_outcomes` | Resultados e faixas esperadas, sem precisão artificial |
| `alternative_hypotheses` | Explicações rivais |
| `counterfactual` | O que ocorreria sem a operação ou com alternativa |
| `risk_budget` | Limites aprovados por política externa ao modelo |
| `costs` | Taxas, spread, slippage, impostos, gas, tempo e manutenção |
| `exit_or_review_rule` | Critério de revisão, encerramento ou invalidação |
| `evidence_snapshot` | Fontes, dados, versões e hashes |
| `approval_record` | Aprovação humana e identidade/escopo do aprovador |
| `realized_outcome` | Resultado observado, registrado depois |
| `learning_record` | O que foi aprendido e o que muda na tese |

A hipótese deve ser congelada ou versionada no momento da decisão. Alterações posteriores geram nova versão, nunca sobrescrevem a previsão original.

### 3.2 Tipos de operação

- **Alocação financeira:** compra, venda, rebalanceamento, hedge, empréstimo;
- **Alocação empreendedora:** tempo, capital, código, IP, contratação, piloto;
- **Alocação de pesquisa:** orçamento, compute, dados, grants, bolsas;
- **Alocação de governança:** voto, delegação, proposta, veto, treasury grant;
- **Alocação de atenção:** priorização de tese, projeto ou experimento.

Cada domínio possui unidade, risco e métrica próprios. Só comparar quando houver uma função de utilidade explícita e justificável.

### 3.3 Hipótese de não agir

A ausência de operação também é uma decisão registrável:
- hipótese de que o risco/custo de agir supera o benefício esperado;
- alternativa de caixa, espera ou coleta adicional de informação;
- custo de oportunidade estimado;
- evento que justificaria reabrir a decisão.

### 3.4 Atualização bayesiana sem falsa precisão

Quando houver probabilidades defensáveis:
[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
]

Registrar prior, evidência, likelihood, posterior, fonte e sensibilidade. Se as probabilidades forem subjetivas ou frágeis, marcar como elicitação qualitativa ou faixa de plausibilidade. Não fabricar percentuais para dar aparência quantitativa.

### 3.5 Decision journal e forecast ledger

Separar:
- previsão prévia;
- decisão tomada;
- justificativa;
- resultado observado;
- avaliação de calibração;
- revisão retrospectiva.

Evitar hindsight bias. A pergunta não é apenas “ganhou ou perdeu?”, mas “a decisão foi razoável dadas as informações disponíveis naquele instante?”.

---

## 4. Design Science Research + Autoetnografia Simbiótica

### 4.1 Design Science Research (DSR)

Aplicar o ciclo DSR:
1. **Problema e motivação:** demonstrar relevância e contexto;
2. **Objetivos da solução:** definir requisitos mensuráveis;
3. **Design e desenvolvimento:** construir artefato, método ou modelo;
4. **Demonstração:** executar em cenário realista;
5. **Avaliação:** comparar com critérios, baseline e alternativas;
6. **Comunicação:** publicar método, limitações, dados permitidos e resultados.

O artefato pode ser software, ontologia, protocolo, modelo de governança, interface, simulador ou workflow.

### 4.2 Autoetnografia simbiótica

Documentar como o pesquisador trabalha com IA, código, dados, comunidades e ferramentas:
- diário de campo reflexivo;
- decisões de prompting e alterações de contexto;
- momentos de confiança, dúvida, fricção e surpresa;
- episódios de automação bem-sucedida e falha;
- mudanças de vocabulário, categorias e práticas;
- distinção entre relato pessoal e observação externa.

**Triangulação obrigatória:** diário reflexivo + logs técnicos + artefatos/versionamento + avaliação externa ou independente, quando possível.

Não inferir estados mentais ocultos a partir de logs. Logs de interação simbólica com IA são dados de processo, não leitura direta de cognição ou personalidade. Coletar consentimento, minimizar dados pessoais e permitir exclusão conforme a política do projeto.

### 4.3 Experimento vivo

O laboratório pode ser um **experimento vivo de design de subjetividades, conhecimento e tecnologia**, desde que o termo seja operacionalizado:
- qual experiência está sendo desenhada?
- quais capacidades se pretende apoiar?
- que comportamento observável pode mudar?
- como diferenciar mudança percebida de mudança medida?
- quais efeitos adversos ou dependências podem emergir?

A meta é criar interfaces e experiências transformativas sem manipulação, paternalismo, medicalização ou gamificação compulsiva.

### 4.4 UX / DX / LX / IX / SXD

| Dimensão | Foco | Métricas possíveis |
|---|---|---|
| UX | Uso e compreensão | sucesso de tarefa, erros, SUS, tempo, acessibilidade |
| DX | Experiência de desenvolvimento | setup, lead time, falhas, clareza de APIs, onboarding |
| LX | Aprendizagem | retenção, transferência, resolução de problemas, autoeficácia calibrada |
| IX | Experiência de informação/interação | encontrabilidade, legibilidade, confiança calibrada, navegação |
| SXD | Symbolic eXperience Design | coerência simbólica, orientação, significado percebido, compreensão e autonomia |

SXD é um conceito de design proposto para o projeto, não uma disciplina padronizada. Deve ser avaliado por indicadores observáveis e pesquisa qualitativa, não por alegações de transformação interior.

---

## 5. Métodos de pesquisa: escolher pelo tipo de pergunta

### 5.1 Matriz de métodos

| Método | Quando usar | Limite / cuidado |
|---|---|---|
| Revisão sistemática | Pergunta delimitada e busca exaustiva/reprodutível | Exige protocolo, critérios e gestão de viés |
| Mapeamento sistemático | Campo amplo, taxonomia e distribuição de estudos | Não equivale a síntese causal |
| Meta-análise | Estudos suficientemente comparáveis com estatísticas compatíveis | Heterogeneidade, viés de publicação e dependência entre estudos |
| Scoping review | Delimitar conceitos, evidências e lacunas | Não estima necessariamente efeito agregado |
| Estudo de caso | Fenômeno contextual complexo | Generalização analítica, não estatística |
| Survey | Atitudes, práticas e características de população definida | Amostragem, não resposta, validade de construto |
| Entrevista / inquiry | Significados, mecanismos e conhecimento tácito | Reflexividade e interpretação |
| Experimento controlado | Efeito causal sob condições controladas | Validade externa e ética |
| A/B test | Comparar variantes de produto/interface | Interferência, múltiplas métricas e parada prematura |
| Coorte | Acompanhar exposição e desfechos ao longo do tempo | Confusão e attrition |
| Quase-experimento | Efeito quando randomização não é viável | Pressupostos identificadores explícitos |
| Backtest | Comportamento histórico de uma regra | Viés temporal, custos, overfitting |
| Walk-forward | Avaliação sequencial fora da amostra | Não elimina regime shift |
| Simulação / agent-based | Mecanismos, interações e cenários | Resultado depende das regras e calibração |
| Pesquisa operacional | Otimização sob restrições | Otimizador pode ser preciso para modelo errado |
| Autoexperimentação | Aprendizagem exploratória individual | N=1, confusão e baixa generalização |
| Citizen science | Participação distribuída na coleta/análise | Curadoria, consentimento e qualidade |
| Red Team | Encontrar falhas, explicações rivais e vulnerabilidades | Não substitui avaliação positiva ou replicação |

### 5.2 Revisão sistemática e meta-análise automatizada contínua

Pipeline:
1. Pergunta e protocolo (PICO/PECO ou equivalente);
2. Bases e fontes autorizadas;
3. Estratégias de busca versionadas;
4. Deduplicação e registro de cobertura;
5. Triagem por critérios explícitos;
6. Extração estruturada de métodos, amostras, efeitos e limitações;
7. Avaliação de qualidade/risco de viés;
8. Síntese narrativa e, quando justificável, quantitativa;
9. Heterogeneidade e sensibilidade;
10. Atualização incremental e alerta de novos estudos.

A IA pode classificar, resumir, sugerir códigos e detectar lacunas, mas a decisão de inclusão, extração crítica e avaliação de viés deve ser auditável e amostralmente verificada por humanos. Meta-análise só quando medidas, desenhos e populações forem suficientemente compatíveis. Não somar resultados heterogêneos só porque existem números.

### 5.3 Metaciência e qualidade da pesquisa

Avaliar também:
- pré-registro e transparência;
- viés de publicação e seleção;
- poder estatístico e precisão;
- multiplicidade de testes;
- replicabilidade computacional;
- reprodutibilidade independente;
- robustez a escolhas analíticas;
- qualidade dos dados e da medição;
- incentivos e conflitos de interesse;
- diferença entre evidência exploratória e confirmatória.

---

## 6. Deep Research como workflow científico e experimento linguístico

### 6.1 Papel no laboratório

Usar Deep Research como **motor de investigação assistida**, não como árbitro da verdade. Seu trabalho é explorar fontes, comparar alegações, produzir mapa de evidências, localizar controvérsias e apontar lacunas. O resultado precisa ser convertido em artefatos verificáveis.

Capacidades úteis, conforme disponibilidade do produto e da conta:
- pesquisa multi-etapas com decomposição de pergunta;
- exploração de fontes web e documentos fornecidos;
- síntese com citações;
- comparação de perspectivas e evidências;
- identificação de lacunas e perguntas de seguimento;
- relatórios estruturados;
- uso de arquivos de referência e links como escopo, quando a interface aceitar;
- possibilidade de interromper, orientar ou refinar a investigação durante a execução, quando suportado.

Não presumir que todo link será acessível, que toda fonte será indexada, que o sistema lerá repositórios privados, nem que haverá API pública equivalente ao recurso de interface. Verificar a documentação e disponibilidade vigentes antes de desenhar integração. Se não houver API Deep Research acessível, usar API de modelos + busca/fetch autorizados + orquestrador próprio como alternativa, sem chamar isso de Deep Research API.

### 6.2 Deep Research por API: arquitetura alternativa

Separar:
- **Research Planner:** converte pergunta em plano e subperguntas;
- **Search Connectors:** web, Crossref/OpenAlex/Semantic Scholar, arXiv, SSRN quando permitido, GitHub, documentação oficial, repositórios DAO e fontes institucionais;
- **Fetch/Parser:** extrai texto, metadados, tabelas e código;
- **Evidence Store:** guarda URL, título, autor, data, trecho, hash, licença e timestamp de acesso;
- **Claim Extractor:** transforma fontes em alegações atômicas;
- **Evidence Graph:** liga alegação ↔ fonte ↔ método ↔ tese ↔ experimento;
- **Synthesis Agent:** sintetiza com citações e desacordos;
- **Verifier / Red Team:** verifica fonte, data, interpretação e evidência contrária;
- **Human Gate:** aprova escopo e conclusão;
- **Report Builder:** gera Org/Markdown/JSON e mapa de pesquisa.

Cada conector deve respeitar robots/termos/licenças, limites de taxa, privacidade, autenticação e políticas de uso. Não contornar paywalls nem controles de acesso.

### 6.3 Pesquisa do alto ao baixo nível

Uma investigação de framework ou projeto deve seguir esta escada:

1. **Landscape:** quais famílias de soluções existem?
2. **Taxonomia:** quais problemas cada uma resolve?
3. **Critérios:** o que significa “melhor” para o caso?
4. **Shortlist:** quais repositórios/documentações merecem inspeção?
5. **Código:** como implementam os recursos relevantes?
6. **Contrato:** quais inputs, outputs, estado, dependências e licenças?
7. **Integração:** qual adaptador ou boundary permite interoperar?
8. **PoC:** menor teste executável isolado;
9. **Simulação:** cenários de uso, falhas e custos;
10. **Review:** testes, code review e segurança;
11. **Replicação:** rodar em ambiente limpo e segundo runtime;
12. **Decisão:** adotar, adaptar, fork, integrar ou rejeitar.

**Prompt — Deep Research de framework:**
> Investigue [framework/problema] como pesquisador de software e quant developer. Comece pelo landscape e documentação primária; depois inspecione o repositório e o código das features relevantes. Produza matriz de capacidades, arquitetura, dependências, licença, maturidade, manutenção, extensibilidade, formatos de dados, APIs, testes, limitações e riscos. Não infira recursos pela descrição de marketing. Cite arquivos, símbolos, versões e linhas quando possível. Compare com [alternativas] usando critérios ponderados definidos antes da avaliação. Proponha uma PoC mínima, fixtures, testes de integração, benchmark e condições objetivas de adoção/rejeição.

### 6.4 Arquivos de links como escopo

Manter `research/registries/source-manifest.yaml` com:
- URL;
- título e organização;
- categoria (paper, dataset, repo, docs, DAO, API);
- pergunta a que serve;
- prioridade;
- status (pendente, acessado, inacessível, arquivado);
- data de acesso;
- licença/termos;
- versão/commit, quando aplicável;
- hash do conteúdo, quando permitido.

Um arquivo de links delimita o universo inicial, mas não prova que o conteúdo foi lido ou validado. Registrar falhas de acesso em vez de substituir silenciosamente por fontes secundárias.

### 6.5 Prompting crítico e follow-ups inteligentes

**Prompt de revisão adversarial:**
> Faça uma crítica científica desta síntese. Separe fatos, inferências, hipóteses e opiniões. Identifique fontes circulares, fontes primárias ausentes, afirmações sem suporte, vieses de seleção, conflito de interesse, datas incompatíveis, evidências contraditórias e generalizações indevidas. Construa o argumento mais forte contra a conclusão e diga que observação poderia refutá-la.

**Prompt de smart follow-up / simulated debug:**
> Simule uma revisão de execução do protocolo. Liste os pontos em que a investigação poderia falhar: busca incompleta, parser, dados ausentes, viés temporal, fonte quebrada, API indisponível, dependência incompatível, teste frágil ou conclusão não suportada. Para cada falha, proponha um teste reproduzível, resultado esperado, log necessário e ação corretiva. Não afirme que executou testes que apenas simulou.

**Prompt de síntese incremental:**
> Atualize a pesquisa apenas com novas evidências desde [data/versão]. Preserve conclusões anteriores que continuam sustentadas; marque o que mudou, por quê, quais hipóteses foram enfraquecidas e quais novos experimentos se tornaram prioritários. Não reescreva o histórico para aparentar coerência retrospectiva.

**Prompt de metaconversa:**
> Antes de responder, critique o próprio desenho da pergunta e do método. Que premissas foram introduzidas? O que está sendo medido como proxy? Que dimensão relevante foi omitida? Qual é a alternativa metodológica mais simples? O que não devemos tentar inferir?

### 6.6 Deep Research como experimento linguístico

Tratar linguagem como interface de investigação:
- comparar formulações de pergunta;
- registrar mudanças de escopo e vocabulário;
- avaliar cobertura, precisão e diversidade de fontes;
- medir taxa de afirmações sustentadas;
- comparar respostas com prompt curto, estruturado e contrato formal;
- registrar quando a fluência retórica aumenta sem ganho de evidência.

Do alto nível (metáfora, inquiry, problema) ao baixo nível (schema, query, função, teste), preservar rastreabilidade entre a intenção original e o código/resultado.

---

## 7. Arquitetura técnica: Scientific Research & Quant Engineering OS

### 7.1 Camadas de referência

| Camada | Responsabilidade | Artefatos |
|---|---|---|
| L0 — Ontologia | Entidades, conceitos, relações e estados | JSON Schema, YAML, glossário |
| L1 — Inquiry | Perguntas, linhas de pesquisa e protocolos | Research Question Registry |
| L2 — Evidence | Fontes, alegações, proveniência e qualidade | Evidence Ledger, Source Manifest |
| L3 — Thesis | Teses, hipóteses, cenários e falsificadores | Thesis Registry |
| L4 — Experiment | Experimentos, variáveis, desenho e execução | Experiment Registry |
| L5 — Data | Ingestão, limpeza, validação e versionamento | Parquet, DuckDB, manifests |
| L6 — Quant | Estatística, modelos, otimização e backtests | Python, notebooks, pacotes |
| L7 — Simulation | Agentes, mecanismos, cenários e stress | Simuladores e specs |
| L8 — Governance | Regras, direitos, propostas e treasury sandbox | DAO adapters, policy engine |
| L9 — Agentic | Planner, workers, skills, ferramentas e verificação | Task contracts, MCP, runners |
| L10 — Evaluation | Testes, benchmarks, red team e replicação | pytest, evals, CI |
| L11 — Interface | UI, mapas, relatórios e Emacs Org | WebApp, dashboards, Org |
| L12 — Audit | Logs, decisões, custos, versões e aprovações | JSONL, SQLite/DuckDB, Git |

### 7.2 Arquitetura lógica

[
\text{Inquiry}
\rightarrow \text{Evidence Graph}
\rightarrow \text{Thesis Registry}
\rightarrow \text{Experiment Registry}
\rightarrow \text{Quant Engine / Simulator}
\rightarrow \text{Evaluation Harness}
\rightarrow \text{Human Decision}
\rightarrow \text{Decision Ledger}
\]

Os fluxos devem ser reexecutáveis a partir de manifests versionados. O relatório é uma projeção dos dados e resultados, não a única fonte de verdade.

### 7.3 Monorepo e interoperabilidade

Possível organização evolutiva:

- `research/`: linhas, perguntas, protocolos, revisões;
- `evidence/`: fontes, claims, bibliografia e proveniência;
- `theses/`: catálogo e registros estruturados;
- `experiments/`: manifests, notebooks e resultados;
- `data/`: schemas, fixtures e dados sintéticos;
- `quant/`: fatores, séries, portfolio, risk, backtest;
- `simulation/`: jogos, ABM, cenários e governança;
- `governance/`: regras, propostas, direitos e políticas;
- `agents/`: contratos, prompts, skills e workflows;
- `interfaces/`: WebApp, visualizações e exportadores;
- `reports/`: relatórios Org/Markdown gerados;
- `tests/`: unit, property, integration, regression, statistical;
- `docs/adr/`: decisões arquiteturais;
- `infra/`: CI, containers e configuração.

Não mover tudo para um monorepo antes de mapear dependências, licenças, versões, testes e fronteiras de domínio. O monorepo é uma hipótese de organização; pode haver subprojetos externos como dependências versionadas.

### 7.4 Paradigmas de programação

Adotar pragmatismo explícito:
- **Funcional:** transformações determinísticas, métricas e pipelines;
- **Orientado a objetos:** domínio com entidades e políticas quando houver estado/invariantes;
- **Declarativo:** schemas, manifests, queries e protocolos;
- **Event-driven:** eventos de experimento, propostas, decisões e auditoria;
- **Data-oriented:** processamento colunar e grandes séries;
- **Agentic:** apenas tarefas com planejamento, ferramentas, estado e revisão;
- **Probabilístico:** modelos estatísticos e inferência;
- **Symbolic/neurosymbolic:** ontologias, regras e relações explicáveis.

Não escolher paradigma por moda. Cada módulo declara por que o paradigma reduz complexidade e quais invariantes protege.

---

## 8. Frameworks e ecossistema: mapa de candidatos para pesquisa

Esta lista é um **ponto de partida de investigação**, não uma afirmação de compatibilidade atual nem uma recomendação automática de adoção. Confirmar versões, manutenção, licenças, APIs e documentação oficial antes de integrar.

### 8.1 Data engineering e research

| Família | Candidatos para investigar | Papel possível |
|---|---|---|
| Dataframes | pandas, Polars, Apache Arrow | Transformação tabular e interoperabilidade |
| Query local | DuckDB | Pesquisa analítica local, SQL sobre arquivos |
| Storage | Parquet, SQLite, PostgreSQL | Persistência e formatos |
| Orquestração | Dagster, Prefect, Airflow | Pipelines e agendamento |
| Data quality | Great Expectations, Pandera | Contratos e validação de dados |
| Versionamento | DVC, lakeFS, Git LFS conforme caso | Versionar datasets e artefatos |
| Catálogo/lineage | OpenLineage e ferramentas compatíveis | Proveniência de pipelines |

### 8.2 Quant research, backtesting e portfolio

| Família | Candidatos | Questões para avaliar |
|---|---|---|
| Backtesting Python | vectorbt, Backtrader, Zipline-reloaded | Semântica de ordens, custos, calendário, look-ahead |
| Engine institucional/open source | LEAN / QuantConnect engine | Licença, adapters, dados, complexidade operacional |
| Pesquisa quantitativa | statsmodels, SciPy, scikit-learn | Adequação estatística e validação |
| Bayesian | PyMC, Stan | Priors, diagnóstico, custo computacional |
| Otimização | CVXPY, SciPy optimize, PyPortfolioOpt | Restrições, estabilidade e robustez |
| ML research | Qlib e bibliotecas correlatas | Data leakage, benchmarks e maturidade |
| Experiment tracking | MLflow, Optuna | Runs, parâmetros, artefatos e tuning |

Critérios mínimos: preço ajustado, corporate actions, survivorship, calendário, execução realista, slippage, spread, liquidez, borrow, funding, impostos aplicáveis, latência e custos de dados. A biblioteca não corrige dados ruins nem desenho experimental enviesado.

### 8.3 Simulação, economia e governança

| Família | Candidatos | Uso possível |
|---|---|---|
| System dynamics | Machinations | Fluxos de recursos, estoques, incentivos |
| ABM | Mesa | Agentes, interação e emergência |
| Simulação econômica | cadCAD e frameworks correlatos | Sistemas dinâmicos e políticas |
| Mecanismos | bibliotecas de jogos/otimização a selecionar | Leilões, votação, alocação |
| Formal methods | TLA+, Alloy, model checking | Invariantes, estados e segurança de regras |

Não presumir que ACT-R, LIDA, HTM, MAML ou RL sejam necessários para a primeira versão. São linhas de pesquisa especializadas. Avaliar validade empírica, manutenção, custo, adequação ao problema e risco de antropomorfização antes de adotar.

### 8.4 IA, agentes e conhecimento

Investigar, conforme necessidade:
- APIs de modelos e runtimes agênticos;
- MCP e conectores com permissões mínimas;
- DSPy para otimização declarativa de programas com LLM, quando houver métricas e dataset de avaliação;
- RAG e índices híbridos para corpora;
- bibliotecas de grafos e bancos de grafos;
- frameworks de avaliação de LLMs e observabilidade;
- ferramentas de extração documental e parsing financeiro.

**Regra de seleção:** feature fit + qualidade de código + manutenção + licença + interoperabilidade + custo total + segurança + facilidade de remoção. Comparar recursos por testes e contratos, não por quantidade de badges no README.

### 8.5 Matriz de comparação de frameworks

Para cada framework, pontuar de 0 a 5 e registrar evidência:
- aderência ao problema;
- maturidade e atividade do projeto;
- documentação e exemplos;
- qualidade e cobertura dos testes;
- API estável e extensível;
- integração com formatos abertos;
- performance e memória;
- compatibilidade com hardware disponível;
- segurança e superfície de ataque;
- licença e restrições;
- custo de adoção/manutenção;
- facilidade de substituição.

Peso deve ser definido antes da comparação. Incluir coluna “não verificado” e penalidade para alegações sem evidência. Não somar notas como se fossem medida objetiva universal.

---

## 9. Framework de pesquisa quantitativa e financeira

### 9.1 Pipeline quant

1. Definir universo e hipótese;
2. Congelar data de corte e universo elegível;
3. Obter dados e registrar licenças;
4. Validar schema, integridade, timezone, calendário e corporate actions;
5. Construir features sem vazamento temporal;
6. Definir benchmark e baseline simples;
7. Separar treino, validação e teste temporal;
8. Executar walk-forward ou nested validation conforme problema;
9. Incluir custos, liquidez e restrições de execução;
10. Avaliar estabilidade por regime e subperíodo;
11. Fazer stress tests e análise de sensibilidade;
12. Rodar Red Team e replicação;
13. Registrar resultado, incerteza e decisão.

### 9.2 Métricas

Não depender de uma métrica única. Conforme estratégia:
- retorno bruto e líquido;
- volatilidade e downside deviation;
- drawdown e duração;
- Sharpe/Sortino com ressalvas;
- turnover e custos;
- exposição e concentração;
- beta/fatores;
- hit rate e payoff ratio;
- calibration/Brier score para previsões probabilísticas;
- estabilidade por período/regime;
- capacity e liquidez;
- performance relativa ao benchmark;
- métricas de risco de cauda.

Métricas de retorno devem declarar frequência, moeda, janela, anualização, benchmark, custos e método. Sharpe não é prova de robustez; drawdown histórico não é limite de perda futura.

### 9.3 Barreiras contra erros quantitativos

- Look-ahead bias;
- survivorship bias;
- selection bias;
- data snooping e múltiplos testes;
- p-hacking e escolha oportunista de janela;
- leakage em features e normalização;
- overfitting e hiperparâmetros excessivos;
- regime shift e não estacionariedade;
- autocorrelação e dependência temporal;
- custos de transação omitidos;
- execução impossível ou preço irreal;
- delisting e corporate actions;
- missing data imputados sem justificativa;
- benchmark inadequado;
- seleção retrospectiva de ativos vencedores.

Registrar quantas variantes foram testadas, inclusive as descartadas. Aplicar correções ou controles apropriados para multiplicidade e seleção de modelos quando a família de testes justificar. O holdout não pode ser reutilizado indefinidamente.

### 9.4 Backtest como experimento, não como evidência final

Um backtest deve conter:
- hipótese e racional econômico;
- período, universo e fonte de dados;
- regra de sinal e execução;
- benchmark e baseline;
- custos e restrições;
- protocolo temporal;
- parâmetros e seeds;
- métricas;
- sensibilidade;
- limitações;
- resultados negativos;
- código/commit e ambiente.

Progressão de evidência:
`SANITY_CHECK → IN_SAMPLE → OUT_OF_SAMPLE → WALK_FORWARD → PAPER_TRADING → SMALL_SCALE_LIVE (se aprovado) → MONITORAMENTO`.

Cada estágio exige autorização própria. Resultado em paper trading não equivale a execução real; sucesso passado não autoriza aumento automático de capital.

---

## 10. Governança de smart money e DAOs como laboratórios vivos

### 10.1 DAO como laboratório de governança subjetiva e institucional

A DAO é uma unidade de estudo para observar como crenças, identidades, reputação, regras, tokens, capital e informação influenciam decisões coletivas. “Subjetiva” significa que valores, percepções e interpretações afetam a ação; não significa que a governança possa ser avaliada apenas por narrativas.

Perguntas:
- Quem propõe, delibera, executa, fiscaliza e captura valor?
- Como direitos de voto se relacionam a capital, contribuição e conhecimento?
- Como delegação, quórum, veto e timelock alteram resultados?
- Como evitar plutocracia, captura por insiders, sybil e baixa participação?
- Como se mede adicionalidade e resultado do treasury?
- Como se registra dissenso e conflito de interesse?

### 10.2 Pesquisa de ecossistema DAO

Para cada DAO:
1. identificar repositório oficial, documentação e contratos;
2. mapear organização, módulos, dependências e histórico de commits;
3. mapear propostas, fóruns, votações e execução on-chain quando disponíveis;
4. identificar treasury, ativos, entradas/saídas e política de grants;
5. mapear delegados, direitos, quórum e mecanismos de veto;
6. identificar indicadores de participação e concentração;
7. ler contratos relevantes e auditorias;
8. comparar documentação com implementação;
9. executar análise de risco e threat modeling;
10. construir adapter somente depois de uma PoC read-only.

Não inferir governança real apenas a partir do README. Verificar contratos implantados, endereços, chain, versões, histórico e fontes oficiais.

### 10.3 Experimentos de mecanismo

Exemplos:
- votação quadrática vs token-weighted;
- delegação livre vs delegação temática;
- funding por milestone vs retroactive public goods funding;
- reputação não transferível vs token fungível;
- orçamento participativo vs comitê;
- matching funds vs ranking por voto;
- grants por forecast de impacto vs avaliação ex post.

Definir população, unidade de randomização, contaminação, desfecho, horizonte, custos e riscos de manipulação. Em ambientes reais, não alterar regras nem alocar treasury sem autorização da DAO e revisão legal/técnica.

### 10.4 Smart Money Governance Engine

Módulos propostos:
- `MandateRegistry`: mandato, objetivos e restrições;
- `ProposalRegistry`: propostas e versões;
- `EvidenceLedger`: alegações e fontes;
- `AllocationPolicy`: critérios e limites;
- `ConflictRegistry`: conflitos e recusas;
- `VotingAdapter`: leitura de votação/delegação;
- `TreasuryReadModel`: visão read-only de tesouraria;
- `MilestoneTracker`: entregas e evidências;
- `OutcomeEvaluator`: avaliação ex post;
- `AuditTrail`: eventos e aprovações.

A primeira versão é somente leitura e simulação. Escrita on-chain, assinatura e transferência de ativos ficam fora do escopo inicial.

---

## 11. Simulação e experiências de pensamento

### 11.1 Tipos de simulação

- **Texto / thought experiment:** explorar coerência, paradoxos e casos-limite;
- **Jogo:** testar incentivos, estratégia e informação;
- **Monte Carlo:** propagar incerteza paramétrica;
- **System dynamics:** estoques, fluxos e feedback;
- **Agent-based:** heterogeneidade e interação;
- **Discrete event:** filas, latência e processos;
- **Scenario analysis:** futuros alternativos;
- **Stress test:** choques extremos plausíveis;
- **Digital twin:** representar sistema real com dados atualizados, somente quando houver calibração e governança.

### 11.2 Triângulo da Sabedoria

[
\text{Pergunta (Atma Vichara)}
\rightarrow \text{Mistério (limite do conhecido)}
\rightarrow \text{Algoritmo (protocolo executável)}
\rightarrow \text{Nova pergunta}
]

É uma heurística de design, não uma teoria científica validada. Sua função é manter a pergunta viva enquanto a investigação ganha precisão.

### 11.3 Smart Grid de Mistérios

Uma rede de questões abertas:
- nós = perguntas, conceitos, hipóteses, fontes, experimentos;
- arestas = depende de, contradiz, sustenta, operacionaliza, replica;
- prioridade = relevância × incerteza × testabilidade × valor de informação;
- energia = orçamento de pesquisa, tempo e capacidade;
- polinização = reutilização de método, dado ou insight entre linhas.

O motor de IA pode sugerir lacunas e relações; pesquisadores validam. A metáfora não deve ser confundida com uma medida objetiva de consciência ou inteligência.

### 11.4 ACT-R, LIDA, HTM, MAML e RL: posição cautelosa

Esses modelos e paradigmas podem inspirar módulos de memória, ciclos de atenção, aprendizagem e adaptação, mas não devem ser combinados como se formassem uma arquitetura cognitiva universal.

- ACT-R: investigar para tarefas em que memória declarativa/procedural e modelos cognitivos sejam relevantes;
- LIDA: investigar ciclos cognitivos e atenção em agentes, com escopo experimental;
- HTM: investigar representações temporais hierárquicas, sem presumir superioridade;
- MAML/meta-learning: usar apenas se o problema exigir adaptação entre tarefas com dados adequados;
- Reinforcement Learning: aplicar quando houver ambiente, reward design, segurança e avaliação robusta.

“Foco cognitivo” gamificado não deve simular diagnóstico emocional nem alegar medir capacidade mental. Preferir indicadores voluntários de carga, fricção, tempo e satisfação.

---

## 12. Gestão de experimentos e administração científica

### 12.1 Registro canônico

Cada experimento tem:
- `experiment_id`, título, owner e linha de pesquisa;
- pergunta, hipótese nula/alternativa e mecanismo;
- método, população/unidade, amostra e comparador;
- variáveis independentes, dependentes e confundidores;
- protocolo, preregistro e versão;
- datasets, licenças, hashes e data cutoff;
- código, ambiente, dependências e seed;
- plano estatístico e métricas primárias/secundárias;
- critérios de exclusão e tratamento de missing;
- riscos éticos, privacidade e conflitos;
- desvios, incidentes e resultados;
- revisão independente, replicação e conclusão;
- vínculos com tese, operação e decisão.

### 12.2 Gestão de recursos

Registrar orçamento de:
- dinheiro;
- horas e capacidade de execução;
- compute, storage e APIs;
- acesso a dados;
- atenção e custo de contexto;
- manutenção e dívida técnica;
- custo de oportunidade.

Não reduzir todos esses custos a um único score sem manter as unidades originais e declarar as taxas de conversão.

### 12.3 Ciclo de vida

`IDEA → QUESTION → PROTOCOL → PREREGISTRATION → BUILD → RUN → QA → REVIEW → REPLICATE → PUBLISH → ARCHIVE`.

Estados e transições devem ser explícitos; experimentos podem ser encerrados por falta de dados, inviabilidade ética, custo, irrelevância ou refutação.

---

## 13. Knowledge Graph e curadoria colaborativa

### 13.1 Modelo de grafo

Entidades:
- ResearchQuestion;
- ResearchLine;
- Concept;
- Claim;
- Source;
- Dataset;
- Thesis;
- Hypothesis;
- Experiment;
- Operation;
- Model;
- Framework;
- Repository;
- DAO;
- Proposal;
- Decision;
- Outcome;
- Contributor;
- Artifact.

Relações:
`SUPPORTS`, `CONTRADICTS`, `DERIVED_FROM`, `TESTS`, `REPLICATES`, `DEPENDS_ON`, `IMPLEMENTS`, `GOVERNS`, `ALLOCATES_TO`, `PRODUCES`, `INVALIDATES`.

### 13.2 Critérios de qualidade do conhecimento

- proveniência e autoria;
- data e validade temporal;
- versão e integridade;
- evidência direta vs inferência;
- replicabilidade;
- conflito e desacordo;
- licença e permissão;
- grau de incerteza;
- ligação a pergunta e decisão;
- revisão humana.

### 13.3 IA identifica gaps

A IA pode sugerir:
- hipóteses sem falsificador;
- conceitos sem definição operacional;
- claims sem fonte primária;
- experimentos sem baseline;
- teses sem evidência contrária;
- decisões sem hipótese registrada;
- datasets sem licença ou data cutoff;
- frameworks sem teste de integração;
- resultados sem replicação;
- nós isolados ou relações contraditórias.

Cada sugestão vira issue ou tarefa revisável, nunca alteração silenciosa no grafo.

### 13.4 IPFS e armazenamento distribuído

O grafo pode ser exportado como JSON-LD/JSON e, futuramente, armazenado em IPFS com CID e versionamento por conteúdo. Não colocar dados pessoais, segredos, dados financeiros privados ou informação sensível em armazenamento público/imutável. IPFS não é banco transacional nem camada de autorização; manter índice, controle de acesso e política de remoção para dados fora da rede distribuída.

---

## 14. Interfaces: laboratório simbólico educacional

### 14.1 Áreas de produto

- **Inquiry Studio:** formular perguntas e linhas de pesquisa;
- **Research Navigator:** landscape, fontes, links e revisões;
- **Evidence Graph:** claims, fontes, controvérsias e lacunas;
- **Thesis Lab:** hipóteses, cenários e falsificadores;
- **Experiment Designer:** protocolo, variáveis, baseline e pré-registro;
- **Quant Workbench:** dados, features, backtests e notebooks;
- **Simulation Garden:** jogos, cenários e mecanismos;
- **DAO Observatory:** propostas, treasury, delegação e execução;
- **Decision Journal:** hipóteses de operações e resultados;
- **Knowledge Garden:** conceitos, mapas e curadoria;
- **Prompt/Agent Lab:** tarefas, contratos, modelos e avaliação;
- **Learning Path:** onboarding, missões e documentação;
- **Org Exporter:** relatórios e diários compatíveis com Emacs Org mode.

### 14.2 Visualizações

- mapas interativos de ecossistema;
- grafos de conhecimento e dependência;
- fluxogramas de recursos e tesouraria;
- timelines de hipóteses, experimentos e decisões;
- curvas de equity e drawdown com ressalvas;
- distribuições, intervalos e sensibilidades;
- mapas de calor de robustez;
- Sankey de fontes e usos de capital;
- diagramas de governança;
- dashboards de qualidade de evidência.

Toda visualização deve declarar fonte, unidade, período, filtros, método e limites. Evitar dashboards que ocultem incerteza ou incentivem overtrading.

### 14.3 Onboarding DAO–IA–Científico

Trilha:
1. conhecer o mandato e a ontologia;
2. formular pergunta;
3. aprender a distinguir dado, informação e inferência;
4. registrar hipótese;
5. executar DYOR com fontes;
6. construir experimento mínimo;
7. validar código e estatística;
8. participar de revisão/curadoria;
9. simular decisão de alocação;
10. publicar relatório reproduzível.

DYOR é disciplina de investigação e responsabilidade, não transferência da responsabilidade para o usuário nem justificativa para ignorar evidências profissionais.

### 14.4 Gamificação sem distorção

Pode haver missões, guildas, mapas, níveis e recompensas por:
- reproduzir experimento;
- encontrar erro;
- adicionar fonte primária;
- documentar resultado nulo;
- revisar código;
- replicar resultado;
- melhorar protocolo.

Não premiar volume de commits, número de prompts, quantidade de trades ou concordância com o modelo. Recompensas não devem induzir fabricação de resultados, spam, captura de governança ou exposição de dados pessoais.

---

## 15. IA Experimental e laboratório de inteligência híbrida

### 15.1 Princípio

Tratar IA como instrumento experimental e amplificador de relevância compartilhada, não como autoridade. O laboratório compara sistemas, prompts, ferramentas e processos sob tarefas controladas.

### 15.2 Experimentos com IA

- modelo A vs B para extração de dados;
- prompt livre vs task contract;
- RAG vs contexto manual;
- agente único vs pipeline multiagente;
- síntese com vs sem Red Team;
- automação integral vs human-in-the-loop;
- interface textual vs visual;
- recuperação lexical vs híbrida/graph;
- modelo geral vs modelo especializado.

### 15.3 Métricas

- precisão, recall e F1 quando houver ground truth;
- taxa de afirmações com fonte válida;
- erro numérico e reconciliação;
- completude de extração;
- taxa de alucinação categorizada;
- calibração e Brier score;
- consistência entre execuções;
- tempo, custo e latência;
- taxa de intervenção humana;
- taxa de falhas críticas;
- satisfação e compreensão do usuário;
- reprodutibilidade por runtime.

### 15.4 Human-in-the-loop e autonomia

Níveis:
- **A0:** observar e explicar;
- **A1:** pesquisar e propor;
- **A2:** gerar artefato em sandbox;
- **A3:** executar testes e alterar branch isolada;
- **A4:** abrir PR para revisão humana;
- **A5:** produção ou transação somente com autorização explícita, controles externos e trilha de auditoria.

Para finanças e DAO, o padrão inicial é A0–A2. Não permitir que LLM decida sozinho alocação real, assine transação, mova treasury ou altere política de risco.

---

## 16. Prova de conceito: primeiro experimento vertical

### 16.1 Objetivo

Demonstrar o ciclo completo de uma tese existente até uma decisão simulada, com evidência rastreável, código testado e relatório Org.

### 16.2 Experimento POC-01

**Pergunta:** um protocolo explícito de hipótese–evidência–falsificação melhora a qualidade e reprodutibilidade de uma análise de tese em comparação com um fluxo livre de prompt?

**Desenho:**
- selecionar uma tese do catálogo;
- usar somente dados públicos ou sintéticos, conforme disponibilidade;
- criar dois fluxos: baseline livre e fluxo científico estruturado;
- usar mesmo conjunto de fontes e mesma data de corte;
- gerar análises sem revelar ao avaliador qual fluxo produziu cada artefato;
- avaliar completude, rastreabilidade, coerência, contradições, erros e tempo;
- repetir em duas runtimes/modelos se disponível;
- executar Red Team independente.

**Desfechos primários:**
- proporção de claims com suporte rastreável;
- proporção de hipóteses com falsificador explícito;
- erros materiais por relatório;
- reprodutibilidade do pipeline.

**Secundários:** tempo, custo, usabilidade e confiança calibrada.

**Limite:** POC testa processo de pesquisa, não rentabilidade de uma estratégia.

### 16.3 Simular o projeto pronto antes de construir

Produzir:
- diagrama de arquitetura;
- journeys UX/DX/LX;
- schemas de tese, experimento, operação e evidência;
- dados sintéticos;
- simulação de uma execução feliz;
- simulação de falha de dados, fonte, API, modelo e teste;
- relatório esperado;
- code review de arquitetura;
- backlog de implementação.

Simulação textual não equivale a execução. Marcar cada artefato como `SIMULADO`, `IMPLEMENTADO` ou `VERIFICADO`.

---

## 17. Testes, debugging e revisão de código

### 17.1 Pirâmide de testes

- **Unit:** funções, indicadores, conversões, cálculos e regras;
- **Property-based:** invariantes matemáticos e propriedades;
- **Golden tests:** fixtures e resultados esperados;
- **Integration:** APIs, formatos, bancos e adaptadores;
- **Contract tests:** compatibilidade entre módulos e repositórios;
- **Statistical tests:** calibração, cobertura, estabilidade e regressão;
- **Backtest sanity tests:** datas, custos, posições e execução;
- **E2E:** journeys de UI;
- **Security:** secrets, permissões, dependências e threat model;
- **Reproducibility:** ambiente limpo e execução a partir do manifest.

### 17.2 Smart follow-ups como debugging simulado

A cada execução, gerar perguntas:
- Que premissa pode ter quebrado?
- Qual input foi usado e qual foi omitido?
- O que muda se deslocarmos o cutoff?
- O resultado depende de uma única fonte ou período?
- O módulo está acoplado a detalhe interno de outro repo?
- Qual teste falharia se a hipótese estivesse errada?
- Qual cenário adverso não foi simulado?
- O resultado pode ser reproduzido por outro runtime?

Agentes podem simular falhas e propor testes; só o runner pode declarar teste executado. Logs devem distinguir `SIMULATED`, `EXECUTED`, `PASSED`, `FAILED`, `NOT_RUN`.

### 17.3 Code review científico

Revisar quatro planos:
1. **Software:** correção, legibilidade, segurança, arquitetura;
2. **Dados:** proveniência, integridade, leakage e validade;
3. **Método:** desenho, estatística, falsificabilidade e limitações;
4. **Domínio:** coerência financeira, econômica, institucional e de governança.

Nenhum PR de cálculo financeiro deve ser aprovado apenas porque os testes de UI passam.

---

## 18. Open science, DeSci, citizen science e economia do conhecimento

### 18.1 Princípios

- publicar protocolos e resultados reproduzíveis sempre que possível;
- versionar dados e código com licenças claras;
- separar dados abertos, restritos e privados;
- permitir replicação e crítica;
- reconhecer contribuição intelectual e operacional;
- preservar resultados negativos;
- declarar conflitos e financiamento;
- não confundir tokenização com ciência aberta.

### 18.2 DAO e financiamento de ciência

Possibilidades experimentais:
- grants por pergunta de pesquisa;
- bounties por reprodução de resultados;
- financiamento por milestones;
- curadoria colaborativa;
- retroactive funding de artefatos públicos;
- reputação baseada em contribuições verificáveis;
- governança participativa de agenda científica.

Avaliar concentração de poder, conflitos, sybil, captura por popularidade, qualidade da revisão e sustentabilidade financeira. Token não é sinônimo de mérito científico.

### 18.3 Economia do conhecimento e da experiência

Registrar separadamente:
- valor informacional;
- valor de conhecimento;
- valor experiencial;
- valor de uso;
- valor de opção;
- valor econômico capturado;
- valor público/social;
- custo e externalidades.

“Coinhecimento” pode ser usado como conceito experimental para conhecimento tácito produzido em colaboração humano–IA, desde que se defina o que foi criado, por quem, com qual contribuição e como pode ser verificado.

---

## 19. Ética, privacidade, segurança e governança

- minimização e classificação de dados;
- consentimento para logs de interação e autoetnografia;
- dados pessoais e financeiros em ambiente privado;
- segredos e chaves fora de prompts, logs e repositórios;
- least privilege para agentes e conectores;
- sandbox para código não confiável;
- dependências pinadas e SBOM quando apropriado;
- threat modeling para contratos e DAO adapters;
- revisão humana para ações irreversíveis;
- política de retenção e exclusão;
- licenças de dados, código e publicações;
- disclosure de conflito de interesse;
- distinção entre protótipo, experimento, produto e aconselhamento financeiro.

Não publicar em GitHub aberto perfis financeiros, diários sensíveis, tokens de API, logs privados ou identificadores pessoais. Usar dados sintéticos e fixtures claramente rotulados.

---

## 20. Roadmap de implementação

### P0 — Fundação científica
- registrar esta spec;
- ligar linhas de pesquisa ao catálogo de teses;
- definir schemas canônicos;
- aprovar estados epistêmicos e experimentais;
- criar ADR de arquitetura e política de dados.

### P1 — Inquiry & Evidence
- Research Question Registry;
- Source Manifest;
- Evidence Ledger;
- claim extraction com validação humana;
- relatório de landscape e revisão sistemática piloto.

### P2 — Thesis & Experiment Registry
- schema de hipótese;
- registro de experimento;
- pré-registro;
- versionamento e ligação entre tese, operação e evidência;
- exportação Org/Markdown.

### P3 — Quant Research vertical
- dataset sintético;
- pipeline de dados e qualidade;
- baseline simples;
- backtest com custos;
- walk-forward;
- relatório reprodutível e testes.

### P4 — IA Experimental
- benchmark de tarefas;
- prompt/task contracts;
- comparação de modelos e runtimes;
- Red Team e avaliação de evidência;
- logs com privacidade.

### P5 — Simulation & DAO Observatory
- simulador de mecanismo;
- DAO adapter read-only;
- grafo de governança;
- análise de propostas e tesouraria;
- cenários e stress.

### P6 — Interfaces e laboratório vivo
- Inquiry Studio;
- Evidence Graph;
- Experiment Designer;
- Quant Workbench;
- dashboards e onboarding;
- UX/DX/LX/IX research.

### P7 — Reprodutibilidade e publicação
- CI científico;
- ambientes reproduzíveis;
- relatórios públicos;
- replicação externa;
- publicação de resultados negativos;
- avaliação de impacto e sustentabilidade.

**Sequenciamento:** não iniciar P1–P7 em paralelo. Construir uma fatia vertical pequena, validar contratos e somente então ampliar.

---

## 21. Backlog de artefatos iniciais

1. `schemas/research-question.schema.json`
2. `schemas/evidence-claim.schema.json`
3. `schemas/thesis.schema.json`
4. `schemas/experiment.schema.json`
5. `schemas/operation-hypothesis.schema.json`
6. `schemas/framework-evaluation.schema.json`
7. `research/lines-of-inquiry.yaml`
8. `research/source-manifest.yaml`
9. `research/protocols/POC-01.md`
10. `experiments/registry.yaml`
11. `quant/baselines/`
12. `simulation/dao-governance/`
13. `tests/scientific_validation/`
14. `docs/adr/ADR-0001-scientific-lab-architecture.md`

Esses são artefatos propostos, não arquivos já implementados.

---

## 22. Prompts de trabalho para o laboratório

### 22.1 Orientador científico
> Atue como orientador de pesquisa transdisciplinar em finanças computacionais. Ajude a formular a pergunta, delimitar a linha de inquiry, escolher método, declarar pressupostos, construir framework teórico/conceitual, identificar literatura primária e definir critérios de qualidade. Não preencha lacunas com autoridade retórica.

### 22.2 Quant researcher
> Converta a tese em hipótese quantitativa falsificável. Defina universo, variáveis, mecanismo, benchmark, baseline, data cutoff, desenho temporal, custos, métricas, testes de robustez e condições de invalidação. Liste riscos de leakage, múltiplos testes, survivorship e regime shift.

### 22.3 Quant developer
> Implemente a menor fatia reproduzível. Antes de codificar, inspecione arquitetura, dependências, licença e APIs. Defina interfaces, schemas, fixtures, testes unitários, property tests e integração. Não altere contratos externos sem ADR. Execute testes e reporte comandos, resultados reais, limitações e arquivos modificados.

### 22.4 Analista / Red Team
> Construa o argumento contrário mais forte. Procure evidências que contradizem a tese, vieses, explicações alternativas, fragilidade de premissas, captura de valor, riscos de liquidez, custos, conflitos de interesse e cenários de perda. Diferencie risco mensurável de incerteza radical.

### 22.5 Designer UX/DX/LX/IX
> Desenhe uma experiência que ajude o pesquisador a formular, executar, compreender e revisar experimentos. Defina personas funcionais, tarefas, estados, acessibilidade, métricas e riscos de confiança excessiva em IA. Não use gamificação para induzir trades ou produtividade compulsiva.

### 22.6 Integrador de repositórios e DAOs
> Inspecione o repositório oficial e documentação da DAO/framework. Confirme organização, versão, licença, contratos, dependências, APIs, testes, issues e histórico. Compare features por evidência no código. Proponha adapter read-only, contract tests e PoC isolada. Não presumir interoperabilidade pela semelhança de nomes.

### 22.7 Meta-prompt de refinamento
> Faça uma metacrítica do plano: o que está amplo demais, o que não é falsificável, quais métodos são inadequados, que dados não existem, quais módulos são prematuros e qual é o menor experimento que produz conhecimento útil? Reescreva o plano preservando rastreabilidade entre pergunta, método, código, resultado e decisão.

---

## 23. Critérios de aceite (Definition of Done)

A primeira versão científica só será considerada funcional quando:
- uma pergunta de pesquisa estiver registrada e versionada;
- uma tese existente estiver ligada a uma hipótese específica;
- um protocolo declarar método, dados, métricas e falsificadores;
- dados sintéticos ou públicos tiverem proveniência e cutoff;
- código executar em ambiente documentado;
- testes determinísticos e validações científicas forem executados;
- resultado negativo ou inconclusivo puder ser registrado;
- relatório Org/Markdown for gerado com citações e limitações;
- outra pessoa/runtime conseguir reproduzir a execução;
- nenhuma operação financeira real puder ser disparada pelo fluxo;
- logs e dados privados obedecerem à política de segurança.

### Estados de maturidade

`IDEA → SPECIFIED → PROTOTYPED → IMPLEMENTED → TESTED → REPRODUCIBLE → REPLICATED → VALIDATED`.

Não usar “cientificamente validado” como sinônimo de “implementado”, “testado” ou “backtest positivo”.

---

## 24. Metacrítica: limites e melhorias contínuas

### Riscos da própria proposta

1. **Escopo excessivo:** ciência, finanças, IA, DAO, UX, cognição e regeneratividade podem produzir um sistema impossível de terminar.
2. **Metáfora substituindo método:** termos como laboratório vivo, mistério, alquimia e sabedoria inspiram, mas precisam de tradução operacional.
3. **Framework maximalista:** ACT-R + LIDA + HTM + RL + MAML não constitui automaticamente uma arquitetura coerente.
4. **Automação da revisão:** IA pode acelerar triagem e síntese, mas também reproduzir vieses e criar consenso artificial.
5. **Quantificação do incomensurável:** nem toda experiência, contribuição, confiança ou impacto cabe em score.
6. **DAO como proxy de descentralização:** token voting não garante participação justa, distribuição de poder ou legitimidade.
7. **Backtest como narrativa:** resultados retrospectivos podem premiar sobreajuste.
8. **Autoetnografia como prova causal:** experiência pessoal é fonte legítima de inquiry, não substitui validação externa.
9. **Custo de manutenção:** cada framework adiciona dependências, superfície de ataque e carga cognitiva.
10. **Confusão entre pesquisa e ação:** produzir uma tese ou sinal não deve automaticamente produzir uma transação.

### Princípios de correção

- começar pela pergunta, não pela tecnologia;
- usar o método mais simples capaz de responder;
- preferir dados e contratos abertos;
- registrar incerteza e desacordo;
- separar descoberta exploratória de teste confirmatório;
- exigir evidência incremental para cada nova camada;
- manter o sistema útil mesmo sem blockchain, token ou agente autônomo;
- tratar não agir como opção legítima;
- privilegiar robustez, auditabilidade e reversibilidade;
- permitir que resultados refutem as premissas do próprio projeto.

**Filosofema final:** *O laboratório não existe para confirmar a inteligência do pesquisador nem a eloquência da IA. Existe para organizar condições nas quais ambos possam descobrir que estavam errados — e melhorar o próximo experimento.*

---

## 25. Referências metodológicas e fontes a verificar

A pesquisa de implementação deve consultar as versões atuais e fontes primárias de:
- Design Science Research e avaliação de artefatos;
- PRISMA e diretrizes de revisão sistemática;
- Cochrane Handbook e métodos de risco de viés, quando aplicáveis;
- Open Science Framework e práticas de pré-registro;
- FAIR principles para dados científicos;
- documentação oficial dos frameworks quant, data, simulation e agentic selecionados;
- documentação oficial de cada DAO, seus repositórios e contratos;
- literatura de backtesting, data snooping, multiple testing e validação temporal;
- literatura de governança de commons, mecanismo de votação e financiamento de bens públicos.

A lista acima é um roteiro bibliográfico, não uma revisão sistemática já executada. Registrar cada fonte efetivamente consultada no `Source Manifest`, com data, versão, referência e papel na conclusão.

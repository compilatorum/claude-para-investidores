# 🧠 Machinations Simulation Blueprint — Capital Intelligence & Decision Learning System

> **Versão:** 1.0 · **Data:** 2026-10-31  
> **Repositório:** `compilatorum/claude-para-investidores`  
> **Tipo:** especificação de simulação sistêmica, prompt mestre para Machinations AI Agent e manual de construção, execução e interpretação.  
> **Relaciona-se a:** Plano de Upgrade I, Plano de Upgrade II, Meta-Prompt Template Chain e Postman API Platform Blueprint.  
> **Natureza:** modelo conceitual e experimental. Não representa uma implementação operacional nem uma previsão financeira.

---

## 0. Tese central

O repositório deve ser modelado como um **sistema adaptativo de inteligência e alocação de capital**. Seu comportamento emerge da interação entre recursos escassos, oportunidades, informação, decisões, execução, validação, risco e aprendizagem.

O objetivo da simulação não é representar cada arquivo ou endpoint como um nó. É representar os mecanismos econômicos e operacionais que conectam as capacidades do repositório.

\[
\boxed{
\text{Capital Intelligence System}
=
\text{Resources}
+ \text{Opportunities}
+ \text{Information}
+ \text{Decisions}
+ \text{Execution}
+ \text{Risk}
+ \text{Learning}
}
\]

**Filosofema:** *O sistema não cria valor porque produz análises; cria valor quando converte recursos escassos em decisões melhores, resultados verificáveis e novas opções.*

### 0.1 Pergunta central da simulação

> Sob quais condições o sistema consegue transformar recursos limitados — dinheiro, tempo, atenção, conhecimento, computação e relações — em oportunidades sustentáveis de criação e captura de valor, sem consumir sua própria capacidade de continuar operando?

### 0.2 O que deve ser possível investigar

1. Quais são os gargalos do pipeline: dados, pesquisa, validação, execução, financiamento ou adoção?
2. Quando automação e agentes reduzem custos e quando apenas deslocam o gargalo?
3. Qual é o efeito de aumentar a qualidade das fontes e da proveniência?
4. Quanto Red Team e validação reduzem erros, e a que custo de tempo?
5. Como a escassez de liquidez ou runway altera as escolhas entre investimento, desenvolvimento e preservação?
6. Qual combinação de grants, bounties, pilotos, serviços e receitas recorrentes sustenta o sistema?
7. Como evitar que excesso de projetos e complexidade causem dispersão de atenção?
8. Como resultados, reputação e aprendizagem retroalimentam oportunidades futuras?
9. Quais cenários provocam falha, estagnação, dependência de uma única fonte de capital ou crescimento insustentável?
10. Quais parâmetros merecem experimentos reais antes de qualquer implementação?

---

## 1. Limites epistemológicos e de ferramenta

Machinations é uma ferramenta visual de modelagem de sistemas baseada em recursos, nós, conexões, estados e simulações. Seus elementos básicos incluem Sources, Pools, Drains, Converters, Traders e Gates; conexões de recursos representam fluxos e conexões de estado alteram condições, fórmulas ou ativações.

O modelo deve usar esses elementos para representar **estoques e fluxos agregados**.

### 1.1 O que a simulação pode representar

- Estoques de recursos e suas variações por período;
- taxas de conversão e consumo;
- filas e atrasos de execução;
- alocação entre alternativas;
- probabilidades e distribuições de cenários;
- limites de capacidade e saturação;
- condições de ativação e parada;
- ciclos de feedback positivos e negativos;
- sensibilidade a parâmetros;
- resultados comparativos entre cenários.

### 1.2 O que não se deve presumir

- A simulação não executa Python, APIs, modelos LLM, agentes ou workflows do repositório.
- Um nó chamado Agent não é um agente autônomo real; é uma abstração de capacidade/custo/produção.
- A ferramenta não substitui backtesting, análise estatística, validação contábil, pesquisa de mercado ou avaliação de investimento.
- Resultados de Monte Carlo dependem das distribuições, fórmulas, correlações e premissas inseridas.
- Não usar o modelo para afirmar retorno esperado, probabilidade real de sucesso empresarial ou suitability.
- Não inserir patrimônio, renda, carteira, passivos ou dados pessoais reais. Começar com unidades normalizadas e dados sintéticos.
- Não representar reputação, conhecimento, saúde, tempo ou relações como se fossem perfeitamente fungíveis ou redutíveis a dinheiro.

### 1.3 Unidade temporal

Usar inicialmente **um Step = um ciclo operacional**, equivalente a uma semana ou sprint. A unidade pode ser alterada depois, mas deve permanecer constante dentro de cada comparação.

Horizonte inicial sugerido: 52 Steps. Para testar ciclos longos, executar 104 ou 156 Steps.

---

## 2. Prompt mestre para o Machinations AI Agent

Copie o conteúdo integral desta seção para o AI Agent do Machinations. Se o agente não conseguir criar todos os componentes de uma vez, solicite a construção em módulos, conforme a seção 4.

### PROMPT — CAPITAL INTELLIGENCE SYSTEM SIMULATION

Você é um Systems Designer especializado em system dynamics, game economies, token engineering, mecanismos de incentivos, alocação de recursos escassos e simulação de sistemas adaptativos.

Crie um diagrama Machinations chamado:

**Capital Intelligence & Decision Learning System — Compilatorum**

#### A. Objetivo do modelo

Modele uma plataforma de inteligência e alocação de capital que recebe recursos limitados, coleta e qualifica informação, formula e testa hipóteses, avalia oportunidades, executa projetos, captura valor, administra riscos e aprende com resultados.

O sistema é uma combinação de:

1. Research & Evidence Engine;
2. Thesis & Opportunity Pipeline;
3. Quantamental Analysis & Evaluation;
4. AI/Agentic Engineering Harness;
5. Capital Allocation Engine;
6. Venture & Revenue Engine;
7. Risk, Liquidity & Resilience Engine;
8. Decision Journal & Learning Loop;
9. Governance & Human Approval.

Não modele apenas uma aplicação de análise de ações. O sistema deve avaliar múltiplas formas de alocação de capital: financeiro, intelectual, cognitivo, computacional, relacional, empreendedor, socioambiental e experiencial. Não some essas formas em uma única unidade monetária; mantenha pools separados e explicite as taxas de conversão quando houver uma hipótese justificável.

#### B. Regras gerais de modelagem

- Use Pools para estoques de recursos e filas.
- Use Sources para entradas exógenas ou geração de recursos.
- Use Drains para consumo, perda, custo, desperdício ou saída do sistema.
- Use Converters para transformação de recursos/capacidades.
- Use Traders quando houver troca explícita entre recursos.
- Use Gates para alocação determinística ou probabilística entre caminhos.
- Use Resource Connections para fluxos.
- Use State Connections para condições, ativação, modificadores e feedback.
- Use Registers ou Custom Variables para métricas agregadas e condições, quando suportadas.
- Dê nomes claros e únicos a todos os nós e conexões.
- Organize o diagrama em camadas ou regiões visuais com títulos.
- Use descrições para explicar fórmulas, hipóteses e unidades.
- Exiba em Charts os principais estoques e indicadores.
- Evite um único diagrama monolítico ilegível: crie subsistemas visuais conectados.
- Não invente funcionalidades de agentes autônomos; represente agentes como recursos/capacidades agregadas.
- Quando uma fórmula não puder ser expressa diretamente, substitua-a por uma aproximação transparente e documente a limitação.

#### C. Recursos e estoques principais

Crie Pools separados para:

**Capital e runway**
- Financial_Capital: caixa operacional abstrato;
- Liquidity_Reserve: reserva disponível;
- Committed_Capital: recursos comprometidos em projetos;
- Operating_Costs: custo acumulado ou saída por período;
- Runway_Buffer: margem operacional agregada.

**Capital não financeiro**
- Attention_Capacity: capacidade de atenção disponível;
- Time_Capacity: capacidade de trabalho disponível;
- Knowledge_Capital: conhecimento reutilizável;
- Computational_Capacity: capacidade de execução computacional;
- Relationship_Capital: acesso e confiança em redes;
- Reputation_Capital: reputação construída por entregas verificáveis;
- IP_Assets: artefatos, software, documentação e propriedade intelectual reutilizável.

**Informação e conhecimento**
- Raw_Information;
- Qualified_Evidence;
- Validated_Theses;
- Research_Backlog;
- Decision_Queue;
- Learning_Assets.

**Execução**
- Task_Backlog;
- Work_In_Progress;
- Validation_Queue;
- Human_Approval_Queue;
- Completed_Artifacts;
- Failed_or_Rework_Tasks.

**Oportunidades**
- Grant_Opportunities;
- Bounty_Opportunities;
- Pilot_Opportunities;
- Service_Opportunities;
- SaaS_Opportunities;
- Investment_Opportunities.

**Risco**
- Operational_Risk_Exposure;
- Model_Error_Exposure;
- Data_Quality_Debt;
- Technical_Debt;
- Concentration_Risk;
- Unvalidated_Commitments.

Use unidades inteiras ou subunidades inteiras quando necessário. Não misture unidades incompatíveis. Para dinheiro abstrato, use unidades monetárias normalizadas (UM); para tempo, use unidades de capacidade (UC); para conhecimento e reputação, use pontos abstratos (PA), sem convertê-los automaticamente em dinheiro.

#### D. Entradas exógenas

Crie Sources configuráveis para:
- novos dados e documentos;
- novas oportunidades de financiamento;
- demanda de clientes/pilotos;
- solicitações de pesquisa;
- novas tarefas e contribuições;
- eventos de mercado/regime;
- choques de custo;
- falhas de ferramentas ou provedores;
- mudanças na qualidade/atualidade das fontes.

As entradas devem poder ser desligadas, reduzidas ou aumentadas em cenários diferentes.

#### E. Pipeline de informação e tese

Modele o caminho:

Raw_Information → Data_Quality_Filter → Qualified_Evidence → Thesis_Formation → Thesis_Validation → Validated_Theses → Opportunity_Screening.

A cada transformação:
- consuma tempo e capacidade computacional;
- aplique uma taxa de perda ou rejeição;
- permita retrabalho por dados conflitantes ou desatualizados;
- aumente Data_Quality_Debt quando evidências insuficientes forem aceitas;
- aumente Knowledge_Capital quando evidências e conclusões forem bem documentadas;
- faça a qualidade de evidência influenciar a probabilidade de uma tese passar na validação.

Não permita que a geração de texto, isoladamente, converta uma hipótese em tese corroborada. Exija validação independente e proveniência.

#### F. Pipeline agêntico e harness

Modele:

Task_Backlog → Context_Builder → Planner → Agent_Workers → Tool_Execution → Evaluator → Red_Team → Human_Approval → Completed_Artifacts.

Inclua:
- custo computacional por tarefa;
- consumo de atenção humana por revisão;
- taxa de falha e retrabalho;
- latência/atraso de fila;
- capacidade limitada por Step;
- ganho de produtividade por automação;
- risco de erro correlacionado entre agentes;
- custo adicional de validação;
- redução de erros por testes, proveniência e Red Team.

Aumentar o número de agentes não deve aumentar automaticamente a qualidade. Use rendimentos decrescentes, custos marginais e risco de coordenação. A aprovação humana deve ser um gate para decisões irreversíveis ou de alto impacto.

#### G. Motor de oportunidades e alocação

Depois do screening, distribua oportunidades por Gate entre:
- Grants;
- Bounties;
- Pilots;
- Productized_Services;
- SaaS_or_API;
- IP_Licensing;
- Financial_Investments;
- Research_or_Exploration;
- Reject_or_Defer.

Cada caminho precisa de:
- custo inicial em UM, UC, atenção e computação;
- tempo de maturação;
- probabilidade de conclusão;
- probabilidade de captura de valor;
- valor/benefício agregado esperado como parâmetro experimental;
- risco de perda;
- liquidez ou reversibilidade;
- dependência de terceiros;
- capacidade de gerar ativos reutilizáveis.

Não suponha que grants, bounties ou investimentos sejam receitas garantidas. Oportunidades podem expirar, ser rejeitadas ou consumir recursos sem retorno.

#### H. Captura de valor e reinvestimento

Modele caminhos de retorno:
- Grant → financiamento restrito ou condicionado;
- Bounty → pagamento por entrega aprovada;
- Pilot → receita inicial, aprendizado e evidência de demanda;
- Service → fluxo de caixa e conhecimento do cliente;
- SaaS/API → receita recorrente, com custos de suporte e infraestrutura;
- IP_Licensing → royalties ou pagamentos por uso;
- Investment → resultado incerto, com risco de perda e liquidez limitada.

Separe:
- Value_Created;
- Value_Captured;
- Cash_Received;
- Reusable_Knowledge;
- Reputation_Gained;
- Customer_Evidence.

Não converta valor criado em caixa automaticamente. Crie taxas de captura e atrasos. Parte do valor pode beneficiar terceiros, permanecer não monetizada ou gerar apenas aprendizagem.

Reinvista uma fração configurável do caixa capturado em:
- reserva;
- manutenção;
- pesquisa;
- produto;
- automação;
- validação;
- novas oportunidades.

A reserva deve ter prioridade mínima antes de compromissos não essenciais.

#### I. Risco e resiliência

Crie mecanismos de:
- custo fixo e variável;
- choque de despesas;
- falha de provedores;
- obsolescência de dados;
- erro de modelo;
- baixa qualidade de evidência;
- concentração de fontes de financiamento;
- atraso de pagamentos;
- fracasso de pilotos;
- perda de capacidade por sobrecarga;
- crescimento de dívida técnica;
- risco de execução e retrabalho.

Use condições de estado para reduzir novas alocações quando a Liquidity_Reserve ou Runway_Buffer cair abaixo de limites configuráveis.

Crie uma condição de parada quando:
- a liquidez for insuficiente para o custo mínimo de operação;
- a fila de tarefas exceder a capacidade por vários Steps;
- o risco operacional ultrapassar um limite;
- o sistema entrar em estado de falha persistente.

Inclua mecanismos de recuperação: pausar projetos, reduzir custos, priorizar entregas com caixa mais rápido, liquidar compromissos reversíveis e preservar ativos reutilizáveis.

#### J. Feedback e aprendizagem

Modele o ciclo:

Completed_Artifacts → Outcome_Observation → Decision_Review → Learning_Assets → Better_Context_and_Validation → Improved_Future_Decisions.

Resultados negativos também devem produzir aprendizagem, mas consumindo recursos. Evite supor que todo fracasso gera aprendizagem automaticamente: use uma taxa de post-mortem e uma taxa de retenção do conhecimento.

A aprendizagem deve:
- reduzir erros futuros somente de forma gradual;
- aumentar a velocidade de tarefas semelhantes;
- melhorar a seleção de oportunidades;
- diminuir retrabalho;
- não eliminar incerteza nem risco.

#### K. Cenários e experimentos

Prepare o diagrama para testar pelo menos:
1. Baseline conservador;
2. Abundância de oportunidades, escassez de atenção;
3. Alta automação e baixa validação;
4. Alta validação e throughput menor;
5. Grants abundantes, baixa recorrência;
6. Pilotos e serviços como ponte para SaaS;
7. Choque de custos e queda de liquidez;
8. Falha de provedor/modelo;
9. Aumento de qualidade de dados;
10. Portfólio excessivamente diversificado;
11. Foco em poucas oportunidades com maior reversibilidade;
12. Aprendizagem acumulativa com ativos reutilizáveis.

Use Predictions/Monte Carlo para variáveis incertas e Charts para comparar:
- caixa e reserva;
- runway;
- tarefas concluídas;
- fila e tempo de ciclo;
- taxa de retrabalho;
- evidências qualificadas;
- teses validadas;
- oportunidades capturadas;
- receitas por canal;
- concentração de receita;
- risco agregado;
- ativos reutilizáveis;
- aprendizagem acumulada.

#### L. Resultado visual esperado

O diagrama final deve ter regiões:
1. Resource Endowment;
2. Information & Evidence;
3. Thesis & Opportunity Pipeline;
4. Agentic Execution & Harness;
5. Capital Allocation;
6. Value Capture & Reinvestment;
7. Risk & Resilience;
8. Decision Learning Loop;
9. Governance & Human Gates.

Inclua uma legenda de unidades, uma legenda de tipos de fluxo, os principais parâmetros editáveis e notas que diferenciem fatos do repositório de hipóteses do modelo.

Antes de finalizar, faça uma checagem de consistência:
- nenhum recurso incompatível deve ser somado;
- todos os fluxos de entrada/saída devem ter origem e destino;
- nenhum caminho de valor deve garantir captura automática;
- os loops devem ter condições de estabilidade ou parada;
- as variáveis de risco devem afetar efetivamente os fluxos;
- o diagrama deve permitir alterar parâmetros sem redesenhar toda a estrutura.

Entregue o diagrama com uma descrição das abstrações adotadas, limitações, variáveis editáveis e sequência sugerida de experimentos.

### FIM DO PROMPT MESTRE

---

## 3. Dicionário de recursos e unidades

O Machinations trabalha com recursos discretos. Por isso, use subunidades inteiras e escalas normalizadas. A tabela é uma convenção experimental, não uma mensuração real do usuário.

| Recurso | Unidade sugerida | Interpretação |
|---|---|---|
| Financial_Capital | UM (unidade monetária) | Caixa abstrato |
| Liquidity_Reserve | UM | Caixa reservado |
| Time_Capacity | UC (unidade de capacidade) | Capacidade de trabalho por Step |
| Attention_Capacity | UA | Capacidade de foco por Step |
| Computational_Capacity | UComp | Capacidade computacional abstrata |
| Knowledge_Capital | PA | Conhecimento reutilizável |
| Relationship_Capital | PR | Capacidade relacional abstrata |
| Reputation_Capital | PRep | Confiança/reputação acumulada |
| IP_Assets | Ativo | Artefato reutilizável |
| Raw_Information | Item | Entrada informacional |
| Qualified_Evidence | Evidência | Informação qualificada e rastreável |
| Validated_Theses | Tese | Hipótese que passou pelos gates definidos |
| Task_Backlog | Tarefa | Trabalho pendente |
| Work_In_Progress | Tarefa | Trabalho em execução |
| Completed_Artifacts | Artefato | Entrega concluída e validada |
| Risk_Exposure | UR (unidade de risco) | Exposição abstrata |
| Data_Quality_Debt | UDQ | Débito de qualidade/proveniência |
| Technical_Debt | UDT | Custo futuro de manutenção |

### 3.1 Regra de não fungibilidade

Não some diretamente UM + UC + PA + PRep. Se for necessário comparar alternativas, use uma função de avaliação multicritério externa ou um índice normalizado explicitamente ponderado. A simulação deve preservar os estoques separados.

---

## 4. Construção manual em módulos

Se o AI Agent gerar um diagrama incompleto, construa os módulos em sequência. Não tente desenhar tudo em uma única interação.

### Módulo A — Estoques de recursos e sobrevivência

Crie os Pools:
- Financial_Capital;
- Liquidity_Reserve;
- Time_Capacity;
- Attention_Capacity;
- Computational_Capacity;
- Knowledge_Capital;
- Relationship_Capital;
- Reputation_Capital;
- IP_Assets.

Adicione Sources para entradas exógenas e Drains para custos recorrentes. Conecte Financial_Capital a Liquidity_Reserve e Operating_Costs com regras explícitas de alocação.

**Teste:** sem entrada de caixa, a reserva deve cair quando custos são consumidos. Com reserva protegida, a operação deve durar mais, mas pode perder oportunidades que exigem investimento imediato.

### Módulo B — Informação, evidência e teses

Crie o fluxo:
Raw_Information → Qualified_Evidence → Thesis_Backlog → Validated_Theses.

Inclua filtros de qualidade, rejeição, atraso e retrabalho. Conecte a qualidade da evidência ao sucesso da validação. Inclua custo de pesquisa em tempo e computação.

**Teste:** aumentar a entrada de informação sem aumentar a capacidade de qualificação deve aumentar backlog, não necessariamente a produção de evidências.

### Módulo C — Orquestração de tarefas e agentes

Crie:
Task_Backlog → Planner → Worker_Capacity → Validation_Queue → Human_Approval → Completed_Artifacts.

Use Pools para filas e capacidade. O número de tarefas concluídas por Step deve ser limitado por recursos disponíveis. Falhas retornam parte do trabalho ao backlog e consomem capacidade adicional.

**Teste:** elevar a automação deve reduzir custo/tempo por tarefa até um ponto, mas sem validação suficiente pode elevar falhas e retrabalho.

### Módulo D — Oportunidades e financiamento

Crie um Gate para distribuir oportunidades entre grants, bounties, pilotos, serviços, SaaS/API, licenciamento, investimentos, pesquisa e rejeição/adiamento.

Cada caminho tem sua própria taxa de sucesso, atraso, custo, risco e captura de valor. Não use um único retorno médio para todos os canais.

**Teste:** grants podem ampliar runway sem gerar receita recorrente; pilotos podem gerar caixa e evidência de demanda; SaaS pode gerar recorrência, mas exige manutenção e aquisição de clientes.

### Módulo E — Captura de valor e reinvestimento

Conecte entregas aprovadas a pools distintos:
- Cash_Received;
- Customer_Evidence;
- Knowledge_Capital;
- Reputation_Capital;
- IP_Assets.

Apenas a parcela capturada como caixa alimenta Financial_Capital. Outros resultados alimentam pools próprios.

**Teste:** um projeto pode criar alto valor social/técnico e capturar pouco caixa. O modelo precisa tornar essa diferença visível.

### Módulo F — Risco, governança e aprendizagem

Conecte risco, qualidade, concentração, dívida técnica e sobrecarga aos fluxos de execução e alocação. Use State Connections para desativar ou reduzir caminhos quando os limites forem ultrapassados.

Crie o ciclo de post-mortem e retenção de aprendizagem.

**Teste:** um choque negativo deve reduzir capacidade ou caixa; a recuperação deve exigir tempo e recursos, não ocorrer instantaneamente.

---

## 5. Parâmetros iniciais para primeira execução

Use os valores abaixo apenas como **parâmetros sintéticos de teste**, sem relação com o patrimônio, renda, capacidade laboral ou produtividade real do usuário.

| Parâmetro | Baseline de demonstração | Faixa para sensibilidade |
|---|---:|---:|
| Caixa inicial | 1.000 UM | 500–2.000 |
| Reserva inicial | 300 UM | 100–700 |
| Custo operacional/Step | 35 UM | 20–70 |
| Capacidade de tarefas/Step | 10 | 4–20 |
| Atenção disponível/Step | 10 UA | 5–15 |
| Capacidade computacional/Step | 10 UComp | 5–20 |
| Taxa de qualificação de informação | 0,60 | 0,30–0,85 |
| Taxa de validação de teses | 0,35 | 0,10–0,60 |
| Taxa de aprovação de artefatos | 0,75 | 0,40–0,95 |
| Retrabalho inicial | 0,20 | 0,05–0,45 |
| Taxa de captura de valor em piloto | 0,40 | 0,10–0,70 |
| Taxa de conversão de serviço em recorrência | 0,15 | 0,00–0,40 |
| Taxa de reinvestimento | 0,30 | 0,10–0,60 |
| Fração de reserva protegida | 0,25 | 0,10–0,50 |
| Choque de custo | 0,00 | 0,00–0,50 |
| Taxa de retenção de aprendizagem | 0,60 | 0,20–0,90 |

As taxas são parâmetros ilustrativos. Não devem ser tratadas como estimativas empíricas. Ajuste-as somente após coletar dados operacionais ou resultados de experimentos.

### 5.1 Normalização

Se os Pools exigirem recursos inteiros, represente taxas como porcentagens em 100 unidades. Exemplo: 60% = 60/100. Para quantidades monetárias fracionárias, use centavos/unidades menores.

---

## 6. Cenários experimentais

Crie versões duplicadas do diagrama ou conjuntos de parâmetros salvos. Altere poucas variáveis por cenário para permitir atribuição causal aproximada.

### S0 — Baseline conservador
- entradas moderadas;
- reserva protegida;
- validação consistente;
- poucos projetos simultâneos;
- baixo crescimento de custos.

Pergunta: o sistema permanece operacional e produz ativos reutilizáveis?

### S1 — Abundância de oportunidades, escassez de atenção
- aumente Grant_Opportunities, Pilot_Opportunities e Service_Opportunities;
- mantenha Time_Capacity e Attention_Capacity fixos.

Pergunta: o gargalo migra para triagem, execução ou aprovação? O backlog cresce sem capturar mais valor?

### S2 — Automação sem validação proporcional
- aumente capacidade de workers e throughput;
- reduza custo por tarefa;
- mantenha validação baixa.

Pergunta: produtividade aparente aumenta enquanto falhas, dívida de dados e retrabalho corroem os ganhos?

### S3 — Validação intensiva
- aumente Red Team, testes e aprovação;
- aumente custo e tempo de revisão.

Pergunta: a redução de erros compensa o throughput menor? Em que nível o gate humano se torna gargalo?

### S4 — Grants sem receita recorrente
- aumente grants aprovados;
- mantenha baixa conversão para serviços, pilotos ou SaaS;
- introduza restrições de uso e atrasos de desembolso.

Pergunta: o sistema cresce em capacidade, mas permanece dependente de financiamento descontínuo?

### S5 — Piloto → serviço → SaaS
- priorize pilotos e serviços;
- permita conversão parcial em receita recorrente;
- aumente custo de suporte e infraestrutura com a base de clientes.

Pergunta: quando a recorrência cobre manutenção e custos fixos? O crescimento aumenta margem ou apenas complexidade?

### S6 — Choque de liquidez
- reduza entradas;
- aumente custos;
- introduza atraso em pagamentos;
- preserve a reserva mínima.

Pergunta: quais atividades devem ser pausadas primeiro? Quanto runway é necessário para evitar falha?

### S7 — Falha de provedor ou modelo
- reduza temporariamente Computational_Capacity;
- aumente falhas e latência;
- permita fallback para outro runtime com custo adicional.

Pergunta: a arquitetura agnóstica reduz dependência ou apenas aumenta custo de coordenação?

### S8 — Qualidade de informação
- compare baixa e alta taxa de qualificação;
- introduza dados desatualizados/conflitantes;
- aumente custo de proveniência.

Pergunta: qualidade de dados reduz retrabalho e decisões ruins o suficiente para justificar o custo?

### S9 — Dispersão de projetos
- aumente projetos ativos;
- eleve custo de troca de contexto;
- reduza atenção por projeto.

Pergunta: o crescimento do portfólio de projetos destrói throughput e conclusão?

### S10 — Concentração disciplinada
- limite projetos simultâneos;
- priorize reversibilidade, evidência e custo de oportunidade;
- mantenha uma reserva para oportunidades futuras.

Pergunta: menos iniciativas aumentam taxa de conclusão e sobrevivência?

### S11 — Aprendizagem acumulativa
- aumente retenção de conhecimento;
- reduza gradualmente o custo de tarefas repetidas;
- melhore a seleção de oportunidades com base em resultados anteriores.

Pergunta: o sistema desenvolve vantagem cumulativa ou a curva de aprendizagem satura?

### S12 — Cenário adversarial combinado
- baixa liquidez;
- dados ruins;
- falha de provedor;
- queda de oportunidades;
- aumento de custos;
- concentração de receita.

Pergunta: qual é a combinação mínima de reservas, modularidade e capacidade de corte que mantém o sistema recuperável?

---

## 7. Indicadores e Charts

Crie Charts para acompanhar, no mínimo:

### Sobrevivência
- Financial_Capital;
- Liquidity_Reserve;
- Runway_Buffer;
- Operating_Costs;
- Cash_Received por canal.

### Throughput e eficiência
- Task_Backlog;
- Work_In_Progress;
- Completed_Artifacts;
- Validation_Queue;
- taxa de retrabalho;
- tempo médio de ciclo.

### Inteligência
- Raw_Information;
- Qualified_Evidence;
- Validated_Theses;
- Data_Quality_Debt;
- Learning_Assets.

### Valor e sustentabilidade
- valor criado;
- valor capturado;
- receita recorrente;
- concentração de receita;
- ativos reutilizáveis;
- custo de manutenção.

### Risco e resiliência
- Risk_Exposure;
- Technical_Debt;
- dependência de provedor;
- reserva;
- falhas acumuladas;
- tempo de recuperação.

Não crie um único KPI composto como verdade universal. Se desejar um índice agregado, documente pesos, escalas, normalização e sensibilidade aos pesos.

---

## 8. Protocolo de execução no Machinations

1. Abra o site do Machinations e entre no workspace.
2. Crie um novo diagrama em branco.
3. Abra o AI Agent e cole o **Prompt Mestre** da seção 2.
4. Peça a geração inicial do diagrama com foco em estrutura e conexões, sem exigir todos os parâmetros de uma vez.
5. Inspecione os nós, nomes, unidades, fórmulas e conexões. Corrija duplicações e fluxos sem destino.
6. Se a geração estiver incompleta, construa os módulos A–F da seção 4, um por vez.
7. Configure os parâmetros iniciais da seção 5, sempre marcados como sintéticos.
8. Execute uma simulação simples em Play Mode para verificar a lógica de um ciclo.
9. Use Predictions/Monte Carlo para múltiplas execuções estocásticas, escolhendo número de Steps e de previsões conforme o plano/limite da conta.
10. Abra Charts e examine séries temporais e distribuições.
11. Faça os cenários S0–S12, alterando apenas um conjunto coerente de parâmetros por vez.
12. Exporte os resultados em CSV quando disponível e mantenha o nome do cenário, versão do diagrama, parâmetros e data junto do arquivo.
13. Registre resultados e limitações no repositório, sem substituir evidências reais por outputs simulados.
14. Revise as premissas após cada experimento; não ajuste parâmetros apenas para obter gráficos desejados.

### 8.1 Ordem recomendada

Primeiro: S0, S1, S2, S3 e S6.  
Depois: S4, S5, S7 e S8.  
Por último: S9, S10, S11 e S12.

Essa ordem testa primeiro a mecânica essencial, depois a estratégia de sustentabilidade e, por fim, a resiliência sistêmica.

### 8.2 Como usar o AI Balancer

Use o AI Balancer somente depois que o diagrama estiver estável e os parâmetros tiverem significado claro.

Exemplos de alvos:
- minimizar falhas mantendo throughput mínimo;
- maximizar runway sujeito a uma quantidade mínima de entregas;
- reduzir retrabalho sem ultrapassar limite de custo;
- atingir receita recorrente mínima sem exceder concentração de receita.

Não peça ao Balancer para maximizar “valor total” sem definir precisamente o que é valor, sua unidade, horizonte, restrições e custos. Otimização de uma métrica mal definida apenas produz uma resposta precisa para a pergunta errada.

---

## 9. Como interpretar os resultados

### 9.1 Padrões que merecem investigação

- **Backlog crescente + throughput estável:** capacidade insuficiente ou seleção fraca.
- **Mais automação + mais retrabalho:** qualidade de execução/validação não acompanhou o volume.
- **Caixa crescente + reserva baixa:** entradas existem, mas compromissos ou custos podem estar mal distribuídos.
- **Grants crescentes + receita recorrente baixa:** dependência de financiamento episódico.
- **Pilotos crescentes + baixa conversão:** falta de product-market fit, monetização ou capacidade de produto.
- **SaaS crescente + custos crescentes:** recorrência não garante margem.
- **Conhecimento crescente + pouca reutilização:** documentação sem integração ao workflow.
- **Reputação crescente + caixa estável:** valor criado não está sendo capturado pelo sistema.
- **Muitos projetos + poucas entregas:** custo de coordenação e troca de contexto.
- **Reserva alta + oportunidades perdidas:** proteção excessiva pode também ter custo de oportunidade.

Esses padrões são sinais para formular perguntas e buscar dados, não diagnósticos automáticos.

### 9.2 Três distinções indispensáveis

**Valor criado ≠ valor capturado.**  
Um projeto pode beneficiar usuários, comunidade ou ecossistema sem gerar caixa para quem o desenvolveu.

**Throughput ≠ qualidade.**  
Mais tarefas concluídas não significam melhores decisões, especialmente quando os critérios de validação são fracos.

**Resultado simulado ≠ resultado observado.**  
Uma simulação só demonstra as consequências das premissas codificadas no modelo.

---

## 10. Integração com os documentos do repositório

| Documento | Papel no modelo Machinations |
|---|---|
| `plano-upgrade-inteligencia-de-capital.md` | Define a ontologia de capital, oportunidades, risco e decisão |
| `plano-upgrade-ii-engenharia-de-sistemas-ia-quant-developer.md` | Define tarefas, agentes, contexto, harness, execução e avaliação |
| `meta-prompt-template-chain-inteligencia-de-capital.md` | Define a cadeia intenção → contrato → contexto → execução → validação → artefato |
| `teses-de-investimento.md` | Alimenta o pipeline de hipóteses, evidências e falsificadores |
| `postman-api-platform-blueprint.md` | Define os contratos de integração e os serviços que futuramente poderão fornecer dados reais |
| WebApp, scripts e Skills | Representam capacidades e custos operacionais a serem medidos futuramente |

### 10.1 Relação com Postman

Postman e Machinations têm funções complementares:

- **Postman:** contratos, chamadas de API, mocks, testes de integração, Flows e monitoração.
- **Machinations:** dinâmica de recursos, capacidade, filas, incentivos, cenários e feedbacks.

Um Mock Server não é uma fonte de dados empíricos. Um diagrama Machinations não é uma API. Uma execução de Flow não é uma simulação de economia. A integração futura pode exportar métricas reais da API para calibrar parâmetros, mas exige instrumentação e coleta apropriadas.

### 10.2 Ciclo de calibração futuro

\[
\text{Machinations Hypothesis}
\rightarrow \text{Operational Experiment}
\rightarrow \text{Observed Data}
\rightarrow \text{Parameter Calibration}
\rightarrow \text{New Simulation}
\]

Somente dados observados e adequadamente medidos devem substituir parâmetros sintéticos.

---

## 11. Metacrítica: riscos de modelagem

1. **Falsa precisão:** números decimais e gráficos não transformam premissas arbitrárias em fatos.
2. **Comensurabilidade indevida:** conhecimento, atenção, reputação e dinheiro não são unidades naturalmente intercambiáveis.
3. **Agentes fictícios:** representar agentes como pools não demonstra capacidade real de LLM ou autonomia.
4. **Correlação omitida:** falhas de modelos, provedores e fontes podem ocorrer simultaneamente.
5. **Endogeneidade:** mais reputação pode gerar oportunidades, mas oportunidades também podem gerar reputação; explicite o mecanismo e evite loops mágicos.
6. **Efeito Goodhart:** otimizar throughput, receita ou quantidade de teses pode degradar qualidade.
7. **Horizonte curto:** projetos com alto custo inicial e retorno tardio podem parecer ruins em poucos Steps.
8. **Aprendizagem gratuita:** conhecimento só se acumula se houver custo de revisão, documentação, retenção e reutilização.
9. **Risco de complexidade:** um diagrama grande demais pode ser impossível de calibrar ou interpretar.
10. **Otimização local:** o AI Balancer pode melhorar um KPI enquanto piora a resiliência global.

**Regra de parcimônia:** cada nó deve representar um estoque, fluxo, decisão ou condição que altere materialmente o comportamento do sistema. Se não alterar comportamento nem melhorar observabilidade, remova-o.

---

## 12. Critérios de conclusão do experimento

Considere a primeira versão concluída quando:

- [ ] O diagrama contém os nove subsistemas da seção 2L.
- [ ] As unidades estão documentadas e não são somadas indevidamente.
- [ ] O fluxo de informação e tese pode ser executado.
- [ ] O fluxo de tarefas e validação tem capacidade e retrabalho.
- [ ] O motor de oportunidades separa canais de financiamento e captura de valor.
- [ ] Reserva, custos e risco influenciam a continuidade operacional.
- [ ] Pelo menos um ciclo de aprendizagem está conectado.
- [ ] Os Charts exibem sobrevivência, throughput, qualidade e risco.
- [ ] Os cenários S0–S6 foram executados.
- [ ] Os resultados foram exportados ou registrados com parâmetros e versão.
- [ ] Limitações e hipóteses estão visíveis no diagrama.
- [ ] Nenhum resultado sintético foi apresentado como dado real ou recomendação financeira.

### Artefatos de saída recomendados

Salvar no repositório, após a execução:
- `experiments/machinations/README.md` — objetivo, versão e instruções;
- `experiments/machinations/parameter-register.csv` — parâmetros, unidade, fonte e status;
- `experiments/machinations/scenario-register.md` — descrição dos cenários;
- `experiments/machinations/results/<scenario>-<date>.csv` — exportações;
- `experiments/machinations/decision-log.md` — interpretações, limitações e decisões;
- imagem/exportação do diagrama, se permitida pela plataforma.

Não versionar credenciais, dados pessoais, informações privadas ou exports que contenham dados não autorizados.

---

## 13. Referências oficiais

- Machinations — What is Machinations? https://machinations.io/docs/what-is-machinations-systems-simulation-tool
- Documentation index: https://machinations.io/docs
- Framework Basics: https://machinations.io/docs/framework-basics
- Pools: https://machinations.io/docs/pools
- State Connections: https://machinations.io/docs/state-connections
- Best Practices: https://machinations.io/docs/best-practices
- FAQ: https://machinations.io/docs/faq

Consulte a documentação atual para detalhes de interface, limites de conta, opções de Predictions, AI Agent, Balancer e exportações. Recursos e limites podem variar com o plano e evoluir com o produto.

---

## 14. Síntese

O diagrama deve revelar a economia interna do próprio sistema: quais recursos entram, onde ficam retidos, onde são consumidos, quais transformações geram valor, quais resultados são capturados e como a aprendizagem altera o próximo ciclo.

\[
\boxed{
\text{Sustentabilidade}
\neq
\text{Crescimento a qualquer custo}
}
\]

\[
\boxed{
\text{Sustentabilidade}
=
\text{Valor Capturado}
+ \text{Ativos Reutilizáveis}
+ \text{Aprendizagem}
+ \text{Resiliência}
- \text{Custos}
- \text{Riscos Não Compensados}
}
\]

**Filosofema final:** *Um sistema inteligente não é aquele que maximiza a atividade; é aquele que preserva a capacidade de escolher, aprender e continuar criando valor quando suas premissas falham.*

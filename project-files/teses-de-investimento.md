# Catálogo de Teses de Investimento — João

> **Versão:** 1.0 · **Data:** 2026-10-30  
> **Integração:** `project-files/perfil-investidor-joao.md`  
> **Uso:** biblioteca de hipóteses para pesquisa, comparação, experimentação e alocação de capital.  
> **Natureza:** mapa de pesquisa; não é carteira, recomendação, previsão de mercado ou avaliação de suitability.

---

## 0. Instrução central ao Claude

Use este documento como um **universo de hipóteses**, não como uma lista de ativos a comprar. O objetivo é transformar ideias em teses causais, verificáveis, comparáveis e eventualmente financiáveis.

O perfil do investidor define preferências e restrições qualitativas; este catálogo organiza os domínios em que vale pesquisar. Nenhum dos dois documentos informa patrimônio, carteira atual, renda, reserva, horizonte financeiro, capacidade de aporte ou tolerância numérica a perdas.

### Regras de interpretação

1. Uma tese não é um fato. Uma narrativa plausível não é evidência de retorno.
2. Interesse do usuário não significa convicção, exposição, recomendação ou validação.
3. Não afirmar que um ativo está barato, caro, atrativo ou oportuno sem dados atuais, data-base e método explícito.
4. Não inferir pesos, preços-alvo, retornos esperados, limites de risco ou tamanho de posição.
5. Separar retorno financeiro, utilidade, aprendizado, impacto, reputação, governança e valor de opção.
6. Não confundir crescimento de mercado com captura de valor por uma empresa, protocolo, token ou investidor.
7. Toda tese deve ter argumento contrário, condições de invalidação e custo de oportunidade.
8. Tratar grants, bounties, doações, crowdfunding, receita, dívida, equity e tokens como instrumentos distintos.
9. Quando uma tese depender de regulação, tributação, dados de mercado ou condições correntes, pesquisar fontes primárias atualizadas.
10. Não transformar o catálogo em uma recomendação personalizada sem dados financeiros e suitability apropriados.

### Estados epistêmicos

Use estes rótulos em todas as atualizações:

- `INTERESSE_DECLARADO`: domínio ou tema mencionado pelo usuário.
- `HIPOTESE_DE_PESQUISA`: mecanismo plausível ainda não testado.
- `EVIDENCIA_PRELIMINAR`: indícios identificados, ainda insuficientes para conclusão.
- `TESE_EM_VALIDACAO`: hipótese com evidências, métricas e teste definido.
- `TESE_CORROBORADA`: evidência convergente, sujeita a revisão.
- `TESE_REFUTADA`: evidência ou mudança de condições contradiz o mecanismo.
- `EM_OBSERVACAO`: sem ação de alocação; manter monitoramento.
- `NAO_AVALIADA`: ainda não analisada.

**Estado inicial padrão de todas as teses abaixo:** `HIPOTESE_DE_PESQUISA`, salvo quando indicado como interesse declarado. A inclusão neste arquivo não comprova atratividade econômica.

---

## 1. Modelo de uma tese

Uma tese individual deve ser documentada com a seguinte ficha:

| Campo | Pergunta |
|---|---|
| ID / nome | Qual é a hipótese em uma frase? |
| Domínio | Macro, ações, crédito, cripto, software, impacto etc. |
| Mecanismo causal | Como a oportunidade produziria valor? |
| Fonte de retorno | Fluxo de caixa, juros, prêmio de risco, valorização, taxa, receita, aprendizado ou impacto? |
| Captura de valor | Quem captura o valor e por qual direito ou mecanismo? |
| Horizonte | Curto, médio ou longo; justificar sem inventar precisão. |
| Indicadores | Quais variáveis confirmariam ou enfraqueceriam a tese? |
| Catalisadores | O que poderia acelerar a materialização? |
| Riscos | O que pode causar perda, atraso ou não captura? |
| Invalidação | Que evidência faria abandonar ou reformular a tese? |
| Exposição possível | Instrumentos ou experimentos, sem recomendar posição. |
| Custo de oportunidade | Comparação com caixa, títulos públicos, alternativas e não agir. |
| Estado epistêmico | Um dos rótulos acima. |
| Próximo teste | Menor experimento capaz de reduzir incerteza. |
| Fontes | Documentos primários, dados, estudos e contrapontos. |

### Formalismo mínimo

Uma tese pode ser representada como:

**T = (M, E, C, R, H, F, X)**

Onde:
- **M** = mecanismo causal;
- **E** = evidência disponível;
- **C** = condições necessárias;
- **R** = riscos e cenários de falha;
- **H** = horizonte;
- **F** = forma de captura de valor;
- **X** = condição de falsificação.

A qualidade da tese não é a eloquência de sua narrativa. É a combinação de mecanismo inteligível, evidência rastreável, captura plausível e capacidade de sobreviver ao contraditório.

---

# PARTE I — TESES SOBRE MERCADOS E ALOCAÇÃO FINANCEIRA

## 2. Macro, regimes e reflexividade

### MAC-01 — Regimes macroeconômicos importam mais do que previsões pontuais
**Hipótese:** carteiras e estratégias podem se comportar de forma muito diferente conforme inflação, crescimento, juros reais, liquidez e condições de crédito.  
**Mecanismo:** mudanças de regime alteram taxas de desconto, custo de capital, margens, inadimplência e correlações.  
**Observar:** inflação corrente e implícita, juros reais, curva de juros, spreads de crédito, liquidez, revisões de lucro e condições financeiras.  
**Invalidar/revisar:** classificações de regime não melhoram decisões fora da amostra ou chegam tarde demais para serem úteis.  
**Risco:** transformar narrativa macro em tentativa de market timing.

### MAC-02 — Liquidez e condições financeiras podem dominar fundamentos no curto prazo
**Hipótese:** fluxos de crédito, liquidez e posicionamento podem explicar movimentos de preço que parecem desconectados dos fundamentos.  
**Observar:** condições de financiamento, spreads, fluxos, alavancagem, volatilidade e profundidade de mercado.  
**Contraponto:** liquidez não explica indefinidamente a geração de caixa nem elimina restrições de solvência.

### MAC-03 — Reflexividade: narrativas podem alterar os fundamentos que parecem apenas descrever
**Hipótese:** crenças sobre crescimento, tecnologia, solvência ou adoção podem modificar decisões de investimento, financiamento e consumo, reforçando ou revertendo a narrativa.  
**Mecanismo:** percepção → decisão → fluxo de capital → mudança operacional/preço → nova percepção.  
**Observar:** revisões de expectativas, captação, investimento, adoção, crédito e comportamento de agentes.  
**Contraponto:** nem toda narrativa se torna autorrealizável; restrições físicas, econômicas e institucionais permanecem.

### MAC-04 — A dispersão entre ativos e setores pode criar oportunidades relativas
**Hipótese:** mudanças de regime podem aumentar a diferença entre vencedores e perdedores, tornando seleção e análise relativa mais importantes que exposição indiscriminada ao mercado.  
**Observar:** dispersão de retornos, revisões de lucro, valuation relativo, qualidade e balanços.  
**Risco:** confundir dispersão com previsibilidade; custos e erro de seleção podem consumir o ganho.

### MAC-05 — A incerteza estrutural favorece decisões graduais e reversíveis
**Hipótese:** quando probabilidades são frágeis, escalonar compromissos e preservar liquidez pode ter valor superior a uma alocação integral baseada em previsão.  
**Observar:** valor da informação, volatilidade, liquidez, custo de esperar e irreversibilidade.  
**Contraponto:** esperar também tem custo; opcionalidade não é gratuita.

## 3. Ações, qualidade, valor e fatores

### EQ-01 — Qualidade econômica e alocação de capital podem explicar persistência de valor
**Hipótese:** empresas com vantagens competitivas duráveis, retornos elevados sobre capital e reinvestimento disciplinado podem compor valor ao longo do tempo.  
**Observar:** ROIC/ROE com ajustes, margens, conversão de caixa, reinvestimento, dívida, governança e diluição.  
**Invalidação:** deterioração persistente da vantagem competitiva, retornos abaixo do custo de capital ou alocação destrutiva.

### EQ-02 — Margem de segurança reduz dependência de previsões precisas
**Hipótese:** pagar preço suficientemente inferior a uma faixa conservadora de valor intrínseco pode reduzir a assimetria negativa.  
**Observar:** cenários de fluxo de caixa, ativos e passivos, qualidade contábil, normalização de ciclo e sensibilidade.  
**Risco:** value trap, balanço frágil, disrupção ou falsa precisão no valuation.

### EQ-03 — Fatores de investimento podem explicar exposições e prêmios sistemáticos
**Hipótese:** valor, qualidade, momentum, tamanho, baixa volatilidade e lucratividade podem ajudar a decompor retornos e riscos.  
**Observar:** definições fatoriais, robustez por mercado/período, turnover, custos, crowding e drawdowns.  
**Contraponto:** fatores podem passar longos períodos em baixa, sofrer arbitragem ou refletir riscos não reconhecidos.

### EQ-04 — Quantamental pode superar abordagens puramente narrativas ou puramente mecânicas em problemas complexos
**Hipótese:** combinar dados quantitativos, fundamentos e julgamento contextual pode melhorar seleção e controle de erros quando cada componente tem função clara.  
**Observar:** desempenho fora da amostra, contribuição incremental, calibração, consistência e custo operacional.  
**Invalidação:** o julgamento humano não acrescenta valor mensurável ou introduz vieses maiores que os benefícios.

### EQ-05 — Governança e incentivos são variáveis econômicas, não acessórios
**Hipótese:** qualidade de controlador, conselho, remuneração e disciplina de capital influencia a distribuição de valor entre acionistas e demais partes.  
**Observar:** transações com partes relacionadas, remuneração, diluição, dividendos, aquisições, dívida e transparência.  
**Risco:** inferir governança apenas por reputação ou comunicação corporativa.

### EQ-06 — Reinvestimento produtivo pode valer mais do que distribuição imediata
**Hipótese:** empresas com oportunidades de reinvestimento de alto retorno podem criar mais valor retendo capital do que distribuindo dividendos.  
**Observar:** retorno incremental sobre capital, runway de oportunidades, disciplina e preço pago por aquisições.  
**Contraponto:** retenção sem oportunidades ou governança adequada destrói valor.

### EQ-07 — Pequenas empresas podem oferecer crescimento, mas com fragilidade e custo de liquidez
**Hipótese:** empresas menores e menos acompanhadas podem conter ineficiências informacionais.  
**Observar:** liquidez, free float, governança, concentração de clientes, balanço, cobertura e qualidade dos dados.  
**Risco:** baixa liquidez, manipulação, spreads, sobrevivência e dificuldade de saída.

### EQ-08 — Ações cíclicas exigem normalização de resultados
**Hipótese:** lucros de pico podem fazer empresas parecerem baratas e lucros deprimidos podem fazê-las parecer caras.  
**Observar:** margens ao longo do ciclo, capacidade, estoques, preços de insumos, dívida e capex.  
**Invalidação:** mudança estrutural de tecnologia, demanda ou custos torna o histórico pouco representativo.

### EQ-09 — Buybacks só criam valor quando preço e incentivos são adequados
**Hipótese:** recompra abaixo do valor intrínseco pode aumentar valor por ação; recompra cara ou financiada por dívida pode destruí-lo.  
**Observar:** preço médio, valuation, origem dos recursos, remuneração em ações e evolução do número de ações.  
**Risco:** tratar recompra como sinal automático de qualidade.

### EQ-10 — A análise de short pode funcionar como teste adversarial de uma tese comprada
**Hipótese:** construir o melhor argumento de deterioração ajuda a detectar riscos que a narrativa otimista omite.  
**Observar:** fragilidade de caixa, contabilidade, concorrência, alavancagem, incentivos e valuation.  
**Restrição:** análise short é ferramenta de crítica; não implica recomendação de venda a descoberto ou uso de alavancagem.

## 4. Renda fixa, crédito e juros

### RF-01 — Renda fixa soberana pode funcionar como âncora de liquidez e referência de custo de oportunidade
**Hipótese:** títulos públicos adequados ao horizonte e à necessidade de liquidez podem oferecer previsibilidade contratual relativa e compor a estrutura de proteção.  
**Observar:** risco soberano, indexador, duration, marcação a mercado, liquidez, tributação e reinvestimento.  
**Risco:** confundir baixo risco de crédito com ausência de risco de preço ou de inflação.

### RF-02 — Duration é uma exposição explícita a juros e inflação esperada
**Hipótese:** títulos longos podem oferecer ganhos relevantes quando taxas caem, mas também perdas expressivas quando sobem.  
**Observar:** duration, convexidade, curva real/nominal e horizonte de passivo.  
**Contraponto:** acertar a direção dos juros é difícil; casar prazo com necessidade pode ser mais robusto que prever.

### RF-03 — Crédito privado remunera risco de inadimplência, liquidez e complexidade
**Hipótese:** spreads podem compensar riscos de crédito quando a análise do emissor, garantias e covenants é adequada.  
**Observar:** alavancagem, cobertura de juros, fluxo de caixa, vencimentos, garantias, subordinação, covenants e spreads.  
**Invalidação:** spread insuficiente frente à perda esperada, iliquidez ou baixa recuperabilidade.

### RF-04 — Estrutura de capital e covenants determinam recuperação em cenários de estresse
**Hipótese:** prioridade de garantias, documentação e restrições contratuais podem ser mais importantes que o yield nominal.  
**Observar:** waterfall, garantias, baskets, leakage, senioridade, intercreditor e capacidade de execução.  
**Risco:** documentos complexos, garantias sobreavaliadas e recuperação demorada.

### RF-05 — Inflação persistente favorece análise de ativos reais e indexadores, mas não garante proteção
**Hipótese:** alguns ativos e contratos podem repassar inflação ou preservar poder de compra em certos regimes.  
**Observar:** indexação, poder de preço, custos, duration, valuation e correlação em choques inflacionários.  
**Contraponto:** inflação pode elevar custos, juros e desconto mais rapidamente que receitas.

## 5. Diversificação internacional, moedas e geografia

### INT-01 — Diversificação geográfica reduz dependência de um único regime doméstico
**Hipótese:** exposição internacional pode diversificar riscos políticos, monetários, setoriais e de crescimento.  
**Observar:** concentração por país, moeda, setor, fator, tributação, custos e correlação em crises.  
**Risco:** diversificação aparente por ETF pode esconder concentração em poucas empresas.

### INT-02 — Moeda forte é diversificador possível, não hedge universal
**Hipótese:** exposição cambial pode proteger parte do poder de compra em certos cenários domésticos.  
**Observar:** passivos em moeda, horizonte, inflação relativa, juros, valuation cambial e correlação.  
**Invalidação:** a moeda não acompanha o risco que se pretende proteger ou a volatilidade prejudica o objetivo.

### INT-03 — Mercados emergentes combinam crescimento potencial e risco institucional
**Hipótese:** prêmio de risco pode compensar crescimento, demografia ou valuation em alguns mercados.  
**Observar:** governança, dívida externa, reservas, instituições, liquidez, moeda e estabilidade regulatória.  
**Risco:** desconto persistente por fragilidade institucional.

### INT-04 — Cadeias produtivas e geopolítica podem redistribuir lucros entre regiões e setores
**Hipótese:** nearshoring, friendshoring, segurança energética e soberania tecnológica podem deslocar capex e margens.  
**Observar:** investimento realizado, contratos, capacidade, custos, subsídios e produtividade.  
**Contraponto:** anúncios e intenções políticas não equivalem a lucros sustentáveis.

## 6. Commodities, energia e ativos reais

### COM-01 — Energia é infraestrutura estratégica e variável macroeconômica
**Hipótese:** oferta, demanda, armazenamento, redes e segurança energética criam oportunidades e riscos de longo prazo.  
**Observar:** capex, custo marginal, estoques, capacidade, regulação, demanda e curva futura.  
**Risco:** ciclos de excesso de oferta, intervenção política e substituição tecnológica.

### COM-02 — Transição energética cria vencedores e perdedores ao longo da cadeia
**Hipótese:** eletrificação, redes, armazenamento, eficiência e novos combustíveis podem deslocar valor entre produtores, fornecedores e usuários.  
**Observar:** custo nivelado, utilização, capex, gargalos de rede, subsídios e retorno sobre capital.  
**Contraponto:** crescimento de adoção pode coexistir com destruição de valor para investidores.

### COM-03 — Metais críticos têm valor estratégico, mas a tese depende de oferta e substituição
**Hipótese:** minerais relevantes para eletrificação e infraestrutura digital podem enfrentar gargalos de oferta.  
**Observar:** projetos, reservas, teor, custo, reciclagem, substitutos, concentração geográfica e contratos.  
**Risco:** ciclos de commodities, novas descobertas, substituição e excesso de capacidade.

### COM-04 — Ouro pode funcionar como diversificador em alguns regimes de confiança e juros reais
**Hipótese:** demanda por reserva de valor e características monetárias podem favorecer o ouro em determinados cenários.  
**Observar:** juros reais, dólar, compras de bancos centrais, fluxos, custos e comportamento em crises.  
**Contraponto:** não gera fluxo de caixa e pode sofrer longos períodos de baixo desempenho.

### COM-05 — Infraestrutura física pode oferecer fluxos vinculados a serviços essenciais
**Hipótese:** redes, logística, saneamento, energia e conectividade podem gerar receitas duráveis quando contratos e regulação são sólidos.  
**Observar:** concessões, demanda, capex de manutenção, dívida, reajustes, regulação e custo de capital.  
**Risco:** alavancagem, risco político e ativos encalhados.

---

# PARTE II — TESES SOBRE TECNOLOGIA, CRIPTO E NOVAS INFRAESTRUTURAS

## 7. IA, dados e infraestrutura computacional

### AI-01 — A camada de infraestrutura da IA pode capturar valor de forma diferente da camada de aplicações
**Hipótese:** chips, energia, data centers, redes, armazenamento e ferramentas de desenvolvimento podem capturar parte do valor da expansão de IA.  
**Observar:** utilização, margens, capex, concentração de fornecedores, custo por inferência e retorno incremental.  
**Risco:** sobreinvestimento, comoditização e obsolescência rápida.

### AI-02 — Aplicações verticais podem capturar valor ao integrar IA a workflows específicos
**Hipótese:** produtos que resolvem tarefas frequentes e custosas em setores específicos podem ter melhor retenção que interfaces genéricas.  
**Observar:** frequência de uso, economia de tempo, erro, integração, retenção, disposição a pagar e custo de servir.  
**Invalidação:** usuários não pagam, adoção é episódica ou o benefício é facilmente replicado.

### AI-03 — Dados proprietários, curadoria e proveniência podem ser ativos diferenciadores
**Hipótese:** dados contextualizados, atualizados, confiáveis e legalmente utilizáveis podem melhorar sistemas de IA e decisões.  
**Observar:** qualidade, cobertura, direitos, custo de atualização, exclusividade, uso e melhoria mensurável.  
**Risco:** dados sem direitos, sem demanda ou facilmente substituíveis.

### AI-04 — Avaliação, auditoria e observabilidade de sistemas de IA são mercados de confiança
**Hipótese:** empresas e instituições precisarão medir desempenho, segurança, rastreabilidade e conformidade de sistemas automatizados.  
**Observar:** orçamento, exigências regulatórias, incidentes, adoção, custo de auditoria e integração.  
**Contraponto:** ferramentas podem ser absorvidas por plataformas maiores ou virar commodity.

### AI-05 — Agentes de IA podem transformar interfaces em sistemas orientados a intenção
**Hipótese:** agentes capazes de interpretar objetivos e executar workflows podem reduzir fricção entre informação e ação.  
**Observar:** taxa de conclusão, supervisão humana, erros, custo, segurança, interoperabilidade e confiança.  
**Risco:** autonomia excessiva, falhas difíceis de detectar e responsabilidade mal definida.

### AI-06 — Oráculos e middleware podem monetizar confiabilidade entre sistemas
**Hipótese:** serviços que conectam dados, contexto, regras e execução entre plataformas podem ter valor quando a integração é crítica.  
**Observar:** disponibilidade, latência, precisão, proveniência, dependência, custo e willingness-to-pay.  
**Risco:** concentração de provedores e dificuldade de provar vantagem defensável.

### AI-07 — Eficiência computacional pode ser mais importante que escala bruta
**Hipótese:** modelos menores, especializados, quantizados ou executados localmente podem vencer em custo, privacidade e latência em tarefas específicas.  
**Observar:** custo por tarefa concluída, qualidade, energia, hardware, manutenção e experiência do usuário.  
**Contraponto:** modelos maiores podem manter vantagem em tarefas complexas e generalistas.

## 8. Software aberto, propriedade intelectual e micro-ventures

### OSS-01 — Open source pode funcionar como canal de distribuição e redução de custo de aquisição
**Hipótese:** software aberto útil pode atrair usuários, colaboradores, feedback e oportunidades comerciais.  
**Observar:** instalações, usuários ativos, issues, contribuições, conversão, suporte e custo de manutenção.  
**Risco:** popularidade sem captura de valor; dependência de trabalho não remunerado.

### OSS-02 — Serviços gerenciados podem monetizar software aberto
**Hipótese:** implantação, hospedagem, suporte, segurança e integração podem ser mais valiosos para clientes que o código isolado.  
**Observar:** demanda, margem de serviço, repetibilidade, churn e custo de suporte.  
**Invalidação:** clientes preferem operar internamente ou o custo de customização impede escala.

### OSS-03 — Micro-SaaS vertical pode oferecer validação econômica com capital inicial reduzido
**Hipótese:** resolver um problema estreito, recorrente e mensurável pode sustentar receita antes de uma plataforma ampla.  
**Observar:** entrevistas, pré-vendas, pilotos pagos, retenção, margem e tempo até valor.  
**Risco:** mercado pequeno, dependência de fundador e competição por preço.

### OSS-04 — Curadoria especializada pode ser vendida como serviço antes de virar software
**Hipótese:** transformar conhecimento disperso em síntese, triagem, comparação e decisão pode gerar valor para clientes com custo de busca elevado.  
**Observar:** tempo economizado, qualidade das decisões, recorrência, disposição a pagar e taxa de reutilização.  
**Risco:** serviço artesanal sem padronização ou escala.

### OSS-05 — APIs e licenciamento podem transformar artefatos intelectuais em fluxos recorrentes
**Hipótese:** ontologias, datasets, modelos, taxonomias e pipelines podem gerar receita quando resolvem uma dependência concreta.  
**Observar:** integração, chamadas, clientes, custo de manutenção, direitos e substituibilidade.  
**Risco:** IP difícil de proteger, adoção baixa ou licenciamento complexo.

### OSS-06 — Repositórios podem ser portfólios de opções, desde que exista foco e manutenção seletiva
**Hipótese:** um conjunto de protótipos pode preservar opções de produto, serviço, pesquisa e colaboração.  
**Observar:** dependências compartilhadas, testes, documentação, usuários, custos de manutenção e reutilização.  
**Invalidação:** custo cognitivo e operacional excede valor de opção; projetos sem uso devem ser arquivados.

### OSS-07 — Build in public pode gerar confiança e distribuição, mas não substitui demanda
**Hipótese:** demonstrar trabalho, evidências e evolução pode atrair colaboradores, clientes, grants e parceiros.  
**Observar:** conversas qualificadas, contribuições, conversão e oportunidades originadas.  
**Risco:** métricas de vaidade, exposição excessiva e incentivo a produzir conteúdo em vez de produto.

## 9. Criptoativos, DeFi e infraestrutura Web3

### WEB3-01 — Infraestrutura blockchain pode ter valor quando resolve coordenação, liquidação ou propriedade digital
**Hipótese:** redes distribuídas podem reduzir dependência de intermediários em aplicações específicas.  
**Observar:** usuários reais, transações úteis, custos, segurança, descentralização efetiva e alternativas centralizadas.  
**Risco:** complexidade sem benefício, baixa adoção e captura de valor por poucos participantes.

### WEB3-02 — Stablecoins podem ampliar utilidade de pagamentos e liquidação transfronteiriça
**Hipótese:** ativos estáveis podem reduzir fricção em transferências, tesouraria e acesso a dólares digitais.  
**Observar:** uso orgânico, spreads, reservas, resgates, risco de emissor, compliance e dependência de blockchain.  
**Risco:** depeg, congelamento, contraparte, regulação e risco operacional.

### WEB3-03 — Tokenização de ativos exige direitos e mecanismos claros
**Hipótese:** representação digital pode melhorar distribuição, registro, fracionamento ou liquidação de determinados direitos.  
**Observar:** titularidade jurídica, custódia, resgate, governança, mercado secundário, custos e proteção do investidor.  
**Invalidação:** token não confere direito executável ou a estrutura custa mais do que o benefício.

### WEB3-04 — DeFi pode oferecer infraestrutura financeira programável, mas acumula riscos compostos
**Hipótese:** protocolos podem automatizar empréstimos, negociação, liquidez e gestão de garantias.  
**Observar:** TVL ajustado, volume orgânico, receita, concentração, colateral, liquidações, auditorias e incidentes.  
**Risco:** smart contract, oracle, bridge, governança, liquidez, stablecoin e correlação sistêmica.

### WEB3-05 — Segurança e gestão de risco podem ser uma camada de valor crescente em DeFi
**Hipótese:** monitoramento, simulação, auditoria, limites e alertas podem reduzir perdas operacionais e de protocolo.  
**Observar:** incidentes evitados, falsos positivos, adoção, integração e willingness-to-pay.  
**Risco:** responsabilidade por falhas e dificuldade de demonstrar prevenção contrafactual.

### WEB3-06 — Infraestrutura de identidade, reputação e credenciais pode apoiar coordenação digital
**Hipótese:** credenciais verificáveis e reputação portátil podem reduzir custos de confiança em comunidades e mercados digitais.  
**Observar:** aceitação entre plataformas, resistência a Sybil, privacidade, contestabilidade e utilidade prática.  
**Risco:** vigilância, captura por plataformas e reputação injusta ou não portável.

### WEB3-07 — DAOs podem ser úteis em coordenação de recursos quando regras e incentivos são proporcionais
**Hipótese:** mecanismos transparentes de proposta, votação, tesouraria e prestação de contas podem apoiar comunidades distribuídas.  
**Observar:** participação efetiva, concentração de voto, execução, custos de governança e resultados.  
**Risco:** plutocracia, baixa participação, captura, burocracia e governança teatral.

### WEB3-08 — Mecanismos de financiamento retroativo podem recompensar contribuição demonstrada
**Hipótese:** financiar resultados após sua produção pode reduzir seleção adversa e direcionar capital a bens públicos úteis.  
**Observar:** critérios de avaliação, adicionalidade, concentração de avaliadores, manipulação e previsibilidade de financiamento.  
**Risco:** incerteza para contribuidores e subjetividade da avaliação.

### WEB3-09 — Bonding curves e mecanismos de mercado podem coordenar descoberta de valor
**Hipótese:** curvas de preço e emissão podem conectar demanda, financiamento e incentivos em comunidades ou projetos.  
**Observar:** profundidade, slippage, distribuição, manipulação, utilidade, emissão e sustentabilidade da tesouraria.  
**Risco:** reflexividade especulativa, corrida por liquidez e confusão entre preço e valor social.

### WEB3-10 — Farcaster e redes sociais abertas podem funcionar como laboratório de distribuição e coordenação
**Hipótese:** canais sociais composáveis podem facilitar descoberta, reputação, colaboração e circulação de ativos digitais.  
**Observar:** retenção, conversas qualificadas, conversão, distribuição, dependência de plataforma e custo de participação.  
**Risco:** atividade social não se converte em produto, receita ou impacto.

### WEB3-11 — DeSci pode financiar pesquisa e infraestrutura científica por mecanismos alternativos
**Hipótese:** comunidades, grants e ativos digitais podem ampliar financiamento, transparência e participação em ciência.  
**Observar:** qualidade científica, revisão por pares, reprodutibilidade, governança, financiamento e conflito de interesses.  
**Risco:** especulação sobre ciência, incentivos perversos e substituição de rigor por marketing.

### WEB3-12 — ReFi pode conectar capital a resultados regenerativos verificáveis
**Hipótese:** mecanismos financeiros e digitais podem direcionar recursos a restauração ecológica e bens comuns.  
**Observar:** adicionalidade, permanência, vazamento, MRV, governança local, direitos territoriais e receita sustentável.  
**Risco:** greenwashing, dupla contagem, métricas frágeis e financeirização sem benefício local.

## 10. Economia de tokens e desenho de incentivos

### TOK-01 — Token só é justificável quando a função econômica não pode ser atendida melhor por alternativa simples
**Hipótese:** token pode coordenar acesso, uso, contribuição ou governança em redes com participantes independentes.  
**Observar:** necessidade real, frequência de uso, direitos, demanda, custos, compliance e alternativas sem token.  
**Invalidação:** pontos, assinatura, contrato ou ledger simples resolvem o problema com menor risco.

### TOK-02 — Separar reputação, utilidade, governança e preço melhora legibilidade do sistema
**Hipótese:** ativos ou registros com funções distintas reduzem confusão de incentivos e conflitos.  
**Observar:** comportamento dos participantes, concentração, governança e entendimento dos direitos.  
**Risco:** fragmentação excessiva e custos de coordenação.

### TOK-03 — Microtarefas financiáveis podem converter trabalho aberto em entregáveis verificáveis
**Hipótese:** dividir projetos em unidades pequenas, auditáveis e negociáveis pode ampliar participação e financiamento granular.  
**Observar:** taxa de conclusão, qualidade, dependências, custo de revisão, tempo de entrega e demanda por cada tarefa.  
**Risco:** fragmentação do trabalho, oportunismo, baixa integração e mercado secundário inexistente.

### TOK-04 — Crowdfunding e mecenato podem financiar bens públicos e protótipos
**Hipótese:** comunidades podem financiar trabalho que não teria retorno privado imediato, desde que exista confiança e prestação de contas.  
**Observar:** recorrência, concentração de doadores, custo de captação, entregas e impacto.  
**Risco:** dependência de campanhas, fadiga de doadores e governança opaca.

### TOK-05 — Experiência, acesso e participação podem ser mais úteis que especulação com token
**Hipótese:** benefícios concretos, acesso a serviços, colaboração e reconhecimento podem sustentar utilidade sem depender de valorização secundária.  
**Observar:** uso, retenção, custo do benefício, satisfação e substitutos.  
**Risco:** utilidade artificial e passivo de benefícios maior que a receita.

---

# PARTE III — TESES SOBRE IMPACTO, CONHECIMENTO E CAPITAL AMPLIADO

## 11. Impacto, regeneração e economia real

### IMP-01 — Impacto mensurável pode revelar custos e benefícios ignorados pela contabilidade convencional
**Hipótese:** incorporar externalidades pode alterar decisões de investimento e avaliação de empresas.  
**Observar:** método de mensuração, materialidade, adicionalidade, atribuição e consistência dos dados.  
**Risco:** monetização arbitrária e comparabilidade ilusória.

### IMP-02 — Resultados verificáveis tendem a ser mais informativos que compromissos ESG genéricos
**Hipótese:** indicadores de resultado, auditoria e evidência física podem reduzir distância entre discurso e desempenho socioambiental.  
**Observar:** métricas de resultado, contrafactual, auditoria, escopo e incentivos.  
**Risco:** métricas fáceis de manipular ou deslocamento de impactos para fora do perímetro.

### IMP-03 — Restauração ecológica pode gerar valor econômico e social, mas depende de direitos e permanência
**Hipótese:** projetos de solo, água, biodiversidade e floresta podem produzir benefícios econômicos e públicos.  
**Observar:** linha de base, adicionalidade, permanência, MRV, direitos locais, custo e fonte de receita.  
**Risco:** incêndios, reversão, conflito fundiário e crédito ambiental sem integridade.

### IMP-04 — Infraestrutura regenerativa local pode combinar resiliência e eficiência
**Hipótese:** sistemas de energia, água, alimentos, construção e resíduos distribuídos podem reduzir vulnerabilidades locais.  
**Observar:** custo total, manutenção, confiabilidade, produtividade, externalidades e governança comunitária.  
**Risco:** economia unitária ruim, manutenção negligenciada e dependência de subsídios.

### IMP-05 — Financiamento de bens públicos precisa separar contribuição, atribuição e impacto
**Hipótese:** mecanismos de financiamento podem remunerar contribuições relevantes sem alegar causalidade indevida sobre resultados coletivos.  
**Observar:** outputs, outcomes, adicionalidade, contrafactual, distribuição e custos administrativos.  
**Risco:** atribuição excessiva e competição por métricas fáceis.

## 12. Conhecimento tácito, narrativas e economia da atenção

### KNO-01 — Conhecimento tácito pode ser fonte de vantagem quando convertido em procedimento sem perder contexto
**Hipótese:** experiência não documentada pode conter heurísticas úteis que, quando explicitadas e testadas, melhoram decisões.  
**Observar:** entrevistas, casos, consistência, transferibilidade, erro e resultados antes/depois.  
**Risco:** transformar intuição em regra sem validação.

### KNO-02 — Curadoria reduz custo de busca em ambientes de excesso informacional
**Hipótese:** seleção, contextualização e síntese podem valer mais que volume adicional de informação.  
**Observar:** tempo de busca, precisão, cobertura, confiança, adoção e disposição a pagar.  
**Risco:** curadoria enviesada, opaca ou facilmente substituível por ferramentas generalistas.

### KNO-03 — Proveniência e cadeia de evidências podem se tornar infraestrutura de confiança
**Hipótese:** decisões de maior consequência exigirão rastrear origem, transformação, data e qualidade das informações.  
**Observar:** adoção, auditabilidade, custo de integração, erros detectados e exigências institucionais.  
**Risco:** excesso de burocracia e rastreabilidade sem melhoria decisória.

### KNO-04 — Narrativas econômicas podem ser monitoradas como variáveis de mercado
**Hipótese:** mudanças de linguagem, enquadramento e atenção podem antecipar ou amplificar fluxos de capital.  
**Observar:** narrativas, revisões de estimativas, fluxos, posicionamento, adoção e divergência entre discurso e fundamentos.  
**Risco:** mineração de sentimento espúria, causalidade reversa e overfitting.

### KNO-05 — Informação pode ser transformada em ativo operacional por meio de compressão semântica
**Hipótese:** representar conhecimento em estruturas compactas e interoperáveis pode reduzir custo de decisão e facilitar recombinação.  
**Observar:** recuperação, precisão, reutilização, custo de atualização e impacto sobre decisões.  
**Risco:** compressão que elimina contexto, ambiguidade ou incerteza.

### KNO-06 — A atenção é um recurso escasso e sua alocação tem custo de oportunidade
**Hipótese:** sistemas que reduzem ruído e priorizam decisões relevantes podem aumentar produtividade e qualidade de vida.  
**Observar:** tempo poupado, interrupções, qualidade de decisão, fadiga e custo de manutenção.  
**Risco:** transformar produtividade em vigilância ou otimização sem finalidade.

## 13. Capital humano, aprendizagem e opções pessoais

### HUM-01 — Aprendizagem aplicada pode produzir retorno composto quando gera capacidades reutilizáveis
**Hipótese:** investir em competências que se combinam com ativos existentes pode ampliar oportunidades futuras.  
**Observar:** projetos concluídos, transferibilidade, tempo até proficiência, aplicação e demanda externa.  
**Risco:** acumular cursos e conceitos sem aplicação.

### HUM-02 — Portfólio de capacidades pode ser mais resiliente que dependência de uma única fonte de renda
**Hipótese:** combinar competências técnicas, pesquisa, produto e relacionamento pode criar múltiplos caminhos de geração de valor.  
**Observar:** receita por fonte, concentração, tempo de manutenção e conversão de capacidade em demanda.  
**Risco:** dispersão, excesso de context switching e renda não recorrente.

### HUM-03 — Autonomia operacional é um ativo, mas deve ser avaliada por custo total
**Hipótese:** ferramentas, automações e processos próprios podem reduzir dependências e aumentar controle.  
**Observar:** custo de manutenção, confiabilidade, portabilidade, tempo economizado e custo de oportunidade.  
**Risco:** construir infraestrutura própria quando comprar ou não fazer seria melhor.

### HUM-04 — Reputação demonstrada pode reduzir custo de confiança e facilitar acesso a oportunidades
**Hipótese:** histórico público de entregas verificáveis pode facilitar colaboração, contratação e financiamento.  
**Observar:** referências, convites, conversão em trabalho, recorrência e qualidade das relações.  
**Risco:** confundir visibilidade com reputação ou reputação com receita.

### HUM-05 — Experimentos pequenos podem ter valor de opção superior a planos extensos não testados
**Hipótese:** protótipos e pilotos baratos podem revelar demanda, restrições e caminhos de execução antes de compromissos maiores.  
**Observar:** custo por aprendizado, tempo até feedback, taxa de conversão e decisões alteradas.  
**Risco:** experimentar indefinidamente sem consolidar o aprendizado.

---

# PARTE IV — TESES TRANSVERSAIS E MÉTODOS DE ALOCAÇÃO

## 14. Estratégias de portfólio e desenho de decisões

### PM-01 — Diversificação deve considerar fatores, dependências e fontes de liquidez
**Hipótese:** contar ativos não mede diversificação; exposições comuns podem concentrar risco oculto.  
**Observar:** look-through, fatores, moedas, emissores, correlações condicionais, liquidez e contraparte.  
**Risco:** modelos de correlação baseados em períodos tranquilos.

### PM-02 — Liquidez possui valor econômico mesmo quando seu retorno nominal parece inferior
**Hipótese:** caixa e ativos líquidos preservam capacidade de agir, cobrir obrigações e aproveitar oportunidades.  
**Observar:** custo de carregamento, necessidade de caixa, volatilidade, custo de venda forçada e oportunidades.  
**Risco:** excesso de caixa por medo ou tentativa de prever o momento ideal.

### PM-03 — Rebalanceamento por aportes pode reduzir giro e fricção
**Hipótese:** quando há novos recursos, direcioná-los a exposições subalocadas pode reduzir vendas e custos.  
**Observar:** desvios de alocação, custos, impostos, liquidez e risco total.  
**Risco:** manter concentração excessiva por evitar realização de perdas.

### PM-04 — Gestão por cenários pode ser mais robusta que um único preço-alvo
**Hipótese:** cenários base, otimista, adverso e de ruptura explicitam dependências e assimetrias.  
**Observar:** premissas, probabilidades quando justificáveis, sensibilidades e sinais de mudança.  
**Risco:** cenários decorativos com probabilidades inventadas.

### PM-05 — A carteira pode incluir orçamento de experimentação separado do capital de preservação
**Hipótese:** separar capital essencial de capital experimental reduz contágio de perdas e permite aprender com limites claros.  
**Observar:** orçamento, perda máxima autorizada, objetivo de aprendizado, liquidez e governança da decisão.  
**Risco:** o compartimento experimental crescer sem validação ou limites.

### PM-06 — O custo de complexidade deve entrar no retorno líquido
**Hipótese:** estruturas com mais intermediários, obrigações, manutenção e risco operacional precisam oferecer benefício proporcional.  
**Observar:** custos financeiros, fiscais, legais, cognitivos, técnicos e de coordenação.  
**Risco:** ignorar custos invisíveis ou subestimar manutenção.

### PM-07 — Uma tese precisa competir contra a alternativa de não agir
**Hipótese:** não investir pode ser a decisão superior quando evidência, preço, liquidez ou adequação são insuficientes.  
**Observar:** custo de espera, perda de oportunidade, preservação de liquidez e evolução da evidência.  
**Risco:** inércia disfarçada de prudência.

### PM-08 — A alocação deve ser revista quando o mecanismo muda, não apenas quando o preço muda
**Hipótese:** monitorar variáveis causais pode antecipar deterioração ou fortalecimento da tese.  
**Observar:** indicadores operacionais, incentivos, concorrência, regulação e estrutura de capital.  
**Risco:** apego à tese e revisão tardia.

### PM-09 — Decisões devem ser auditáveis para melhorar o processo, não para racionalizar o passado
**Hipótese:** registrar premissas, evidências e resultados permite aprender sobre calibração e vieses.  
**Observar:** previsão versus resultado, qualidade das fontes, mudanças de tese e custo de erro.  
**Risco:** hindsight bias, registros seletivos e métricas que premiam sorte.

### PM-10 — Convexidade e antifragilidade precisam ser demonstradas na estrutura de payoff
**Hipótese:** algumas estratégias se beneficiam de variabilidade ou têm perdas limitadas e ganhos assimétricos.  
**Observar:** payoff, custos, dependência de trajetória, liquidez, cauda e risco de ruína.  
**Risco:** chamar volatilidade de oportunidade ou assimetria sem calcular a perda.

## 15. Tese-síntese: ecossistema de capital regenerativo

### SYN-01 — Um ecossistema de ativos financeiros, intelectuais e computacionais pode ampliar a capacidade de gerar valor
**Hipótese:** pesquisa, software, curadoria, relações e produtos podem se reforçar, criando opções de receita, financiamento, aprendizado e impacto.  
**Mecanismo proposto:** informação → conhecimento estruturado → ferramenta/serviço → uso → evidência → receita ou financiamento → reinvestimento seletivo.  
**Observar:** usuários, entregas, receita, custo de manutenção, reutilização, parcerias e resultados verificáveis.  
**Risco:** ecossistema conceitualmente integrado, mas sem comprador, usuário ou unidade econômica clara.  
**Condição de invalidação:** após testes proporcionais, não existe demanda recorrente nem benefício mensurável que justifique manutenção.

### SYN-02 — ValueCurator / Compilatorum como laboratório de construção de opções
**Hipótese:** repositórios, curadoria, agentes, oráculos, ontologias e microserviços podem formar uma base reutilizável para serviços e produtos.  
**Status:** linha de experimentação do usuário; não presumir tração, receita, valuation ou demanda comprovada.  
**Testes:** selecionar um problema estreito, identificar usuário e comprador, entregar manualmente, medir resultado, cobrar por piloto e automatizar somente após repetição.  
**Risco:** amplitude excessiva, custo de integração, manutenção e ausência de foco comercial.

---

# PARTE V — PRIORIZAÇÃO E PROTOCOLO DE PESQUISA

## 16. Priorização inicial por aderência temática

A tabela abaixo expressa **aderência às conversas e potencial de pesquisa**, não expectativa de retorno nem recomendação de alocação.

| Cluster | Aderência temática | Próximo passo racional |
|---|---:|---|
| Quantamental, qualidade, fatores e valuation | Alta | Criar metodologia de pesquisa e comparação de ativos |
| Liquidez, juros reais e risco de ruína | Alta | Definir dados financeiros pessoais antes de qualquer sizing |
| IA, dados, curadoria e oráculos | Alta | Escolher um caso de uso e medir economia para um usuário |
| Open source, micro-SaaS e IP | Alta | Testar serviço manual/piloto pago antes de ampliar software |
| ReFi, impacto e bens públicos | Alta | Definir métrica de resultado, adicionalidade e pagador |
| Web3, DAOs e token design | Alta como pesquisa | Simular mecanismos e validar utilidade sem token negociável |
| Narrativas, reflexividade e comportamento | Alta | Criar observatório de hipóteses com sinais e falsificadores |
| Commodities e transição energética | Média/alta | Estudar cadeia de valor, ciclos e exposição indireta |
| Crédito privado e estruturas complexas | Média | Estudar documentação, risco de recuperação e liquidez |
| Angel investing e participações ilíquidas | Interesse conceitual | Não presumir capital, acesso ou adequação |

## 17. Matriz de triagem — pontuar sem falsa precisão

Use notas de 1 a 5 apenas como julgamento estruturado, com justificativa textual. Não some automaticamente os itens como se fossem probabilidades ou retornos.

| Critério | Pergunta |
|---|---|
| Clareza causal | O mecanismo é compreensível e plausível? |
| Qualidade da evidência | Há dados primários e evidência independente? |
| Captura de valor | Está claro quem recebe o benefício econômico? |
| Assimetria | A perda pode ser limitada em relação ao ganho potencial? |
| Reversibilidade | É possível testar em escala pequena? |
| Liquidez | Há saída ou alternativa de liquidez realista? |
| Robustez | A tese sobrevive a cenários adversos? |
| Diferenciação | Existe vantagem informacional, operacional ou de execução? |
| Custo total | Custos técnicos, fiscais, jurídicos e cognitivos são proporcionais? |
| Adequação | A tese respeita objetivos, horizonte e restrições confirmadas? |
| Impacto | Há resultado verificável e adicionalidade, quando relevante? |
| Aprendizado | O teste gera conhecimento reutilizável? |

**Regra:** critérios críticos desconhecidos permanecem como desconhecidos; não preencher lacunas com notas neutras.

## 18. Protocolo de pesquisa e decisão

1. **Descoberta:** registrar a hipótese e sua origem.
2. **Definição:** escrever o mecanismo causal em linguagem simples.
3. **Evidência:** buscar documentos primários, dados e fontes independentes.
4. **Steelman:** formular a versão mais forte do argumento favorável.
5. **Red team:** formular a versão mais forte do argumento contrário.
6. **Modelo:** explicitar premissas, cenários, sensibilidades e limites.
7. **Captura:** identificar quem paga, quem recebe e quais direitos existem.
8. **Risco:** mapear perda permanente, liquidez, dependências e cauda.
9. **Experimento:** desenhar o menor teste informativo e reversível.
10. **Decisão:** pesquisar mais, testar, alocar, acompanhar, pausar ou rejeitar.
11. **Auditoria:** comparar premissas com resultados e atualizar o estado epistêmico.

### Hierarquia recomendada de fontes

1. **Primárias:** demonstrações financeiras, documentos regulatórios, prospectos, contratos, dados oficiais, código, documentação técnica, governança e relatórios auditados.
2. **Independentes:** estudos acadêmicos, pesquisas setoriais, provedores de dados com metodologia explícita e jornalismo de apuração.
3. **Interpretativas:** cartas de gestores, análises, podcasts, redes sociais, fóruns e narrativas de mercado.

Fontes promocionais podem gerar hipóteses, mas não devem validar sozinhas uma tese. Registrar data de acesso, período dos dados, limitações e conflitos de interesse.

## 19. Painel de acompanhamento

Manter uma tabela viva com estes campos:

| ID | Tese | Estado | Evidência mais forte | Principal risco | Próximo gatilho | Última revisão |
|---|---|---|---|---|---|---|
| MAC-03 | Reflexividade | HIPOTESE_DE_PESQUISA | A preencher | Narrativa sem causalidade | A definir | A definir |
| EQ-01 | Qualidade econômica | HIPOTESE_DE_PESQUISA | A preencher | Deterioração competitiva | A definir | A definir |
| RF-03 | Crédito privado | HIPOTESE_DE_PESQUISA | A preencher | Default/ilíquidez | A definir | A definir |
| AI-02 | IA vertical | HIPOTESE_DE_PESQUISA | A preencher | Ausência de disposição a pagar | A definir | A definir |
| OSS-04 | Curadoria como serviço | HIPOTESE_DE_PESQUISA | A preencher | Serviço não escalável | A definir | A definir |
| WEB3-07 | DAOs | HIPOTESE_DE_PESQUISA | A preencher | Captura de governança | A definir | A definir |
| IMP-03 | Restauração ecológica | HIPOTESE_DE_PESQUISA | A preencher | Baixa adicionalidade | A definir | A definir |
| SYN-01 | Ecossistema regenerativo | HIPOTESE_DE_PESQUISA | A preencher | Integração sem demanda | A definir | A definir |

O painel é uma amostra inicial; criar linhas para todas as teses à medida que forem efetivamente pesquisadas.

## 20. Regras de segurança intelectual e financeira

- Não recomendar alavancagem, derivativos ou ativos ilíquidos sem análise específica de risco e adequação.
- Não apresentar tokens, NFTs, pontos, reputação ou métricas sociais como equivalentes a dinheiro.
- Não presumir que uma grant é receita recorrente ou que um grant retroativo será concedido.
- Não confundir TVL com receita, usuários cadastrados com usuários ativos, volume incentivado com demanda orgânica ou valuation com liquidez.
- Não inferir que crescimento de uma tecnologia produz retorno para qualquer ativo associado a ela.
- Não usar backtests sem custos, survivorship bias, look-ahead bias, dados fora de amostra e documentação.
- Não usar correlações históricas como garantia de hedge futuro.
- Não tratar impacto declarado como impacto adicional.
- Não preencher dados pessoais ou financeiros ausentes com exemplos do perfil demonstrativo de Rafael.
- Para ativos regulados no Brasil, verificar regras e documentos vigentes e distinguir educação, análise e recomendação individual.

---

## 21. Integração com o repositório

Este arquivo deve funcionar como biblioteca de hipóteses, conectado às demais memórias:

- `project-files/perfil-investidor-joao.md` — preferências, filosofia, estilo e regras de interação.
- `project-files/teses-de-investimento.md` — universo de hipóteses e mecanismos.
- `project-files/situacao-financeira.md` — situação financeira, somente quando fornecida pelo usuário.
- `project-files/carteira-atual.md` — posições e exposições, somente com dados atuais fornecidos/importados.
- `project-files/restricoes-e-suitability.md` — objetivos, horizonte, liquidez, limites e adequação confirmados.
- `project-files/fontes.md` — hierarquia e registro de fontes.
- `project-files/diario-de-decisoes.md` — decisões, premissas, resultados e revisões.
- `project-files/experimentos.md` — pilotos, microtarefas, grants, serviços e produtos em validação.

### Instrução para o Claude

Ao receber uma nova oportunidade:
1. procurar teses relacionadas por ID e mecanismo;
2. verificar se a hipótese já foi refutada ou revisada;
3. separar fatos, inferências e narrativas;
4. atualizar apenas o que a nova evidência sustenta;
5. registrar fontes e data;
6. explicitar o que ainda não se sabe;
7. sugerir um teste proporcional antes de comprometer capital;
8. não converter automaticamente uma tese de negócio em tese de investimento financeiro.

### Filosofema operacional

**Capital é capacidade de agir no futuro. Investir é escolher quais possibilidades merecem recursos hoje — sem destruir, por excesso de convicção, as possibilidades de amanhã.**

**Tese sem falsificador é crença; modelo sem proveniência é decoração; retorno sem risco é propaganda; opcionalidade sem teste é imaginação.**

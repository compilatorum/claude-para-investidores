# fontes.md — Hierarquia de Fontes e Regras de Busca da Carteira

> **Regra de Precedência Absoluta:**
> $$\text{Camada 1 (Fato Primário CVM/B3/BCB/RI)} \;\succ\; \text{Camada 2 (Notícia de Apuração Primária)} \;\succ\; \text{Camada 3 (Opinião Identificada)}$$
> Notícia sem documento primário correspondente na Camada 1 deve ser classificada como **"A confirmar no RI/CVM"**.

---

## 🏛️ Camada 1 — Fato Primário (Documentos Regulatórios e Dados Oficiais)
*Sempre buscar primeiro nesta camada. É a única fonte aceita como prova factual e para citação em relatórios (conforme Ofício APIMEC Brasil nº 002/2025 e Resolução CVM nº 20/2021).*

### 1.1 Órgãos Reguladores, Bolsas e Bancos Centrais
- **CVM (Comissão de Valores Mobiliários):** Sistema Empresas.NET / RAD CVM (`rad.cvm.gov.br`, `dados.cvm.gov.br`) — ITR, DFP, Formulário de Referência (FRE), Fatos Relevantes, Comunicados ao Mercado e Formulário CVM 358 (negociações de insiders/controladores).
- **B3 (Brasil, Bolsa, Balcão):** `b3.com.br` — Composição oficial do Ibovespa (`BOVA11`), proventos creditados, eventos corporativos e boletins diários.
- **Banco Central do Brasil (BCB):** `bcb.gov.br` — Atas e Comunicados do Copom, Relatório de Inflação, Sistema Gerenciador de Séries Temporais (SGS: Selic `432`, CDI `4389`, PTAX `1`, IPCA `433`) e Boletim Focus (`olinda.bcb.gov.br`).
- **IBGE:** `ibge.gov.br` / SIDRA — IPCA, IPCA-15, PIB Contas Nacionais, PMC e PIM-PF.
- **SEC (EUA — para `IVVB11` / S&P 500):** `sec.gov/edgar` (10-K, 10-Q, 8-K) e **Federal Reserve (Fed):** `federalreserve.gov` (FOMC Statements, Dot Plot, Beige Book).

### 1.2 Mapa de RI e Códigos CVM das 8 Empresas da Carteira (+ 2 ETFs)
| Ticker | Empresa / Emissor | Código CVM | CNPJ | Portal Oficial de Relações com Investidores (RI) |
| :--- | :--- | :---: | :--- | :--- |
| **`VALE3`** | Vale S.A. | `4170` | `33.592.510/0001-54` | `vale.com/pt/investidores` |
| **`ITUB4`** | Itaú Unibanco Holding S.A. | `19348` | `60.872.504/0001-23` | `itau.com.br/relacoes-com-investidores` |
| **`PETR4`** | Petróleo Brasileiro S.A. — Petrobras | `9512` | `33.000.167/0001-01` | `investidorpetrobras.com.br` |
| **`WEGE3`** | WEG S.A. | `5410` | `84.429.695/0001-11` | `ri.weg.net` |
| **`PRIO3`** | PRIO S.A. (PetroRio) | `22187` | `10.629.105/0001-68` | `ri.prio3.com.br` |
| **`BBAS3`** | Banco do Brasil S.A. | `1023` | `00.000.000/0001-91` | `ri.bb.com.br` |
| **`RENT3`** | Localiza Rent a Car S.A. | `19739` | `16.670.085/0001-55` | `ri.localiza.com` |
| **`RADL3`** | Raia Drogasil S.A. (RD Saúde) | `5258` | `61.585.865/0001-51` | `ri.rdsaude.com.br` |
| **`BOVA11`** | iShares Ibovespa Fundo de Índice (BlackRock) | — | `10.406.511/0001-61` | `blackrock.com/br/produtos/251816/ishares-ibovespa-fundo-de-indice` |
| **`IVVB11`** | iShares S&P 500 Fundo de Índice (BlackRock) | — | `19.909.560/0001-91` | `blackrock.com/br/produtos/251902/ishares-sp-500-fundo-de-indice-inv-no-exterior` |

---

## 📰 Camada 2 — Notícia de Apuração Primária (Jornalismo Econômico)
*Usada para detectar eventos nas últimas horas/dias, mas exige cruzamento obrigatório com a Camada 1.*

- **Brasil (Macroeconomia, Empresas e Regulação):**
  - *Valor Econômico* (`valor.globo.com`)
  - *Broadcast / Estadão E-Investidor* (`broadcast.com.br`)
  - *Brazil Journal* (`braziljournal.com`)
  - *NeoFeed* (`neofeed.com.br`)
- **Internacional (Commodities, Juros Globais, China e S&P 500):**
  - *Reuters* (`reuters.com`)
  - *Bloomberg* (`bloomberg.com`)
  - *Financial Times* (`ft.com`)
  - *The Wall Street Journal* (`wsj.com`)

---

## 💬 Camada 3 — Opinião Identificada (Tese, Contraste e *Red Team*)
*Nunca tratar como fato. Sempre rotular explicitamente o autor/casa e o potencial conflito de interesse.*

- **Cartas de Gestores Independentes:** Verde Asset, SPX Capital, Adam Capital, Dynamo, Atmos Capital, Squadra Investimentos, Alaska, Guepardo, Kinea.
- ** Análises Independentes e Podcasts Especializados:** Market Makers (`mmakers.com.br`), relatórios de *sell-side* (apenas quando confrontados com os números primários da CVM).
- **Fontes Proibidas (Ruído Puro):** Fóruns anônimos, threads de redes sociais sem link para documento CVM, vídeos com manchetes caça-clique ("oportunidade urgente", "ação vai dobrar"), rumores de M&A sem comunicado ao mercado.

---

## 🧭 Matriz de Fatores de Risco da Carteira × Fontes Primárias Obrigatórias

| Fator de Risco da Carteira | Ativos Sensíveis na Carteira | Fonte Primária Obrigatória (Camada 1) | Indicador-Chave a Monitorar |
| :--- | :--- | :--- | :--- |
| **1. Juros Domésticos (Selic / Curva DI / NTN-B)** | `RENT3`, `RADL3`, `ITUB4`, `BBAS3`, `BOVA11` | BCB (Copom / Focus) e Tesouro Direto / ANBIMA | Taxa Selic Meta, DI Futuro Jan/27–Jan/29 e Juro Real NTN-B |
| **2. Minério de Ferro & Demanda Chinesa** | `VALE3` (15,3%) + `BOVA11` (*look-through*) | RI da Vale (Relatório de Produção e Vendas), Dalian/Singapore Iron Ore (`62% Fe`) e NBS China | Preço realizado de finos/pelotas (US$/t), prêmio de qualidade e C1 Cash Cost |
| **3. Petróleo Brent, Capex & Governança Estatal** | `PETR4` (11,3%), `PRIO3` (7,2%) + `BOVA11` | ANP (Boletim da Produção de Petróleo e Gás), EIA/OPEC, RI Petrobras e RI PRIO | Brent (US$/bbl), *lifting cost* (US$/boe), produção diária por campo (Wahoo/Albacora/Búzios) e Fatos Relevantes de dividendos/Capex |
| **4. Crédito, Inadimplência & Agronegócio** | `ITUB4` (13,5%), `BBAS3` (7,0%) + `BOVA11` | BCB (Estatísticas Monetárias e de Crédito / IF.data) e Demonstrações Cosif/IFRS dos Bancos | NPL > 90 dias (PF, PME e Agro), Custo do Crédito, NIM (Margem Financeira com Clientes) e ROE |
| **5. Câmbio (USD/BRL), Capex Industrial Global & S&P 500** | `WEGE3` (9,8%), `IVVB11` (4,0%), Exportadoras | BCB (PTAX), BEA/Fed (EUA), S&P Dow Jones Indices e RI WEG | Receita Mercado Externo da WEG, carteira de pedidos T&D (EUA/Europa) e múltiplos do S&P 500 |

---

## 🛡️ As 5 Regras de Ouro de Uso do `fontes.md`
1. **Hierarquia Estrita:** Fato regulatório (CVM/BCB/RI) vence qualquer manchete de jornal.
2. **Proibição de Rumor:** Rumor de mercado ("fontes próximas disseram") sem Fato Relevante ou Questionamento da CVM/B3 não gera recomendação de giro na carteira.
3. **Citação Obrigatória de Página e Data:** Todo número extraído de ITR, DFP ou Release deve vir acompanhado de `[Documento, Data, Página X]`.
4. **Conferência de Link em Buscadores de IA:** Ao usar buscadores (Perplexity, Gemini ou Web Search), abrir e verificar o link original antes de aceitar a informação (devido à taxa de 30%–37% de erro de atribuição de fonte documentada pela Columbia/EBU).
5. **Vedação Regulatória (APIMEC 002/2025 & CVM 20/2021):** A IA jamais é fonte. A fonte é sempre o documento público primário auditável.

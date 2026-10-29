# 🏛️ Claude para Investidores & O Arsenal de IA do Mercado Financeiro (v1.0 & v2.0)

> **Engenharia Reversa, Re-Engenharia Simbólica e Implementação Completa (WebApp 17 Abas + Scripts Python + Skills Financeiras + Artefatos de Projeto)**
> Baseado na obra de **Leonardo Dawadji** e **Market Makers Academy**:
> 1. 🎥 **Masterclass (v1.0):** [`https://www.youtube.com/watch?v=zNVHixsE1ik`](https://www.youtube.com/watch?v=zNVHixsE1ik) (*"Claude para Investidores: aprenda a usar IA para turbinar sua carteira de investimentos"*)
> 2. 🎓 **Formação Completa CPI02 (v2.0):** [`https://store.mmakers.com.br/claude-investidores-cpi02-b`](https://store.mmakers.com.br/claude-investidores-cpi02-b) (14 Módulos: `Módulos 0 a 11` + `Bônus I: Valuation com IA` + `Bônus II: Gestão de Portfólio`)
> 3. 📘 **Guia Técnico (v2.0):** [`docs/O-Arsenal-de-IA-do-Mercado-Financeiro-v2.pdf`](./docs/O-Arsenal-de-IA-do-Mercado-Financeiro-v2.pdf) (*"O Arsenal de IA do Mercado Financeiro — As ferramentas, onde cada uma funciona e os prompts para começar"*)

---

## 📂 Estrutura Completa do Repositório Implementado

| Caminho / Artefato | Tipo | Descrição Técnica |
| :--- | :---: | :--- |
| **[`index.html`](./index.html)** | 🖥️ **WebApp Interativo** | Sistema WebApp completo autocontido com **seletor de modo v1.0 (9 abas da Masterclass) e v2.0 (17 abas unificadas)**, construtor interativo do Prompt de 6 Partes, gráficos SVG e cópia de todos os prompts com 1 clique. |
| **[`ENGENHARIA_REVERSA_V1_MASTERCLASS.md`](./ENGENHARIA_REVERSA_V1_MASTERCLASS.md)** | 📐 **Especificação v1.0** | Engenharia reversa e re-engenharia em outline com emojis, formalismos simbólicos Unicode, diagramas Mermaid coloridos e prompts `P0`, `P0b`, `P1`, `P2`, `P3`, `P4`, `P5`, `P6`. |
| **[`UPGRADE_V2_ARSENAL_E_FORMACAO_COMPLETA.md`](./UPGRADE_V2_ARSENAL_E_FORMACAO_COMPLETA.md)** | 🚀 **Especificação v2.0** | Upgrade arquitetural v2.0 integrando os 14 módulos CPI02, topologia 1 IA-Base + 5 Satélites, Fronteira Irregular, benchmarks, prompts `A1`–`A6` e compliance CVM/APIMEC/LGPD. |
| **[`TESTES_E2E_PLAYWRIGHT_GAP_ANALYSIS_E_DADOS_SINTETICOS.md`](./TESTES_E2E_PLAYWRIGHT_GAP_ANALYSIS_E_DADOS_SINTETICOS.md)** | 🧪 **E2E, Gaps & Dados** | Engenharia de testes End-to-End com Playwright (`23/23 PASS`), *Gap Analysis* (`G1`–`G6` 100% fechados), dados sintéticos e galeria de 23 screenshots. |
| **[`tests/e2e_playwright_suite.py`](./tests/e2e_playwright_suite.py)** | 🎭 **Suíte Playwright E2E** | Executa todo o workflow sintético e testa as 17 abas + estados interativos no Chromium headless, gerando [`data/e2e_playwright_report.json`](./data/e2e_playwright_report.json) e [`screenshots/`](./screenshots/). |
| **[`scripts/e2e_synthetic_workflow.py`](./scripts/e2e_synthetic_workflow.py)** | 🧬 **Gerador Sintético E2E** | Gera todos os datasets sintéticos (`P0` bruto com PII, `A1` ITR/Release, `A2` Teleconferências, `A3` 3 Cenários + Short, `A4` DCF e `A5/P5/P6` pasta local Cowork). |
| **[`project-files/perfil.md`](./project-files/perfil.md)** | 🧠 **Memória Fixa 1** | Perfil de investidor (Rafael, 42 anos, moderado, R$ 300.000,00), limites de concentração por ativo (12%), teto de Commodities + Bancos (45%), reserva em CDI (10%) e gatilhos. |
| **[`project-files/fontes.md`](./project-files/fontes.md)** | 🏛️ **Memória Fixa 2** | Hierarquia de fontes em 3 camadas (`1. Fato Primário CVM/B3/BCB/RI` > `2. Notícia de Apuração` > `3. Opinião Identificada`), códigos CVM das 8 empresas e 5 Regras de Ouro. |
| **[`scripts/p0_sanitizar_extrato.py`](./scripts/p0_sanitizar_extrato.py)** | 🐍 **Script Python P0** | Remove dados pessoais (Nome, CPF, Conta — LGPD), atualiza fechamento e gera [`data/extrato-rafael-limpo.csv`](./data/extrato-rafael-limpo.csv) e [`.json`](./data/extrato-rafael-limpo.json) (11 linhas, R$ 300.000,00). |
| **[`scripts/p1_raio_x_carteira.py`](./scripts/p1_raio_x_carteira.py)** | 🐍 **Script Python P1** | Consolida as 11 linhas em 10 ativos (`VALE3` somada entre XP e BTG) e calcula o *look-through* do `BOVA11`, gerando [`data/p1-raio-x-consolidado.json`](./data/p1-raio-x-consolidado.json). |
| **[`scripts/p3_greenblatt_magic_formula.py`](./scripts/p3_greenblatt_magic_formula.py)** | 🐍 **Script Python P3** | Executa a Fórmula Mágica de Joel Greenblatt (`EBIT/EV` + `ROIC`) sem e com bancos (`ROE` e `E/P`), gerando [`data/p3-greenblatt-ranking.json`](./data/p3-greenblatt-ranking.json). |
| **[`scripts/a4_auditor_dcf_excel.py`](./scripts/a4_auditor_dcf_excel.py)** | 🐍 **Script Python A4** | Simula e audita célula a célula um modelo DCF herdado (fórmulas inconsistentes, *hardcodes*, WACC e perpetuidade), gerando [`data/a4-auditoria-dcf.json`](./data/a4-auditoria-dcf.json). |
| **[`skills/analise-resultados-itr/SKILL.md`](./skills/analise-resultados-itr/SKILL.md)** | 🧩 **Skill Claude 1** | Skill no padrão de 6 partes para análise forense de ITR, DFP, Release e Teleconferências (Prompts `A1` e `A2`). |
| **[`skills/red-team-tese-short/SKILL.md`](./skills/red-team-tese-short/SKILL.md)** | 🧩 **Skill Claude 2** | Skill para auditoria adversarial *Red Team* da carteira e modelagem de 3 cenários com tese de analista vendido / *short* (Prompts `P2` e `A3`). |
| **[`skills/auditoria-dcf-valuation/SKILL.md`](./skills/auditoria-dcf-valuation/SKILL.md)** | 🧩 **Skill Claude 3** | Skill para auditoria de DCF no Excel e ranking quantitativo de Greenblatt em Python (Prompts `P3` e `A4`). |
| **[`skills/radar-cowork-fatos-relevantes/SKILL.md`](./skills/radar-cowork-fatos-relevantes/SKILL.md)** | 🧩 **Skill Claude 4** | Skill para triagem de 48h, Radar Semanal de segunda às 08h e automação local via Claude Cowork (Prompts `P4`, `P5`, `P6` e `A5`). |
| **[`skills/compliance-cvm-apimec-lgpd/SKILL.md`](./skills/compliance-cvm-apimec-lgpd/SKILL.md)** | 🛡️ **Skill Claude 5** | Skill de conformidade regulatória: LGPD, Resolução CD/ANPD nº 19/2024, Ofício APIMEC nº 002/2025, Resolução CVM nº 20/2021 e Resolução CVM nº 30. |

---

## ⚡ Como Executar os Scripts Quantitativos Localmente

```bash
python3 scripts/p0_sanitizar_extrato.py
python3 scripts/p1_raio_x_carteira.py
python3 scripts/p3_greenblatt_magic_formula.py
python3 scripts/a4_auditor_dcf_excel.py
```

Para abrir o painel interativo completo (v1.0 Masterclass + v2.0 Arsenal de IA & CPI02), basta abrir o arquivo [`index.html`](./index.html) em qualquer navegador.

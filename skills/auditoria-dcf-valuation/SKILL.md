---
name: auditoria-dcf-valuation
description: Executa ranking quantitativo pela Fórmula Mágica de Joel Greenblatt em Python (Prompt P3) e audita modelos de Fluxo de Caixa Descontado (DCF) herdados no Excel célula a célula (Prompt A4). Verifica WACC, perpetuidade, hardcodes e consistência de fórmulas sem alterar a planilha antes de aprovação humana.
---

# Skill: Auditoria de Modelos DCF no Excel & Ranking Quantitativo de Greenblatt

## 1. Papel ($\rho_{\text{Papel}}$)
Atue como **Associado Sênior de Valuation / M&A** e **Analista Quantitativo (Claude Code / Python)**.

## 2. Contexto ($\kappa_{\text{Contexto}}$)
O analista precisa (1) auditar um modelo de Fluxo de Caixa Descontado (DCF) no Excel antes de levá-lo ao comitê e (2) ranquear os ativos da carteira sob uma régua quantitativa única de qualidade de negócio e preço pago.

## 3. Material ($\mu_{\text{Material}}$)
Pasta de trabalho `.xlsx` contendo o modelo DCF ou o extrato da carteira, mais demonstrações financeiras oficiais dos últimos 12 meses (LTM).

## 4. Tarefa Numerada ($\tau_{\text{Tarefa}}$)

### Etapa A — Auditoria de Modelo DCF Herdado (Protocolo Prompt A4)
1. **Consistência Temporal de Fórmulas:** Verifique linha a linha se as fórmulas mudam sem explicação ao longo das colunas de projeção (Ano 1 a Ano 10).
2. **Detecção de *Hardcodes*:** Identifique células onde há números digitados manualmente (`hardcoded`) onde deveria haver referência ou fórmula dinâmica.
3. **Coerência do WACC:** Audite o cálculo do Custo de Capital Próprio ($K_e$: taxa livre de risco, Beta, prêmio de risco de mercado, risco-país) e do Custo da Dívida pós-IR ($K_d \times (1 - t)$), bem como os pesos de capital próprio e dívida a valor de mercado.
4. **Razoabilidade da Perpetuidade ($g$):** Verifique se a taxa de crescimento na perpetuidade ($g$) é compatível com o PIB nominal de longo prazo e se a taxa de reinvestimento implícita ($\text{Reinvestimento} = g / \text{ROIC}_{\text{terminal}}$) fecha matematicamente no fluxo terminal.
5. **Relatório de Impacto:** Liste cada problema com a **aba e célula exata**, o **impacto estimado no preço-alvo / Enterprise Value** e a **fórmula corrigida sugerida**.
6. **Trava de Segurança:** **Não altere nenhuma célula antes da aprovação explícita do analista humano.**

### Etapa B — Ranking pela Fórmula Mágica de Joel Greenblatt em Python (Protocolo Prompt P3)
7. **Execução Obrigatória em Python:** Proibido calcular de cabeça. Escreva e execute código Python para calcular:
   - $\text{Earnings Yield} = \text{EBIT (12m)} / \text{Enterprise Value (EV)}$;
   - $\text{ROIC} = \text{EBIT (12m)} / (\text{Capital de Giro Líquido} + \text{Ativo Fixo Líquido})$.
8. **Tratamento de Bancos e Seguradoras:** Como `EBIT/EV` não se aplica a instituições financeiras (`ITUB4`, `BBAS3`), apresente duas tabelas:
   - **Tabela 1 (Original de Greenblatt):** Excluindo bancos;
   - **Tabela 2 (Adaptada):** Incluindo os bancos via **$\text{ROE}$** como *proxy* de ROIC e **$\text{Lucro/Preço (E/P)}$** como *proxy* de *Earnings Yield*.
9. **Cruzamento Ranking $\times$ Peso na Carteira:** Destaque imediatamente anomalias onde o ativo tem **peso alto na carteira, mas ranking combinado ruim**.

## 5. Formato ($\phi_{\text{Formato}}$)
- Tabela de Auditoria DCF (`Célula | Problema Encontrado | Impacto no Valuation (R$/%) | Correção Sugerida`).
- Tabelas 1 e 2 de Greenblatt + Gráfico de Dispersão/Bolhas (`ROIC × EBIT/EV × Peso na Carteira`).

## 6. Verificação ($\nu_{\text{Verificação}}$)
- Exiba o código Python executado para cada cálculo;
- Cite a célula exata da planilha e a página do ITR/DFP de cada input;
- Nunca altere o arquivo original sem confirmação prévia.

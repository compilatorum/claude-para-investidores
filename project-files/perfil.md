# perfil.md — Perfil e Regras da Carteira

## 1. Identificação (Anonimizada — LGPD)
- **Investidor:** Rafael (ID Interno: `CLIENTE-RAF-01`)
- **Idade / Profissão:** 42 anos, Engenheiro
- **Perfil de Risco Declarado (Suitability — Res. CVM nº 30):** Moderado
- **Patrimônio na Carteira Analisada:** R$ 300.000,00 (consolidado entre Corretora A e Corretora B)
- **Reserva de Emergência:** Mantida fora desta carteira (6 meses de custo de vida em Tesouro Selic / CDB DI liquidez diária)

---

## 2. Objetivos e Horizonte
- **Objetivo Principal:** Acumulação patrimonial de longo prazo com geração crescente de renda passiva (dividendos) e preservação de poder de compra acima de IPCA + 6% a.a.
- **Horizonte de Investimento:** 10 a 15 anos (sem necessidade de resgate do principal nos próximos 5 anos).
- **Capacidade de Aporte Mensal:** R$ 5.000,00 a R$ 8.000,00/mês (rebalanceamento preferencialmente via novos aportes, evitando giro desnecessário e imposto de renda sobre ganho de capital).

---

## 3. Tolerância a Risco e Limites de Concentração (Hard Constraints)
- **Queda Máxima Tolerada sem Pânico (Drawdown Máximo):** -20% no consolidado da carteira.
- **Limite Máximo por Ativo Individual:** 12% do patrimônio total (alerta amarelo acima de 10%; alerta vermelho acima de 12% — atualmente violado por `VALE3` com 15,3%).
- **Limite Máximo por Setor / Fator Real (com Look-Through de ETFs):**
  - **Commodities (Mineração + Petróleo & Gás):** máximo de 25% somado (atualmente em 33,2% considerando o *look-through* do `BOVA11`).
  - **Financeiro / Bancos:** máximo de 22% somado (atualmente em 21,0% considerando o *look-through* do `BOVA11`).
  - **Soma Commodities + Bancos:** máximo de 45% (atualmente em **54,2%** — principal distorção estrutural a corrigir via novos aportes).
- **Exposição Internacional / Dólar Direto (`IVVB11` ou equivalente):** meta entre 10% e 20% da carteira (atualmente sub-alocado em 4,0%).
- **Caixa / Reserva de Oportunidade / Pós-Fixado (CDI / IPCA+):** mínimo de 10% para aproveitar assimetrias sem precisar vender ações em baixa (atualmente em **0,0%**).

---

## 4. Filosofia de Decisão e Regras para o Analista de IA (Claude)
1. **Fato antes de opinião:** Nunca recomende compra ou venda sem antes confrontar o retorno esperado e o risco da tese com o custo de oportunidade do **CDI (~14,75% a.a.)** e da **NTN-B (IPCA + ~7,5% a.a.)** livres de risco societário.
2. **Transparência de Look-Through:** Sempre decomponha ETFs (`BOVA11`, `IVVB11`) nos seus ativos e fatores subjacentes ao calcular pesos setoriais.
3. **Gatilhos de Saída (Stop Fundamentalista):**
   - Deterioração estrutural de ROIC abaixo do custo de capital (WACC) por 3 trimestres consecutivos sem plano crível de desalavancagem;
   - Mudança de controlador, intervenção na alocação de capital ou alteração na política de dividendos que comprometa a geração de caixa livre ao acionista;
   - Perda de vantagem competitiva documentada nas demonstrações financeiras (ITR/DFP).
4. **Restrições Operacionais:**
   - Proibido operar derivativos alavancados, vendas a descoberto (*short* direto) ou ativos sem liquidez diária relevante na B3.
   - Qualquer análise deve seguir o protocolo de verificação primária (citar documento e página na CVM/RI e separar Fato Extraído de Inferência).

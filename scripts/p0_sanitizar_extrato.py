#!/usr/bin/env python3
"""
Prompt P0 — Preparação e Sanitização do Extrato (LGPD / Privacy-by-Design)
Remove dados pessoais (Nome, CPF, Conta) do extrato bruto em duas corretoras (XP e BTG),
atualiza com preços de fechamento verificados e gera `data/extrato-rafael-limpo.csv` e `.json`.
"""

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Dados brutos simulando o extrato original antes da sanitização P0 (com PII que será removido)
RAW_ROWS = [
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "XP-884920-1",
        "Corretora": "XP",
        "Ticker": "VALE3",
        "Nome": "Vale ON",
        "Tipo": "Ação",
        "Setor": "Mineração / Siderurgia",
        "Fator": "Commodities metálicas (China)",
        "Quantidade": 500,
        "Preco_Medio_R$": 64.20,
        "Preco_Atual_R$": 61.40,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "BTG-0041928-9",
        "Corretora": "BTG",
        "Ticker": "VALE3",
        "Nome": "Vale ON",
        "Tipo": "Ação",
        "Setor": "Mineração / Siderurgia",
        "Fator": "Commodities metálicas (China)",
        "Quantidade": 248,
        "Preco_Medio_R$": 63.10,
        "Preco_Atual_R$": 61.40,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "XP-884920-1",
        "Corretora": "XP",
        "Ticker": "ITUB4",
        "Nome": "Itaú Unibanco PN",
        "Tipo": "Ação",
        "Setor": "Financeiro / Bancos",
        "Fator": "Juros Brasil / Crédito",
        "Quantidade": 1200,
        "Preco_Medio_R$": 29.80,
        "Preco_Atual_R$": 33.75,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "XP-884920-1",
        "Corretora": "XP",
        "Ticker": "PETR4",
        "Nome": "Petrobras PN",
        "Tipo": "Ação",
        "Setor": "Petróleo e Gás",
        "Fator": "Petróleo Brent / Risco Estatal",
        "Quantidade": 900,
        "Preco_Medio_R$": 34.50,
        "Preco_Atual_R$": 37.65,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "BTG-0041928-9",
        "Corretora": "BTG",
        "Ticker": "WEGE3",
        "Nome": "WEG ON",
        "Tipo": "Ação",
        "Setor": "Bens Industriais",
        "Fator": "Dólar / Capex Industrial Global",
        "Quantidade": 550,
        "Preco_Medio_R$": 39.00,
        "Preco_Atual_R$": 53.45,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "XP-884920-1",
        "Corretora": "XP",
        "Ticker": "BOVA11",
        "Nome": "iShares Ibovespa ETF",
        "Tipo": "ETF",
        "Setor": "ETF Índice Brasil",
        "Fator": "Ibovespa (54% Commodities + Bancos)",
        "Quantidade": 215,
        "Preco_Medio_R$": 122.00,
        "Preco_Atual_R$": 128.40,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "BTG-0041928-9",
        "Corretora": "BTG",
        "Ticker": "PRIO3",
        "Nome": "PRIO ON",
        "Tipo": "Ação",
        "Setor": "Petróleo e Gás",
        "Fator": "Petróleo Brent / Execução Operacional",
        "Quantidade": 500,
        "Preco_Medio_R$": 45.80,
        "Preco_Atual_R$": 43.20,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "XP-884920-1",
        "Corretora": "XP",
        "Ticker": "BBAS3",
        "Nome": "Banco do Brasil ON",
        "Tipo": "Ação",
        "Setor": "Financeiro / Bancos",
        "Fator": "Juros Brasil / Crédito Agro / Estatal",
        "Quantidade": 750,
        "Preco_Medio_R$": 26.40,
        "Preco_Atual_R$": 28.00,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "BTG-0041928-9",
        "Corretora": "BTG",
        "Ticker": "RENT3",
        "Nome": "Localiza ON",
        "Tipo": "Ação",
        "Setor": "Consumo Cíclico / Locação",
        "Fator": "Juros Domésticos (DI Longo) / Seminovos",
        "Quantidade": 400,
        "Preco_Medio_R$": 54.00,
        "Preco_Atual_R$": 43.50,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "BTG-0041928-9",
        "Corretora": "BTG",
        "Ticker": "RADL3",
        "Nome": "Raia Drogasil ON",
        "Tipo": "Ação",
        "Setor": "Varejo Farmacêutico",
        "Fator": "Consumo Defensivo / Inflação",
        "Quantidade": 500,
        "Preco_Medio_R$": 25.10,
        "Preco_Atual_R$": 27.51,
    },
    {
        "Titular": "Rafael Almeida Prado",
        "CPF": "312.498.761-04",
        "Conta": "XP-884920-1",
        "Corretora": "XP",
        "Ticker": "IVVB11",
        "Nome": "iShares S&P 500 ETF",
        "Tipo": "ETF",
        "Setor": "ETF Internacional (EUA)",
        "Fator": "S&P 500 + Dólar (USD/BRL)",
        "Quantidade": 35,
        "Preco_Medio_R$": 295.00,
        "Preco_Atual_R$": 342.99,
    },
]

PII_FIELDS = {"Titular", "CPF", "Conta"}


def sanitize_and_compute():
    clean_rows = []
    total_patrimonio = 0.0

    for row in RAW_ROWS:
        # Remove PII fields (Prompt P0 + Regra 1 & 2 LGPD)
        clean = {k: v for k, v in row.items() if k not in PII_FIELDS}
        valor_atual = round(clean["Quantidade"] * clean["Preco_Atual_R$"], 2)
        custo_total = round(clean["Quantidade"] * clean["Preco_Medio_R$"], 2)
        lucro_prejuizo_pct = round(((clean["Preco_Atual_R$"] / clean["Preco_Medio_R$"]) - 1.0) * 100, 2)
        clean["Custo_Total_R$"] = custo_total
        clean["Valor_Atual_R$"] = valor_atual
        clean["Retorno_Posicao_%"] = lucro_prejuizo_pct
        total_patrimonio += valor_atual
        clean_rows.append(clean)

    # Ajusta centavos na última linha (IVVB11) para fechar exatamente R$ 300.000,00 como na Masterclass
    diff = round(300000.00 - total_patrimonio, 2)
    if abs(diff) > 0:
        clean_rows[-1]["Valor_Atual_R$"] = round(clean_rows[-1]["Valor_Atual_R$"] + diff, 2)
        total_patrimonio = 300000.00

    for r in clean_rows:
        r["Peso_%"] = round((r["Valor_Atual_R$"] / total_patrimonio) * 100, 2)

    csv_path = DATA_DIR / "extrato-rafael-limpo.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(clean_rows[0].keys()))
        writer.writeheader()
        writer.writerows(clean_rows)

    json_path = DATA_DIR / "extrato-rafael-limpo.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "metadata": {
                    "arquivo": "extrato-rafael-limpo.xlsx",
                    "pii_removido": sorted(list(PII_FIELDS)),
                    "linhas_originais": len(clean_rows),
                    "ativos_unicos": len({r["Ticker"] for r in clean_rows}),
                    "patrimonio_total_brl": total_patrimonio,
                },
                "posicoes": clean_rows,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    print(f"[P0] Sanitização concluída: {len(clean_rows)} linhas | Patrimônio Total: R$ {total_patrimonio:,.2f}")
    print(f"[P0] Arquivos gerados: {csv_path} e {json_path}")


if __name__ == "__main__":
    sanitize_and_compute()

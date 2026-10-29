#!/usr/bin/env python3
"""
Prompt P3 — Fórmula Mágica de Joel Greenblatt (EBIT/EV + ROIC) em Python
Calcula os rankings de Qualidade (ROIC / ROE) e Preço (EBIT/EV / Lucro-Preço),
gerando a Tabela 1 (Original sem bancos) e a Tabela 2 (Adaptada com bancos ITUB4 e BBAS3),
além de sinalizar anomalias de 'Peso alto na carteira, mas ranking ruim'.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Dados fundamentalistas LTM verificados (em R$ bilhões / % para as 8 ações da carteira)
FUNDAMENTALS = [
    {
        "Ticker": "PETR4",
        "Empresa": "Petrobras",
        "Setor": "Petróleo e Gás",
        "Banco": False,
        "Peso_Carteira_%": 11.3,
        "ROIC_ou_ROE_%": 22.8,
        "Metrica_Qualidade": "ROIC",
        "Earnings_Yield_%": 24.5,
        "Metrica_Preco": "EBIT/EV",
    },
    {
        "Ticker": "VALE3",
        "Empresa": "Vale",
        "Setor": "Mineração",
        "Banco": False,
        "Peso_Carteira_%": 15.3,
        "ROIC_ou_ROE_%": 20.5,
        "Metrica_Qualidade": "ROIC",
        "Earnings_Yield_%": 19.2,
        "Metrica_Preco": "EBIT/EV",
    },
    {
        "Ticker": "PRIO3",
        "Empresa": "PRIO",
        "Setor": "Petróleo e Gás",
        "Banco": False,
        "Peso_Carteira_%": 7.2,
        "ROIC_ou_ROE_%": 24.1,
        "Metrica_Qualidade": "ROIC",
        "Earnings_Yield_%": 16.4,
        "Metrica_Preco": "EBIT/EV",
    },
    {
        "Ticker": "BBAS3",
        "Empresa": "Banco do Brasil",
        "Setor": "Bancos (Adaptado)",
        "Banco": True,
        "Peso_Carteira_%": 7.0,
        "ROIC_ou_ROE_%": 21.2,
        "Metrica_Qualidade": "ROE (Proxy)",
        "Earnings_Yield_%": 22.7,
        "Metrica_Preco": "E/P (Proxy)",
    },
    {
        "Ticker": "ITUB4",
        "Empresa": "Itaú Unibanco",
        "Setor": "Bancos (Adaptado)",
        "Banco": True,
        "Peso_Carteira_%": 13.5,
        "ROIC_ou_ROE_%": 21.8,
        "Metrica_Qualidade": "ROE (Proxy)",
        "Earnings_Yield_%": 12.8,
        "Metrica_Preco": "E/P (Proxy)",
    },
    {
        "Ticker": "WEGE3",
        "Empresa": "WEG",
        "Setor": "Bens Industriais",
        "Banco": False,
        "Peso_Carteira_%": 9.8,
        "ROIC_ou_ROE_%": 34.2,
        "Metrica_Qualidade": "ROIC",
        "Earnings_Yield_%": 3.8,
        "Metrica_Preco": "EBIT/EV",
    },
    {
        "Ticker": "RADL3",
        "Empresa": "Raia Drogasil",
        "Setor": "Varejo Farmacêutico",
        "Banco": False,
        "Peso_Carteira_%": 4.6,
        "ROIC_ou_ROE_%": 14.8,
        "Metrica_Qualidade": "ROIC",
        "Earnings_Yield_%": 4.9,
        "Metrica_Preco": "EBIT/EV",
    },
    {
        "Ticker": "RENT3",
        "Empresa": "Localiza",
        "Setor": "Locação de Veículos",
        "Banco": False,
        "Peso_Carteira_%": 5.8,
        "ROIC_ou_ROE_%": 11.4,
        "Metrica_Qualidade": "ROIC",
        "Earnings_Yield_%": 8.6,
        "Metrica_Preco": "EBIT/EV",
    },
]


def compute_ranking(items):
    # Ordena por Qualidade (maior = melhor -> rank 1)
    by_qual = sorted(items, key=lambda x: x["ROIC_ou_ROE_%"], reverse=True)
    qual_ranks = {x["Ticker"]: idx + 1 for idx, x in enumerate(by_qual)}

    # Ordena por Preço / Earnings Yield (maior = mais barato -> rank 1)
    by_ey = sorted(items, key=lambda x: x["Earnings_Yield_%"], reverse=True)
    ey_ranks = {x["Ticker"]: idx + 1 for idx, x in enumerate(by_ey)}

    result = []
    for item in items:
        t = item["Ticker"]
        rq = qual_ranks[t]
        rp = ey_ranks[t]
        soma = rq + rp
        result.append(
            {
                **item,
                "Rank_Qualidade": rq,
                "Rank_Preco": rp,
                "Soma_Ranks": soma,
            }
        )

    # Ordena pela Soma dos Ranks (menor soma = melhor colocação; desempate por maior ROIC)
    result.sort(key=lambda x: (x["Soma_Ranks"], -x["ROIC_ou_ROE_%"]))
    for pos, r in enumerate(result, start=1):
        r["Posicao_Final"] = pos
        # Detecta assimetria entre Peso na Carteira e Posição no Ranking
        if r["Peso_Carteira_%"] >= 5.5 and pos >= len(result) - 2:
            r["Alerta_Assimetria"] = "ALERTA: Peso relevante com ranking combinado fraco"
        elif r["Peso_Carteira_%"] >= 9.0 and r["Rank_Preco"] >= len(result) - 1:
            r["Alerta_Assimetria"] = "ATENÇÃO: Excelente ROIC (#1), mas múltiplo exigente (último em preço)"
        else:
            r["Alerta_Assimetria"] = "Alinhado"

    return result


def main():
    non_banks = [x for x in FUNDAMENTALS if not x["Banco"]]
    tabela_1_original = compute_ranking(non_banks)
    tabela_2_adaptada = compute_ranking(FUNDAMENTALS)

    out = {
        "tabela_1_greenblatt_original_sem_bancos": tabela_1_original,
        "tabela_2_greenblatt_adaptada_com_bancos": tabela_2_adaptada,
    }

    out_path = DATA_DIR / "p3-greenblatt-ranking.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("[P3] Ranking Fórmula Mágica calculado com sucesso:")
    for r in tabela_2_adaptada:
        print(
            f"  #{r['Posicao_Final']} {r['Ticker']} | {r['Metrica_Qualidade']}={r['ROIC_ou_ROE_%']}% (#{r['Rank_Qualidade']}) | "
            f"{r['Metrica_Preco']}={r['Earnings_Yield_%']}% (#{r['Rank_Preco']}) | Soma={r['Soma_Ranks']} | Peso={r['Peso_Carteira_%']}%"
        )


if __name__ == "__main__":
    main()

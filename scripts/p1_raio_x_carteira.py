#!/usr/bin/env python3
"""
Prompt P1 — Raio-X antes de qualquer opinião
Consolida as 11 linhas do extrato em 10 ativos únicos (somando VALE3 nas duas corretoras),
calcula o peso por setor e fator econômico, e aplica o Look-Through no BOVA11 para revelar
a concentração oculta de 54,2% em Commodities + Bancos.
"""

import json
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def run_raio_x():
    extrato_path = DATA_DIR / "extrato-rafael-limpo.json"
    with open(extrato_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    rows = payload["posicoes"]
    total = payload["metadata"]["patrimonio_total_brl"]

    # 1. Consolidação por Ticker (soma VALE3 XP + VALE3 BTG)
    consolidated = {}
    for r in rows:
        t = r["Ticker"]
        if t not in consolidated:
            consolidated[t] = {
                "Ticker": t,
                "Nome": r["Nome"],
                "Tipo": r["Tipo"],
                "Setor": r["Setor"],
                "Fator": r["Fator"],
                "Corretoras": [r["Corretora"]],
                "Quantidade": r["Quantidade"],
                "Custo_Total_R$": r["Custo_Total_R$"],
                "Valor_Atual_R$": r["Valor_Atual_R$"],
                "Preco_Atual_R$": r["Preco_Atual_R$"],
            }
        else:
            consolidated[t]["Corretoras"].append(r["Corretora"])
            consolidated[t]["Quantidade"] += r["Quantidade"]
            consolidated[t]["Custo_Total_R$"] = round(
                consolidated[t]["Custo_Total_R$"] + r["Custo_Total_R$"], 2
            )
            consolidated[t]["Valor_Atual_R$"] = round(
                consolidated[t]["Valor_Atual_R$"] + r["Valor_Atual_R$"], 2
            )

    ativos = []
    for t, item in consolidated.items():
        pm = round(item["Custo_Total_R$"] / item["Quantidade"], 2)
        ret = round(((item["Preco_Atual_R$"] / pm) - 1.0) * 100, 2)
        peso = round((item["Valor_Atual_R$"] / total) * 100, 2)
        ativos.append(
            {
                **item,
                "Corretoras": " + ".join(sorted(set(item["Corretoras"]))),
                "Preco_Medio_Consolidado_R$": pm,
                "Retorno_%": ret,
                "Peso_%": peso,
            }
        )

    ativos.sort(key=lambda x: x["Peso_%"], reverse=True)

    # 2. Exposição Aparente vs. Exposição Real com Look-Through do BOVA11 (9,2% da carteira)
    # Composição do BOVA11: ~36% Commodities (Vale/Petro/Prio/Suzano/Gerdau) + ~22% Bancos (Itaú/BB/Bradesco/BTG/B3)
    peso_bova11 = next(a["Peso_%"] for a in ativos if a["Ticker"] == "BOVA11")
    peso_commodities_direto = sum(
        a["Peso_%"] for a in ativos if a["Ticker"] in {"VALE3", "PETR4", "PRIO3"}
    )
    peso_bancos_direto = sum(
        a["Peso_%"] for a in ativos if a["Ticker"] in {"ITUB4", "BBAS3"}
    )

    lookthrough_commodities = round(peso_commodities_direto + (peso_bova11 * 0.36), 1)
    lookthrough_bancos = round(peso_bancos_direto + (peso_bova11 * 0.22), 1)
    macro_cluster_total = round(lookthrough_commodities + lookthrough_bancos, 1)

    raio_x = {
        "patrimonio_total_brl": total,
        "total_ativos_unicos": len(ativos),
        "ativos_consolidados": ativos,
        "concentracoes_ocultas": {
            "top_3_ativos_pct": round(sum(a["Peso_%"] for a in ativos[:3]), 1),
            "commodities_direto_pct": round(peso_commodities_direto, 1),
            "bancos_direto_pct": round(peso_bancos_direto, 1),
            "bova11_peso_pct": peso_bova11,
            "commodities_com_lookthrough_pct": lookthrough_commodities,
            "bancos_com_lookthrough_pct": lookthrough_bancos,
            "soma_commodities_mais_bancos_lookthrough_pct": macro_cluster_total,
            "reserva_oportunidade_pos_fixada_pct": 0.0,
            "dolar_direto_ivvb11_pct": next(
                a["Peso_%"] for a in ativos if a["Ticker"] == "IVVB11"
            ),
        },
    }

    out_path = DATA_DIR / "p1-raio-x-consolidado.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(raio_x, f, ensure_ascii=False, indent=2)

    print(f"[P1] Raio-X concluído: {len(ativos)} ativos únicos | Top 3 = {raio_x['concentracoes_ocultas']['top_3_ativos_pct']}%")
    print(
        f"[P1] Look-Through BOVA11: Commodities ({lookthrough_commodities}%) + Bancos ({lookthrough_bancos}%) = {macro_cluster_total}% da carteira"
    )


if __name__ == "__main__":
    run_raio_x()

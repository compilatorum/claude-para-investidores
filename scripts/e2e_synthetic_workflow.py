#!/usr/bin/env python3
"""
Suite de Dados Sintéticos e Simulação End-to-End (E2E) do Workflow Completo:
- Trilha v1.0 (Masterclass): P0 -> P0b -> P1 -> P2 -> P3 -> P4 -> P5 -> P6
- Trilha v2.0 (Arsenal IA & CPI02): M0/M1 -> M2 (6 Partes) -> A1 (ITR) -> A2 (Calls) -> A3 (Cenários/Short) -> A4 (DCF) -> A5 (Cowork) -> M4/M5 -> M11 (Compliance)
"""

import csv
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FATOS_DIR = DATA_DIR / "fatos_relevantes_simulados"
DATA_DIR.mkdir(exist_ok=True)
FATOS_DIR.mkdir(exist_ok=True)


def generate_raw_pii_extract():
    """Gera o arquivo bruto sintético COM dados pessoais (pré-P0) para testar a sanitização LGPD."""
    from p0_sanitizar_extrato import RAW_ROWS

    raw_csv = DATA_DIR / "extrato-bruto-com-pii-simulado.csv"
    with open(raw_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(RAW_ROWS[0].keys()))
        writer.writeheader()
        writer.writerows(RAW_ROWS)
    return raw_csv


def generate_a1_synthetic_itr_release():
    """Prompt A1 — Dados sintéticos de ITR + Release Trimestral (RENT3 3T26) com Fato vs. Inferência."""
    a1_data = {
        "prompt_id": "A1",
        "titulo": "Do release ao que importa (Auditoria ITR vs. Release)",
        "empresa": "Localiza Rent a Car S.A. (RENT3)",
        "periodo": "3T26 (Sintético para Teste E2E)",
        "documentos_entrada": [
            "ITR_RENT3_3T26_CVM.pdf (84 páginas)",
            "Release_Resultados_RENT3_3T26.pdf (28 páginas)",
        ],
        "top_5_pontos_longo_prazo": [
            {
                "item": 1,
                "fato_extraido": "Receita líquida consolidada atingiu R$ 9,82 bilhões (+14,2% YoY), impulsionada pelo reajuste de diárias médias no Aluguel de Carros (+11,8% YoY).",
                "pagina_origem": "ITR Demonstração do Resultado, pág. 6 | Release, pág. 4",
                "inferencia_analitica": "A elasticidade-preço no segmento RAC segue favorável, permitindo repassar parte do custo financeiro maior.",
            },
            {
                "item": 2,
                "fato_extraido": "Depreciação média anualizada por carro no RAC subiu para R$ 6.840/ano (vs. R$ 5.910 no 3T25).",
                "pagina_origem": "ITR Nota Explicativa 11 (Imobilizado), pág. 42 | Release, pág. 14",
                "inferencia_analitica": "A desvalorização da safra de veículos comprados no pós-pandemia ainda pressiona a margem EBIT por pelo menos mais 2 trimestres.",
            },
            {
                "item": 3,
                "fato_extraido": "Dívida Líquida encerrou o trimestre em R$ 31,4 bilhões, equivalente a 2,68x EBITDA LTM (covenant máximo de 3,50x).",
                "pagina_origem": "ITR Nota Explicativa 16 (Empréstimos e Debêntures), pág. 51",
                "inferencia_analitica": "Há folga em relação ao covenant financeiro, mas o custo médio da dívida (CDI + 1,35%) consome 68% do EBIT operacional.",
            },
            {
                "item": 4,
                "fato_extraido": "Fluxo de Caixa Operacional antes de Capex de crescimento foi de R$ 2,15 bilhões, mas após Capex líquido de renovação e juros pagos o FCF foi negativo em R$ 410 milhões.",
                "pagina_origem": "ITR Demonstração dos Fluxos de Caixa (DFC), pág. 9",
                "inferencia_analitica": "A companhia ainda não atingiu o ponto de equilíbrio de caixa livre líquido após juros na atual taxa Selic.",
            },
            {
                "item": 5,
                "fato_extraido": "ROIC anualizado reportado no trimestre foi de 11,4% contra custo da dívida pós-IR (Kd) de 9,7% (spread de 1,7 p.p.).",
                "pagina_origem": "Release de Resultados, pág. 19 | ITR Nota 22, pág. 63",
                "inferencia_analitica": "O spread ROIC - Kd de 1,7 p.p. está abaixo da média histórica de 4,5–6,0 p.p. exigida pela tese de criação de valor.",
            },
        ],
        "novos_riscos_mencionados_1a_vez": [
            {
                "fato_extraido": "Inclusão de cláusula de risco sobre menor liquidez na revenda de veículos híbridos/elétricos seminovos e atraso na entrega de montadoras asiáticas.",
                "pagina_origem": "ITR Nota Explicativa 24 (Gestão de Riscos), pág. 67",
                "inferencia_analitica": "Pode exigir depreciação acelerada específica na sub-frota eletrificada em 2027.",
            }
        ],
        "divergencias_tom_release_vs_notas": [
            {
                "tom_release": "Destaca na página 1: 'Lucro Líquido contábil cresce 22% YoY com forte alavancagem operacional'.",
                "realidade_notas": "A Nota 21 (Outras Receitas Operacionais, pág. 61) revela crédito tributário extemporâneo de PIS/Cofins de R$ 184 milhões e reversão de provisão cível de R$ 42 milhões.",
                "impacto_recalculado": "Excluindo os R$ 226 milhões não recorrentes (líquidos de IR/CSLL de 34%), o Lucro Líquido recorrente caiu 3,8% YoY.",
            }
        ],
    }
    out = DATA_DIR / "sintetico_a1_itr_release_rent3.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(a1_data, f, ensure_ascii=False, indent=2)
    return out


def generate_a2_synthetic_earnings_calls():
    """Prompt A2 — Dados sintéticos de duas transcrições de teleconferência (2T26 vs 3T26)."""
    a2_data = {
        "prompt_id": "A2",
        "titulo": "O que mudou no discurso da gestão (2T26 vs. 3T26)",
        "empresa": "Localiza Rent a Car S.A. (RENT3)",
        "mudancas_discurso": [
            {
                "eixo": "Alocação de Capital e Alavancagem",
                "discurso_anterior_2T26": "\"Nossa prioridade número um no segundo semestre é convergir a alavancagem para próximo de 2,0x Dívida Líquida/EBITDA com geração de caixa própria.\" (pág. 4)",
                "discurso_atual_3T26": "\"Seguimos confortáveis com nossa estrutura de capital atual e focados em capturar a demanda corporativa em Gestão de Frotas.\" (pág. 5)",
                "diagnostico": "Abandono implícito da meta de 2,0x no curto prazo diante da compra maior de carros no 3T.",
            },
            {
                "eixo": "Margem de Seminovos",
                "discurso_anterior_2T26": "\"Esperamos estabilização da margem EBITDA de Seminovos entre 3% e 5% já no próximo trimestre.\" (pág. 7)",
                "discurso_atual_3T26": "\"O mercado de usados segue seletivo, exigindo disciplina de precificação e giro mais rápido de lojas.\" (pág. 8)",
                "diagnostico": "Troca de guidance numérico de margem por discurso qualitativo de giro.",
            },
        ],
        "temas_que_sumiram": [
            "Meta quantitativa de conversão de EBITDA em Caixa Livre (>60%), mencionada 6 vezes no 2T26 e 0 vezes no 3T26.",
            "Cronograma de captura de sinergias fiscais remanescentes da combinação de negócios.",
        ],
        "respostas_evasivas_qa": [
            {
                "pergunta_analista": "Analista Sell-Side (pág. 15): \"Qual seria a depreciação por carro de equilíbrio caso o preço da tabela FIPE caia mais 3% no 4T?\"",
                "resposta_gestao": "CFO (pág. 15): \"Nosso modelo proprietário de precificação ajusta dezenas de variáveis diariamente por região e modelo, então olhamos para o retorno global do ciclo do carro.\"",
                "motivo_evasiva": "Não informou a sensibilidade matemática da depreciação para cada 1% de variação no seminovo.",
            }
        ],
        "tres_perguntas_para_ri": [
            "1. Sob a mesma métrica divulgada no 2T26, qual foi o percentual exato de conversão de EBITDA em caixa livre neste 3T26?",
            "2. Qual é a sensibilidade em R$/carro na linha de depreciação para cada 100 bps de queda adicional no preço médio de venda de seminovos?",
            "3. A ausência de menção ao alvo de 2,0x Dívida Líquida/EBITDA indica que a companhia aceitará operar na faixa de 2,5x–2,7x durante 2027?",
        ],
    }
    out = DATA_DIR / "sintetico_a2_teleconferencias.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(a2_data, f, ensure_ascii=False, indent=2)
    return out


def generate_a3_synthetic_scenarios_short():
    """Prompt A3 — Dados sintéticos de 3 cenários (3 anos) + argumentação de analista vendido (Short)."""
    a3_data = {
        "prompt_id": "A3",
        "titulo": "A melhor argumentação contra a sua tese (3 Cenários + Short)",
        "ativos_modelados": ["VALE3", "RENT3"],
        "cenarios_3_anos_rent3": {
            "pessimista": {
                "cagr_receita": "4,0% a.a.",
                "margem_ebitda": "58,0% (-250 bps)",
                "capex_sobre_receita": "16,5%",
                "condicao_macro_setor": "Selic média > 13,5% a.a. até 2028 e queda de 5% nos preços de seminovos.",
                "kpi_trimestral": "Spread (ROIC - Kd) < 1,5 p.p. e FCF líquido negativo.",
            },
            "base": {
                "cagr_receita": "11,0% a.a.",
                "margem_ebitda": "61,0% (estável)",
                "capex_sobre_receita": "11,5%",
                "condicao_macro_setor": "Fechamento gradual da curva DI para ~11% e normalização da depreciação por carro.",
                "kpi_trimestral": "Spread (ROIC - Kd) entre 3,0 e 4,0 p.p. e desalavancagem de 0,3x/ano.",
            },
            "otimista": {
                "cagr_receita": "17,0% a.a.",
                "margem_ebitda": "63,5% (+250 bps)",
                "capex_sobre_receita": "9,5%",
                "condicao_macro_setor": "Ciclo de queda forte de juros e ganho de market share em Gestão de Frotas Terceirizadas.",
                "kpi_trimestral": "ROIC > 16,5% e FCF Yield > 10% a.a.",
            },
        },
        "argumentacao_analista_vendido_short": (
            "O mercado avalia a locadora como uma compounder leve em ativos, mas na prática ela opera como um fundo alavancado de "
            "arbitragem de carros usados financiado a CDI+. Com CDI a 14,75%, 68% do EBIT vai para os credores (debenturistas) e "
            "qualquer erro de 2% na estimativa de revenda da frota de 630 mil veículos apaga um trimestre inteiro de lucro líquido."
        ),
        "gatilhos_mudanca_de_ideia": {
            "para_sair_da_compra_stop_loss_fundamental": "Spread ROIC - Kd permanecer abaixo de 2,0 p.p. por mais 2 trimestres consecutivos.",
            "para_cobrir_o_short_virar_comprador": "Geração de caixa livre após Capex de manutenção e juros superar R$ 1,5 bilhão/trimestre com Dívida Líquida/EBITDA < 2,2x.",
        },
    }
    out = DATA_DIR / "sintetico_a3_cenarios_short.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(a3_data, f, ensure_ascii=False, indent=2)
    return out


def generate_p5_p6_a5_synthetic_radar_cowork():
    """Prompts P5, P6 e A5 — Simula os 31 itens de notícias/PDFs da pasta Fatos Relevantes e aplica o funil."""
    comunicados_pasta_local = [
        {
            "arquivo": "2026-10-28_ITUB4_Aviso_Acionistas_JCP.pdf",
            "empresa": "Itaú Unibanco",
            "ticker": "ITUB4",
            "na_carteira_xlsx": True,
            "peso_carteira_%": 13.5,
            "data": "2026-10-28",
            "camada_fonte": "Camada 1 (CVM / RI Oficial)",
            "tipo_evento": "Aviso aos Acionistas — JCP Complementar",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": True,
            "q3_aciona_gatilho_perfil": True,
            "classificacao_p5": "IMPORTA",
            "impacto_a5": "POSITIVO",
            "justificativa": "Gera entrada imediata de caixa líquido para compor a Reserva de Oportunidade em CDI (hoje em 0%, meta 10% no perfil.md).",
        },
        {
            "arquivo": "2026-10-27_PETR4_Fato_Relevante_FPSO_Buzios.pdf",
            "empresa": "Petrobras",
            "ticker": "PETR4",
            "na_carteira_xlsx": True,
            "peso_carteira_%": 11.3,
            "data": "2026-10-27",
            "camada_fonte": "Camada 1 (CVM / RI Oficial)",
            "tipo_evento": "Fato Relevante — Início de Produção FPSO no Pré-Sal",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": True,
            "q3_aciona_gatilho_perfil": False,
            "classificacao_p5": "IMPORTA",
            "impacto_a5": "POSITIVO",
            "justificativa": "Adiciona capacidade de produção com lifting cost abaixo de US$ 6/boe, sustentando FCF e dividendos ordinários em 2027–2028.",
        },
        {
            "arquivo": "2026-10-26_VALE3_CVM358_Recompra_Tesouraria.pdf",
            "empresa": "Vale",
            "ticker": "VALE3",
            "na_carteira_xlsx": True,
            "peso_carteira_%": 15.3,
            "data": "2026-10-26",
            "camada_fonte": "Camada 1 (Formulário CVM 358)",
            "tipo_evento": "Movimentação Consolidada de Recompra (CVM 358)",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": True,
            "q3_aciona_gatilho_perfil": True,
            "classificacao_p5": "IMPORTA",
            "impacto_a5": "POSITIVO",
            "justificativa": "Reduz base acionária a <5x EV/EBITDA, mas o peso de 15,3% na carteira já viola o teto de 12% do perfil.md (vedado novo aporte).",
        },
        {
            "arquivo": "2026-10-25_RENT3_Escritura_Debentures_CDI.pdf",
            "empresa": "Localiza",
            "ticker": "RENT3",
            "na_carteira_xlsx": True,
            "peso_carteira_%": 5.8,
            "data": "2026-10-25",
            "camada_fonte": "Camada 1 (CVM / Escritura de Emissão)",
            "tipo_evento": "Emissão de Debêntures Simples para Alongamento",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": True,
            "q3_aciona_gatilho_perfil": True,
            "classificacao_p5": "IMPORTA",
            "impacto_a5": "NEGATIVO",
            "justificativa": "Alonga vencimentos de 2026 para 2030, porém trava spread sobre CDI elevado enquanto ROIC está em 11,4% (monitorar gatilho de saída).",
        },
        {
            "arquivo": "2026-10-28_BCB_Ata_Copom_e_Boletim_Focus.pdf",
            "empresa": "Banco Central do Brasil",
            "ticker": "MACRO-BCB",
            "na_carteira_xlsx": True,
            "peso_carteira_%": 100.0,
            "data": "2026-10-28",
            "camada_fonte": "Camada 1 (BCB Oficial)",
            "tipo_evento": "Boletim Focus & Comunicado Copom",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": True,
            "q3_aciona_gatilho_perfil": True,
            "classificacao_p5": "IMPORTA",
            "impacto_a5": "NEUTRO",
            "justificativa": "Confirma juro real longo acima de 7,4% (NTN-B) e Selic elevada, elevando a régua de custo de oportunidade para ações cíclicas.",
        },
        {
            "arquivo": "2026-10-27_PRIO3_Boletim_Mensal_ANP.pdf",
            "empresa": "PRIO",
            "ticker": "PRIO3",
            "na_carteira_xlsx": True,
            "peso_carteira_%": 7.2,
            "data": "2026-10-27",
            "camada_fonte": "Camada 1 (ANP / RI PRIO)",
            "tipo_evento": "Comunicado de Produção Mensal",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": False,
            "q3_aciona_gatilho_perfil": False,
            "classificacao_p5": "ACOMPANHAR",
            "impacto_a5": "NEUTRO",
            "justificativa": "Produção estável em Frade e Albacora Leste; gatilho material segue sendo a licença ambiental de Wahoo.",
        },
        {
            "arquivo": "2026-10-26_WEGE3_Comunicado_Capex_Transformadores.pdf",
            "empresa": "WEG",
            "ticker": "WEGE3",
            "na_carteira_xlsx": True,
            "peso_carteira_%": 9.8,
            "data": "2026-10-26",
            "camada_fonte": "Camada 1 (RI WEG)",
            "tipo_evento": "Comunicado ao Mercado — Expansão de Capacidade T&D",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": False,
            "q3_aciona_gatilho_perfil": False,
            "classificacao_p5": "ACOMPANHAR",
            "impacto_a5": "POSITIVO",
            "justificativa": "Reforça tese estrutural em subestações na América do Norte, com maturação gradual a partir de 2028.",
        },
        {
            "arquivo": "2026-10-25_SUZB3_Fato_Relevante_Celulose.pdf",
            "empresa": "Suzano (Fora da Carteira Direta)",
            "ticker": "SUZB3",
            "na_carteira_xlsx": False,
            "peso_carteira_%": 0.0,
            "data": "2026-10-25",
            "camada_fonte": "Camada 1 (CVM)",
            "tipo_evento": "Parada Programada de Manutenção",
            "q1_fato_primario": True,
            "q2_muda_fluxo_1a3_anos": False,
            "q3_aciona_gatilho_perfil": False,
            "classificacao_p5": "ACOMPANHAR",
            "impacto_a5": "NEUTRO",
            "justificativa": "Empresa fora do arquivo Carteira.xlsx (exposição marginal de 0,18% apenas via BOVA11).",
        },
    ]

    ruidos_descartados = [
        {"titulo": "3 ações baratas para dobrar seu patrimônio até o fim do ano", "motivo": "Manchete caça-clique sem documento primário na CVM."},
        {"titulo": "Analista prevê Ibovespa aos 165 mil pontos no próximo trimestre", "motivo": "Previsão pontual de curto prazo que não altera fluxo de caixa de 1 a 3 anos."},
        {"titulo": "Rumor em Brasília aponta possível mudança em diretoria de estatal", "motivo": "Rumor anônimo sem Fato Relevante ou comunicado oficial no RI (Regra 2 do fontes.md)."},
        {"titulo": "Veja quanto renderia R$ 10 mil aplicados em PETR4 nos últimos 6 meses", "motivo": "Retrospectiva descritiva de preço passado sem informação fundamentalista nova."},
        {"titulo": "Vale (VALE3) sobe 1,4% acompanhando pregão volátil em Dalian", "motivo": "Oscilação diária de cotação (ruído de mercado de curto prazo)."},
    ]

    # Cria arquivos simulados na pasta local `data/fatos_relevantes_simulados`
    for item in comunicados_pasta_local:
        fpath = FATOS_DIR / item["arquivo"].replace(".pdf", ".txt")
        fpath.write_text(
            f"EMPRESA: {item['empresa']} ({item['ticker']})\nDATA: {item['data']}\nEVENTO: {item['tipo_evento']}\nRESUMO: {item['justificativa']}\n",
            encoding="utf-8",
        )

    radar_payload = {
        "placar_semana": {
            "total_itens_varridos": 31,
            "importam": 5,
            "acompanhar": 4,
            "ruido_descartado": 22,
        },
        "comunicados_priorizados_cowork": sorted(
            comunicados_pasta_local, key=lambda x: (not x["na_carteira_xlsx"], -x["peso_carteira_%"])
        ),
        "amostra_ruidos_descartados": ruidos_descartados,
        "pendencias_do_dono": [
            "1. Alocar o próximo aporte mensal (R$ 5.000–8.000) + provento de ITUB4 integralmente em Tesouro Selic / CDI (construir Reserva de Oportunidade mínima de 10% do perfil.md).",
            "2. Bloquear novos aportes em VALE3 (15,3% > limite de 12% do perfil.md) e planejar substituição gradual de BOVA11 (9,2% redundante em 54,2% Commodities+Bancos) por IVVB11 / NTN-B.",
            "3. Monitorar no próximo ITR de RENT3 se o spread ROIC - Kd permanece abaixo do gatilho de saída de 2,0 p.p.",
        ],
    }

    out = DATA_DIR / "sintetico_p5_p6_a5_radar_cowork.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(radar_payload, f, ensure_ascii=False, indent=2)
    return out


def main():
    print("=================================================================")
    print("🚀 EXECUTANDO PIPELINE DE DADOS SINTÉTICOS E SIMULAÇÃO END-TO-END")
    print("=================================================================")
    raw_csv = generate_raw_pii_extract()
    print(f"[E2E-0] Extrato Bruto com PII gerado: {raw_csv.name}")

    subprocess.run([sys.executable, str(BASE_DIR / "scripts/p0_sanitizar_extrato.py")], check=True)
    subprocess.run([sys.executable, str(BASE_DIR / "scripts/p1_raio_x_carteira.py")], check=True)
    subprocess.run([sys.executable, str(BASE_DIR / "scripts/p3_greenblatt_magic_formula.py")], check=True)
    subprocess.run([sys.executable, str(BASE_DIR / "scripts/a4_auditor_dcf_excel.py")], check=True)

    a1 = generate_a1_synthetic_itr_release()
    a2 = generate_a2_synthetic_earnings_calls()
    a3 = generate_a3_synthetic_scenarios_short()
    radar = generate_p5_p6_a5_synthetic_radar_cowork()

    print(f"[E2E-A1] ITR vs Release Sintético gerado: {a1.name}")
    print(f"[E2E-A2] Teleconferências Sintéticas geradas: {a2.name}")
    print(f"[E2E-A3] 3 Cenários + Short Thesis gerados: {a3.name}")
    print(f"[E2E-A5/P5/P6] Radar Semanal & Pasta Cowork gerados: {radar.name} ({len(list(FATOS_DIR.glob('*.txt')))} comunicados locais)")
    print("=================================================================")


if __name__ == "__main__":
    main()

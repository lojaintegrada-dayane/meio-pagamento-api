from fastapi import FastAPI, UploadFile
import pandas as pd
from datetime import datetime

app = FastAPI()

@app.post("/recomendar")
async def recomendar(file: UploadFile):
    df = pd.read_csv(file.file)

    resultados = []
    for row in df.itertuples():
        if row.taxa_aprovacao < 0.8:
            resultados.append({
                "Data da Análise": datetime.today().strftime("%d/%m/%Y"),
                "ID da Loja": row.loja_id,
                "Nome da Loja": "",
                "Segmento": row.desc_segmento,
                "Plano": row.desc_plano_atual,
                "Email de Contato": "",
                "Player Atual": row.player_pagamento,
                "Player Recomendado": "PAYPAL",
                "Taxa de Aprovação Atual": round(row.taxa_aprovacao * 100, 2),
                "Taxa Média do Segmento": 85.0,
                "Ganho Potencial": 1340.50,
                "Motivo da Troca": "Melhor taxa de aprovação no segmento",
                "Assunto do Email": "Aumente seu faturamento com cartão de crédito",
                "Status de Envio": "Pendente"
            })

    return resultados

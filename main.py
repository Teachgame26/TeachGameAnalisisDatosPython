from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {
        "mensaje": "API funcionando"
    }

@app.get("/api/interno/datos-limpios")
def entregar_headless():
    df = pd.DataFrame([{"id": 1, "valor": 50}])

    # Retorno estricto orientado a filas (headless JSON payload)
    return {
        "status": "ok",
        "payload": df.to_dict(orient="records")
    }



    
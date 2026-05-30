from fastapi import FastAPI
from fastapi.responses import FileResponse
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

    return {
        "status": "ok",
        "payload": df.to_dict(orient="records")
    }

@app.get("/imagen")
def obtener_imagen():
    return FileResponse(
        "data/reports/reporte_impresion.png",
        media_type="image/png"
    )



    
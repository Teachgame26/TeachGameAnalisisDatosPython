from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
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

@app.get("/debug")
def debug():

    base = Path(__file__).parent

    return {
        "base": str(base),
        "data": (base / "data").exists(),
        "reports": (base / "data" / "reports").exists(),
        "png": (base / "data" / "reports" / "reporte_impresion.png").exists()
    }

@app.get("/imagen")
def obtener_imagen():

    ruta = Path(__file__).parent / "data" / "reports" / "reporte_impresion.png"

    return FileResponse(
        str(ruta),
        media_type="image/png"
    )


    
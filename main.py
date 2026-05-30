from pathlib import Path

@app.get("/debug")
def debug():
    base = Path(__file__).parent

    return {
        "main_py": str(base),
        "existe_data": (base / "data").exists(),
        "existe_reports": (base / "data" / "reports").exists(),
        "existe_png": (base / "data" / "reports" / "reporte_impresion.png").exists()
    }



    
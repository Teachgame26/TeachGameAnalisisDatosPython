import pandas as pd

def cargar_datos(ruta):
    """Carga un archivo CSV en un DataFrame"""
    return pd.read_csv(ruta)

def manejar_valores_nulos(df):
    """Elimina filas con valores nulos"""
    return df.dropna()

def estandarizar_texto(df, columnas):
    """Convierte texto a minúsculas y elimina espacios"""
    for col in columnas:
        df[col] = df[col].str.lower().str.strip()
    return df

def validar_notas(df):
    """Mantiene solo notas válidas entre 0 y 5"""
    df = df[df["nota"] >= 0]
    df = df[df["nota"] <= 5]
    return df

def eliminar_duplicados(df, columna_id):
    """Elimina registros duplicados"""
    return df.drop_duplicates(subset=columna_id)



import pandas as pd

# 🔹 Importar funciones desde tu archivo limpieza.py
from src.limpieza import (
    cargar_datos,
    manejar_valores_nulos,
    estandarizar_texto,
    eliminar_duplicados,
    validar_notas
)

# 1️⃣ Cargar datos
estudiantes = cargar_datos("data/estudiantes.csv")
calificaciones = cargar_datos("data/calificaciones.csv")

# 2️⃣ Limpieza de estudiantes
estudiantes = manejar_valores_nulos(estudiantes)
estudiantes = estandarizar_texto(estudiantes, ["nombre", "grado"])
estudiantes = eliminar_duplicados(estudiantes, "id_estudiante")

# 3️⃣ Limpieza de calificaciones
calificaciones = manejar_valores_nulos(calificaciones)
calificaciones = estandarizar_texto(calificaciones, ["materia", "juego"])
calificaciones = validar_notas(calificaciones)

# 4️⃣ Unir tablas
df = calificaciones.merge(estudiantes, on="id_estudiante")

print("\n📊 DATOS LIMPIOS Y UNIFICADOS")
print(df.head())

# 5️⃣ Análisis de Frecuencia
estudiante_mas_juegos = df["nombre"].value_counts().idxmax()
print(f"\n✅ Estudiante con más participaciones: {estudiante_mas_juegos}")

# 6️⃣ Análisis de Agregación
promedio_por_materia = df.groupby("materia")["nota"].mean()
print("\n✅ Nota promedio por materia:")
print(promedio_por_materia)

# 7️⃣ Filtrado y Conteo
aprobados_matematicas = df[
    (df["materia"] == "matemáticas") & (df["nota"] >= 3)
]

print(f"\n✅ Estudiantes que aprobaron Matemáticas: {len(aprobados_matematicas)}")





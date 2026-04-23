from src.limpieza import (
	cargar_datos,
	manejar_valores_nulos,
	estandarizar_texto,
	validar_notas,
	eliminar_duplicados
)

# 1. Cargar datos
estudiantes = src.limpieza.cargar_datos("data/estudiantes.csv")
calificaciones = src.limpieza.cargar_datos("data/calificaciones.csv")

# 1. Análisis de Frecuencia
estudiante_mas_juegos = df["nombre"].value_counts().idxmax()
print(f"\n✅ Estudiante con más participaciones en juegos: {estudiante_mas_juegos}")

# 2. Análisis de Agregación
promedio_por_materia = df.groupby("materia")["nota"].mean()
print("\n✅ Nota promedio por materia:")
print(promedio_por_materia)




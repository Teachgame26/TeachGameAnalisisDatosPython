# TeachGame – Análisis de Evaluación de Estudiantes por Juegos

TeachGame es un proyecto académico de análisis de datos desarrollado en Python, cuyo objetivo es analizar la evaluación de estudiantes por materia a través de juegos educativos.  
Los datos utilizados contienen errores reales (valores nulos, duplicados e inconsistencias), por lo que se implementa un proceso completo de limpieza y análisis usando Pandas y buenas prácticas de desarrollo con Git Flow.

---

## Objetivo del Proyecto

- Simular un sistema donde los **profesores califican a los estudiantes mediante juegos educativos**.
- Limpiar y preparar datos con problemas reales.
- Realizar análisis de filtrado.
- Aplicar control de versiones usando **Git Flow**.
- Responder preguntas clave sobre el desempeño académico.

---

## Funcionamiento General

1. Se cargan los archivos de datos (`estudiantes.csv` y `calificaciones.csv`).
2. Se limpian los datos:
   - Eliminación de valores nulos
   - Corrección de texto (minúsculas y espacios)
   - Eliminación de registros duplicados
   - Validación de notas (rango 0 a 5)
3. Se unen los datos usando un `merge`.
4. Se realizan análisis para responder:
   - ¿Qué estudiante participa más en los juegos?
   - ¿Cuál es el promedio de notas por materia?
   - ¿Cuántos estudiantes aprobaron matemáticas?

---

## Estructura del Proyecto


AnalisisDatosPython/
│
├── data/
│   ├── estudiantes.csv        # Información de estudiantes
│   └── calificaciones.csv     # Resultados de juegos y notas
│
├── src/
│   ├── __init__.py
│   └── limpieza.py            # Funciones de limpieza de datos
│
├── analisis.py                # Script principal de análisis
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Archivos ignorados por Git
└── README.md                  # Documentación del proyecto


## Tecnologías
- Python
- Pandas
- Git / Git Flow

## Instalación
python -m venv venv
source venv/Scripts/Activate
pip install -r requirements.txt

## Ejecución

python analisis.py

## Autores
- Mayerlin Cubides
- Paola Arismendy
- Johana Peña


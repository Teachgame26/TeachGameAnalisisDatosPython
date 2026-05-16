# Importaciones necesarias
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://6a08c3ade7e3f433d482d2ba.mockapi.io/Notas/api/doc/Notasporestudiante"
response = requests.get(url)
# 1. Verificamos si la petición fue exitosa
if response.status_code == 200:
    # 2. Si lo fue, extraemos el contenido JSON
    datos = response.json()
    print("¡Petición exitosa!")
    print("Tipo de datos recibidos:", type(datos))
    print("Contenido:", datos)
    # A partir de aquí, cargamos 'datos' en un DataFrame de Pandas y procesamos
    df = pd.DataFrame(datos)
    print(df)
    df.info()
    df['nota'] = df['nota'].astype('float64')
    df.info()

    # 1. Preparar el lienzo (Ancho, Alto en pulgadas)
    plt.figure(figsize=(10, 6))

    colores=['blue', 'red', 'orange', 'yellow']
    # 2. Pintar el gráfico (usando la integración directa de Pandas)
    df.plot(kind='bar', x='estudiante', y='nota', color='blue')
    # 3. Personalización y Contexto (Metadata)
    plt.title("Notas por estudiante", fontsize=14)
    plt.xlabel("Nombre Estudiantes")
    plt.ylabel("Notas")
    plt.xticks(rotation=45) # Rotar textos para que no colisionen

    # Asegurar que exista la carpeta de reportes antes de guardar
    import os
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    reports_dir = os.path.join(base_dir, 'data', 'reports')
    os.makedirs(reports_dir, exist_ok=True)

    plt.savefig(os.path.join(reports_dir, 'reporte_impresion.png'), format='png', dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(reports_dir, 'reporte_web.svg'), format='svg', bbox_inches='tight')
    plt.savefig(os.path.join(reports_dir, 'reporte_ejecutivo.pdf'), format='pdf', bbox_inches='tight')

    # 4. Renderizar (Mostrar a pantalla)
    plt.show()
else:
    print(f"Error al hacer la petición. Código de estado: {response.status_code}")

# Opción A: PNG (Rasterizado / Mapa de Bits)
# Ideal para: PowerPoint, Word, correos electrónicos o impresión física.
# Parámetro técnico: dpi=300 (Puntos por pulgada). Es el estándar internacional 
# para calidad de imprenta. Si omites el DPI, se guardará a 72 o 100 DPI (se verá borroso).
#plt.savefig("reporte_impresion.png", format='png', dpi=300, bbox_inches='tight')

# Opción B: SVG (Vectorial / Matemático)
# Ideal para: Páginas web, aplicaciones interactivas o diseño gráfico (Illustrator/Figma).
# No usa DPI porque no está hecho de píxeles, sino de fórmulas matemáticas. 
# Puedes hacerle zoom infinito sin que se pixele.
#plt.savefig("reporte_web.svg", format='svg', bbox_inches='tight')

# Opción C: PDF (Vectorial Empaquetado)
# Ideal para: Informes formales, adjuntos gerenciales o entregables académicos.
# Al igual que el SVG, el PDF guarda los gráficos de forma vectorial, garantizando
# texto nítido sin importar cuánto zoom haga el gerente.
#plt.savefig("reporte_ejecutivo.pdf", format='pdf', bbox_inches='tight')


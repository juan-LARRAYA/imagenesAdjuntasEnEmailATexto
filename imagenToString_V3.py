import os
from PIL import Image
import pytesseract

# Configuración del modelo
USAR_TESSERACT = True

def imagen_a_texto_tesseract(ruta_imagen):
    """
    Convierte una imagen a texto usando Tesseract OCR.

    Parámetros:
    ruta_imagen (str): Ruta de la imagen que se va a procesar.

    Retorna:
    str: Texto extraído de la imagen.
    """
    try:
        imagen = Image.open(ruta_imagen)
        texto = pytesseract.image_to_string(imagen)
        return texto
    except Exception as e:
        print(f"Error al procesar {ruta_imagen} con Tesseract: {e}")
        return ""

def imagen_a_texto(ruta_imagen):
    """
    Selecciona el método de OCR a utilizar.

    Parámetros:
    ruta_imagen (str): Ruta de la imagen que se va a procesar.

    Retorna:
    str: Texto extraído de la imagen.
    """
    if USAR_TESSERACT:
        return imagen_a_texto_tesseract(ruta_imagen)
    else:
        return ""

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = "/Users/apple/Desktop/programador/aDesarrollar/imagenesAdjuntasEnEmailATexto/imagenes"

# Ruta de la carpeta para guardar los archivos de texto resultantes
carpeta_resultados = "/Users/apple/Desktop/programador/aDesarrollar/imagenesAdjuntasEnEmailATexto/resultados"
os.makedirs(carpeta_resultados, exist_ok=True)

# Ruta al archivo de texto consolidado
archivo_consolidado = "/Users/apple/Desktop/programador/aDesarrollar/imagenesAdjuntasEnEmailATexto/archivo_consolidado.txt"

# Procesar todas las imágenes en la carpeta
for nombre_archivo in os.listdir(carpeta_imagenes):
    ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
    if os.path.isfile(ruta_imagen):
        texto_extraido = imagen_a_texto(ruta_imagen)
        print(f"Texto extraído de {nombre_archivo}:\n{texto_extraido}\n")

        # Guardar el texto extraído en un archivo de texto
        nombre_archivo_texto = os.path.splitext(nombre_archivo)[0] + ".txt"
        ruta_archivo_texto = os.path.join(carpeta_resultados, nombre_archivo_texto)
        with open(ruta_archivo_texto, "w", encoding="utf-8") as archivo_texto:
            archivo_texto.write(texto_extraido)

# Abrir archivo de texto consolidado para escritura
with open(archivo_consolidado, 'w', encoding='utf-8') as archivo_txt:
    # Recorrer todos los archivos en la carpeta
    for nombre_archivo in os.listdir(carpeta_imagenes):
        if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)

            # Convertir imagen a texto
            texto = imagen_a_texto(ruta_imagen)

            # Si está la palabra "cliente", filtra el texto para incluir solo lo que aparece después
            if 'cliente' in texto.lower():
                # Encuentra la posición de la palabra "cliente" y extrae el texto después
                texto = texto.lower().split('cliente', 1)[-1].strip()

            # Escribir el texto filtrado en el archivo consolidado
            archivo_txt.write(f"Texto de {nombre_archivo}:\n")
            archivo_txt.write(texto + "\n")

            archivo_txt.write("\n--------------------\n")
print(f"Archivo consolidado creado en {archivo_consolidado}.")

import os
from PIL import Image
import pytesseract

# Función para convertir imagen a texto
def imagen_a_texto(ruta_imagen):
    try:
        # Abrir la imagen con PIL
        imagen = Image.open(ruta_imagen)
        # Usar pytesseract para extraer el texto
        texto = pytesseract.image_to_string(imagen)
        return texto
    except Exception as e:
        print(f"Error al procesar {ruta_imagen}: {e}")
        return ""

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = r"C:\Users\RutaATusImagenes"

# Ruta de la carpeta para guardar los archivos de texto resultantes
carpeta_resultados = r"C:\Users\RutaAResultados"
os.makedirs(carpeta_resultados, exist_ok=True)

# Ruta al archivo de texto consolidado
archivo_consolidado = r"C:\Users\RutaAArchivo_consolidado.txt"

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
            
            # Abrir imagen
            imagen = Image.open(ruta_imagen)
            
            # Convertir imagen a texto
            texto = pytesseract.image_to_string(imagen)
            
            # Filtrar el texto para incluir solo lo que aparece después de la palabra "cliente"
            if 'cliente' in texto.lower():
                # Encuentra la posición de la palabra "cliente" y extrae el texto después
                texto_posterior = texto.lower().split('cliente', 1)[-1].strip()
                
                # Escribir el texto filtrado en el archivo consolidado
                archivo_txt.write(f"Texto de {nombre_archivo}:\n")
                archivo_txt.write(texto_posterior + "\n")
                archivo_txt.write("\n--------------------\n")

print(f"Archivo consolidado creado en {archivo_consolidado}.")
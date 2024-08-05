# Imágenes Adjuntas en Email a Texto

Este proyecto proporciona un script que convierte el texto de múltiples imágenes en un archivo de texto. Cada una de estas imágenes contiene información sobre la fecha, el cliente y el artículo. Al convertir estas imágenes a texto, podemos automatizar la gestión de materiales recibidos para cada proyecto y determinar cuáles están pendientes de recepción y compra.

## Descripción

Este script permite extraer y procesar información de imágenes que contienen datos de proyectos. Cada imagen tiene la siguiente información:
- **Fecha**
- **Cliente**
- **Artículo**

La salida del script es un archivo `.txt` que organiza esta información para su fácil consulta y gestión.

## Funcionalidades

- Extraer texto de imágenes utilizando OCR (Reconocimiento Óptico de Caracteres).
- Procesar y organizar la información en un formato estructurado.
- Generar un archivo de texto consolidado con la información de todas las imágenes.

## Requisitos

- Python 3.x
- Bibliotecas de Python: `pytesseract`, `Pillow`

### Instalación de bibliotecas necesarias

```bash
pip install pytesseract Pillow
```


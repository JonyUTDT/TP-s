import numpy as np                  
from PIL import Image  # Permite abrir, modificar y guardar imágenes en distintos formatos               
import os  # Permite crear carpetas, listar archivos y manejar rutas en el sistema operativo  

carpeta_healty = "DatasetTP/Healthy"
carpeta_comprimida_healthy = "Healthy_comprimido"

carpeta_parkinson = "DatasetTP/Parkinson"
carpeta_comprimida_parkinson = "Parkinson_comprimido"

# Crear la carpeta comprimida de healthy si no existe
if not os.path.exists(carpeta_comprimida_healthy):
    os.makedirs(carpeta_comprimida_healthy)

# Crear la carpeta comprimida de parkinson si no existe
if not os.path.exists(carpeta_comprimida_parkinson):
    os.makedirs(carpeta_comprimida_parkinson)

# Pedimos al usuario el nuevo tamaño
ancho = int(input("Ingrese el nuevo ancho de las imágenes: "))
alto = int(input("Ingrese el nuevo alto de las imágenes: "))

# Procesamos las imágenes en la carpeta Healthy y las guardamos en la carpeta comprimida Healthy
for imagen in os.listdir(carpeta_healty):
    if not imagen.lower().endswith('.png'): # Verificamos que sea un archivo PNG, sino lo salteamos
        continue
    
    ruta_imagen = os.path.join(carpeta_healty, imagen) 
    imagen_original = Image.open(ruta_imagen).convert("L") 
    imagen_redimensionada = imagen_original.resize((ancho, alto), Image.LANCZOS) # Comprimimos la imagen al nuevo tamaño
    
    # Guardar la imagen redimensionada en la carpeta de imagenes comprimidas con el mismo nombre
    ruta_guardado = os.path.join(carpeta_comprimida_healthy, imagen) # Creamos la ruta de guardado en la carpeta comprimida
    imagen_redimensionada.save(ruta_guardado) # # Guardamos la imagen comprimida en la carpeta de imagenes comprimidas correspondiente

print(f"Se comprimieron y guardaron las imágenes en '{carpeta_comprimida_healthy}'.")

for imagen in os.listdir(carpeta_parkinson):
    if not imagen.lower().endswith('.png'): 
        continue
    
    ruta_imagen = os.path.join(carpeta_parkinson, imagen)
    imagen_original = Image.open(ruta_imagen).convert("L")
    imagen_redimensionada = imagen_original.resize((ancho, alto), Image.LANCZOS) 
    
    # Guardar la imagen redimensionada en la carpeta de imagenes comprimidas con el mismo nombre
    ruta_guardado = os.path.join(carpeta_comprimida_parkinson, imagen)
    imagen_redimensionada.save(ruta_guardado)

print(f"Se comprimieron y guardaron las imágenes en '{carpeta_comprimida_parkinson}'.")

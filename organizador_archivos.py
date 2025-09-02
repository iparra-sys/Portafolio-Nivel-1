import os
import shutil

# Carpeta que quieres organizar
carpeta = "C:/Usuarios/TuUsuario/Descargas"  # Cambia a tu ruta
# Tipos de archivos y carpetas destino
tipos = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Música": [".mp3", ".wav"],
}

# Crear carpetas si no existen
for carpeta_destino in tipos.keys():
    ruta = os.path.join(carpeta, carpeta_destino)
    if not os.path.exists(ruta):
        os.makedirs(ruta)

# Mover archivos a sus carpetas
for archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta_archivo):
        for carpeta_destino, extensiones in tipos.items():
            if archivo.lower().endswith(tuple(extensiones)):
                shutil.move(ruta_archivo, os.path.join(carpeta, carpeta_destino))
                print(f"{archivo} movido a {carpeta_destino}")

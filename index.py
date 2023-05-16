from PIL import Image
import os

# Abre la imagen
image = Image.open('Moda.png')

# Define el nivel de calidad de la compresión (0 a 100)
quality = 50

# Guarda la imagen comprimida en un archivo temporal
tmp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)
tmp_file = os.path.join(tmp_path, 'mi_imagen_comprimida.jpg')
image.save(tmp_file, optimize=True, quality=quality)

# Lee el archivo comprimido y guárdalo en un nuevo archivo
with open(tmp_file, 'rb') as f:
    compressed_data = f.read()
new_file = 'mi_imagen_comprimida.jpg'
with open(new_file, 'wb') as f:
    f.write(compressed_data)

# Elimina el archivo temporal
os.remove(tmp_file)
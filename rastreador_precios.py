import requests
from bs4 import BeautifulSoup

# URL del producto (ejemplo)
url = "https://articulo.mercadolibre.com.co/MLC-1234567890-ejemplo-producto"

# Hacer request a la página
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Buscar precio (selector simple, puede variar según la página)
precio = soup.find("span", class_="price-tag-fraction")  # Ajustar si cambia el HTML
if precio:
    print(f"El precio actual es: ${precio.text}")
else:
    print("No se pudo encontrar el precio")

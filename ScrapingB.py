# Importar las librerías necesarias
import requests
import random
import time
from bs4 import BeautifulSoup


# Función para realizar la solicitud GET a la URL y obtener la página HTML
def get_html(url):
    # Agregar un tiempo de espera aleatorio para evitar ser bloqueado por el servidor
    time.sleep(random.uniform(1, 5))
    # Enviar una solicitud GET a la URL especificada
    response = requests.get(url)
    # Verificar si la respuesta es exitosa
    if response.status_code == 200:
        # Devolver el código HTML de la página
        return response.text
    else:
        # Devolver una cadena vacía si la respuesta no es exitosa
        return ""

# Función para extraer los datos necesarios de la página HTML
def extract_data(html):
    # Crear un objeto BeautifulSoup a partir de la página HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Buscar todos los elementos con la clase especificada
    items = soup.find_all(class_="vtex-search-result-3-x-galleryItem")                            ###ESTA LINEA DEBE SER MODIFICADA POR EL USUARIO
    # Inicializar una lista para almacenar los datos extraídos
    data = []
    # Iterar sobre cada elemento
    for item in items:
        # Extraer el título y el precio de cada elemento
        title = item.find(class_="vtex-product-summary-2-x-productBrand").text.strip()               ###ESTA LINEA DEBE SER MODIFICADA POR EL USUARIO
        price = item.find(class_="vtex-store-components-3-x-currencyContainer").text.strip()               ###ESTA LINEA DEBE SER MODIFICADA POR EL USUARIO
        # Agregar un diccionario con los datos extraídos a la lista
        data.append({"title": title, "price": price})
    # Devolver la lista de datos extraídos
    return data

# URL a la que se realizará la solicitud GET
url = "https://www.walmart.com.sv/electronica"               ###ESTA LINEA DEBE SER MODIFICADA POR EL USUARIO

# Obtener la página HTML
html = get_html(url)

# Extraer los datos necesarios de la página HTML
data = extract_data(html)

# Imprimir los datos extraídos
print(data)

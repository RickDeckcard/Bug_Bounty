import urllib.request
import json

try:
    # Consultamos un servicio público que devuelve la IP en formato JSON
    with urllib.request.urlopen('https://api.ipify.org?format=json') as response:
        data = json.loads(response.read().decode())
        print("Tu IP pública es:", data['ip'])
except Exception as e:
    print("Error al obtener la IP:", str(e))

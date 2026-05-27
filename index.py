import urllib.request
import json
import sys

print("=== Detectando IP Pública ===")

esquemas = [
    {'url': 'https://api.ipify.org?format=json', 'key': 'ip'},
    {'url': 'https://ipinfo.io/json', 'key': 'ip'},
    {'url': 'https://ifconfig.me/all.json', 'key': 'ip_addr'}
]

ip_encontrada = False

for esquema in esquemas:
    try:
        # Configuramos un User-Agent para evitar que el servicio bloquee la petición
        req = urllib.request.Request(
            esquema['url'], 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            print(f"Tu IP pública es: {data[esquema['key']]}")
            ip_encontrada = True
            break # Si funciona uno, salimos del bucle
            
    except Exception:
        continue # Si un servicio falla, intenta con el siguiente

if not ip_encontrada:
    print("Error: No se pudo determinar la IP pública. Verifica tu conexión a internet.")

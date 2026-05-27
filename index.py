import urllib.request

url = 'https://api.github.com/zen' # Usamos /zen porque consume poquísimos recursos

try:
    # Creamos la petición a un dominio permitido
    req = urllib.request.Request(url)
    
    with urllib.request.urlopen(req) as response:
        # Buscamos en los encabezados de respuesta
        headers = response.info()
        
        # El encabezado 'X-Client-IP' o 'Client-IP' suele reflejar la IP de origen
        ip_publica = headers.get('X-Client-IP') or headers.get('Client-IP')
        
        if ip_publica:
            print("Tu IP pública (detectada vía GitHub) es:", ip_publica)
        else:
            # Si GitHub oculta el header directo, podemos ver los resolvers intermedios
            forwarded = headers.get('X-Forwarded-For')
            if forwarded:
                # La primera IP de la lista suele ser la tuya real
                tu_ip = forwarded.split(',')[0].strip()
                print("Tu IP pública (vía Forwarded) es:", tu_ip)
            else:
                print("GitHub aceptó la petición, pero no expuso la IP en los headers comunes.")
                # Opcional: Descomenta la línea de abajo para auditar todos los headers recibidos
                # print(headers)

except Exception as e:
    print("Error al conectar con el dominio permitido:", str(e))

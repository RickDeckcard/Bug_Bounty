import urllib.request

# Usamos el dominio de contenido RAW que está permitido y no tiene el límite de la API
url = 'https://raw.githubusercontent.com/RickDeckcard/Bug_Bounty/main/no_existo_404'

try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
    except urllib.error.HTTPError as e:
        # Aprovechamos el error (404) porque los headers de error también viajan con la info
        headers = e.headers

    # Evaluamos los encabezados devueltos por la infraestructura de red de GitHub
    ip_publica = (
        headers.get('X-Client-IP') or 
        headers.get('Client-IP') or 
        headers.get('X-Forwarded-For') or
        headers.get('Fastly-Client-IP') # GitHub usa Fastly en su infraestructura CDN
    )

    if ip_publica:
        # X-Forwarded-For puede traer una cadena de IPs; nos quedamos con la primera
        print("Tu IP pública es:", ip_publica.split(',')[0].strip())
    else:
        print("El servidor respondió, pero la infraestructura ocultó la IP.")
        print("Headers disponibles para inspección:\n", headers)

except Exception as e:
    print("Error de conexión:", str(e))

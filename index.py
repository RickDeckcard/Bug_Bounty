import urllib.request

# Lista de alternativas usando tus dominios permitidos (provocando un 404 a propósito)
urls_alternativas = [
    'https://pypi.org/un_archivo_que_no_existe_404',
    'http://archive.ubuntu.com/un_archivo_que_no_existe_404',
    'https://api.anthropic.com/v1/endpoints_inventado'
]

ip_encontrada = False

for url in urls_alternativas:
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                headers = response.info()
        except urllib.error.HTTPError as e:
            # Capturamos los headers del error (404, 403, etc.)
            headers = e.headers

        # Buscamos las cabeceras donde las CDNs suelen reflejar la IP origen
        ip_publica = (
            headers.get('X-Client-IP') or 
            headers.get('Client-IP') or 
            headers.get('X-Forwarded-For') or
            headers.get('Fastly-Client-IP') or
            headers.get('CF-Connecting-IP') # Para dominios que usen Cloudflare
        )

        if ip_publica:
            print(f"Tu IP pública es: {ip_publica.split(',')[0].strip()}")
            ip_encontrada = True
            break # IP encontrada con éxito, salimos del bucle
            
    except Exception:
        continue # Si este dominio falla por completo, pasa al siguiente

if not ip_encontrada:
    print("No se pudo obtener la IP a través de los métodos alternativos.")
    print("Es probable que tu proxy local esté eliminando las cabeceras de depuración.")

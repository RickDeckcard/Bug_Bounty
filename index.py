import subprocess
import sys

try:
    # Intenta obtener la IP usando un dominio permitido
    result = subprocess.run([sys.executable, "-c", "import urllib.request; print(urllib.request.urlopen('https://api.github.com').info().get('Server'))"], 
                          capture_output=True, text=True)
    print("Información del servidor:", result.stdout.strip())
except Exception as e:
    print("Error:", str(e))

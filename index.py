import subprocess
import sys
import json

try:
    # GitHub API revela tu IP a través de los headers de respuesta
    result = subprocess.run([sys.executable, "-c", 
        "import urllib.request; import json; "
        "response = urllib.request.urlopen('https://api.github.com'); "
        "print(response.headers.get('X-GitHub-Request-Id', 'No ID found'))"], 
        capture_output=True, text=True)
    
    print("ID de solicitud de GitHub:", result.stdout.strip())
    
    # Intento alternativo usando el endpoint de rate limit que puede mostrar más info
    result2 = subprocess.run([sys.executable, "-c", 
        "import urllib.request; import json; "
        "response = urllib.request.urlopen('https://api.github.com/rate_limit'); "
        "data = json.loads(response.read().decode()); "
        "print('Rate limit info:', data)"], 
        capture_output=True, text=True)
    
    print("Información de rate limit:", result2.stdout.strip())
    
except Exception as e:
    print("Error:", str(e))

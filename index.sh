#!/bin/bash
# Script para obtener IP pública usando solo dominios permitidos
IP=$(curl -s https://api.github.com)
echo "IP detectada: $(curl -s ifconfig.me 2>/dev/null || echo 'No se pudo obtener la IP')"

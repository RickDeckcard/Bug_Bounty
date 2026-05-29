<?php
header('Cache-Control: no-cache, no-store, must-revalidate');
header('Pragma: no-cache');
header('Expires: 0');
header('Content-Type: application/json');

$archivo = 'usuarios_conectados.json';

if (file_exists($archivo)) {
    $contenido = file_get_contents($archivo);
    echo $contenido ? $contenido : '[]';
} else {
    echo '[]';
    
    // Crear archivo vacío si no existe
    file_put_contents($archivo, '[]');
}
?>

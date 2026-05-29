<?php
header('Cache-Control: no-cache, no-store, must-revalidate');
header('Content-Type: application/json');

$input = file_get_contents('php://input');
$data = json_decode($input, true);

if (!$data || empty($data['usuario'])) {
    echo json_encode(['status' => 'error', 'mensaje' => 'Datos inválidos']);
    exit;
}

$archivo = 'usuarios_conectados.json';

$usuarios = [];
if (file_exists($archivo)) {
    $usuarios = json_decode(file_get_contents($archivo), true) ?? [];
}

$usuarios[] = [
    'usuario' => htmlspecialchars($data['usuario']),
    'ip'      => $data['ip'] ?? 'N/A',
    'hora'    => $data['hora'] ?? date('Y-m-d H:i:s'),
    'timestamp' => time()
];

// Mantener solo los últimos 20 registros
if (count($usuarios) > 20) {
    $usuarios = array_slice($usuarios, -20);
}

file_put_contents($archivo, json_encode($usuarios, JSON_UNESCAPED_UNICODE));

echo json_encode(['status' => 'ok']);
?>

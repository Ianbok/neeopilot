#!/bin/bash

# Cambiar al directorio del proyecto
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Verificar que estamos en el directorio correcto
if [ ! -f "frontend/package.json" ] || [ ! -d "backend" ]; then
    echo "❌ Error: No se encontró la estructura del proyecto NeoPilot"
    echo "💡 Asegúrate de que existen las carpetas frontend/ y backend/"
    exit 1
fi

# Verificar/crear entorno virtual
if [ ! -d "venv" ]; then
    python3 -m venv venv &>/dev/null
    if [ $? -ne 0 ]; then
        echo "❌ Error creando entorno virtual"
        exit 1
    fi
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar/actualizar dependencias Python
pip install --upgrade pip &>/dev/null
pip install PyQt5 PyQtWebEngine &>/dev/null

if [ $? -ne 0 ]; then
    echo "❌ Error instalando PyQt5. Verifica tu instalación de Python"
    exit 1
fi

# Verificar frontend compilado
if [ ! -d "frontend/build" ]; then
    # Verificar Node.js
    if ! command -v npm &> /dev/null; then
        echo "❌ Error: Node.js/npm no está instalado"
        echo "💡 Instala Node.js: sudo apt install nodejs npm"
        exit 1
    fi
    
    # Instalar dependencias de frontend
    cd frontend
    npm install &>/dev/null
    
    # Compilar frontend
    npm run build &>/dev/null
    cd ..
    
    if [ ! -d "frontend/build" ]; then
        echo "❌ Error: No se pudo compilar el frontend"
        exit 1
    fi
fi

# Limpiar variables de entorno problemáticas (snap conflicts)
unset SNAP
unset SNAP_DESKTOP_RUNTIME

# Función de limpieza al salir
cleanup() {
    pkill -f "server_web.py" 2>/dev/null || true
    pkill -f "kiosk_launcher.py" 2>/dev/null || true
    exit 0
}

# Configurar manejadores de señales
trap cleanup SIGINT SIGTERM

# Ejecutar el launcher de kiosko
python backend/kiosk_launcher.py

# Cleanup al finalizar
cleanup

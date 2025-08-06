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

# Verificar si estamos en Raspberry Pi
if [[ $(uname -m) != arm* ]] && [[ $(uname -m) != aarch64 ]]; then
    echo "⚠️  Advertencia: No se detectó arquitectura ARM (Raspberry Pi)"
    echo "💡 Para Ubuntu usa: ./run-ubuntu.sh"
    read -p "¿Continuar de todos modos? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Verificar dependencias de sistema en Raspberry Pi
if ! python3 -c "import PyQt5" 2>/dev/null; then
    echo "❌ PyQt5 no disponible en el sistema"
    echo "💡 Instala con: sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine"
    exit 1
fi

# Verificar frontend compilado
if [ ! -d "frontend/build" ]; then
    echo "❌ Frontend no compilado"
    echo "💡 Compila en tu PC de desarrollo y transfiere el proyecto completo"
    echo "💡 O instala Node.js en Raspberry Pi: sudo apt install nodejs npm"
    exit 1
fi

# Configurar entorno para Raspberry Pi
export QT_QPA_PLATFORM=xcb
export DISPLAY=:0

# Función de limpieza al salir
cleanup() {
    pkill -f "server_web.py" 2>/dev/null || true
    pkill -f "kiosk_launcher.py" 2>/dev/null || true
    exit 0
}

# Configurar manejadores de señales
trap cleanup SIGINT SIGTERM

# Ejecutar el launcher de kiosko
python3 backend/kiosk_launcher.py

# Cleanup al finalizar
cleanup

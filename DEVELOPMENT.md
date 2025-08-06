# NeeOPiloT - Guía de Desarrollo

## Configuración del Entorno

### Requisitos
- Python 3.8+
- Node.js 16+
- PyQt5
- Sistema Linux (preferiblemente Raspberry Pi OS)

### Instalación
```bash
# Configurar entorno de desarrollo
./setup-dev.sh

# O manualmente:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd frontend
npm install
npm run build
```

## Desarrollo

### Ejecutar en modo desarrollo
```bash
./run-dev.sh
```

### Construir solo el frontend
```bash
./build-frontend.sh
```

### Probar backend
```bash
./test-backend.sh
```

## Estructura del Proyecto

### Backend (`backend/`)
- `main.py` - Aplicación principal Qt
- `app_launcher.py` - Sistema de lanzamiento de apps
- `websocket_server.py` - Servidor WebSocket para comunicación tiempo real

### Frontend (`frontend/src/`)
- `components/AppStore.jsx` - Interfaz básica de apps
- `components/AppStoreEnhanced.jsx` - Interfaz con WebSocket
- `hooks/useWebSocket.js` - Hook para comunicación WebSocket

## API WebSocket

### Mensajes del Cliente al Servidor
```json
// Lanzar app
{"type": "launch_app", "data": {"app_id": "waze"}}

// Cerrar app
{"type": "close_app", "data": {"app_id": "waze", "force": false}}

// Obtener estado
{"type": "get_status", "data": {}}
```

### Mensajes del Servidor al Cliente
```json
// App lanzada
{"type": "app_launched", "data": {"app_id": "waze", "pid": 1234}}

// App cerrada
{"type": "app_closed", "data": {"app_id": "waze", "exit_code": 0}}

// Error en app
{"type": "app_error", "data": {"app_id": "waze", "error": "mensaje"}}
```

## Comandos VS Code

- **Ctrl+Shift+P** → "Tasks: Run Task" → "Ejecutar Desarrollo"
- **F5** → Debug Backend
- **Ctrl+Shift+P** → "Tasks: Run Task" → "Construir Frontend"

## Producción

Para instalar en Raspberry Pi:
```bash
sudo ./scripts/setup-autostart.sh
```


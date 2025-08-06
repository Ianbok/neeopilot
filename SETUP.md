# Configuración del Entorno en Otro PC

Esta guía te ayudará a configurar el mismo entorno virtual de NeoPilot en otra computadora.

## 📋 Requisitos del Sistema

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm git
sudo apt install -y python3-pyqt5 qt5-default  # Para PyQt5
```

### Windows
1. Instalar Python 3.8+ desde [python.org](https://python.org)
2. Instalar Node.js desde [nodejs.org](https://nodejs.org)
3. Instalar Git desde [git-scm.com](https://git-scm.com)

### macOS
```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar dependencias
brew install python nodejs git
```

## 🔧 Configuración Paso a Paso

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Ianbok/neeopilot.git
cd neeopilot
```

### 2. Configurar el Backend (Python)

#### Crear entorno virtual
```bash
cd backend
python3 -m venv venv --system-site-packages  # Importante para Raspberry Pi
```

#### Activar entorno virtual
**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

#### Instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configurar el Frontend (React)

```bash
cd ../frontend
npm install
```

### 4. Construir el Frontend

```bash
npm run build
```

## 🚀 Ejecutar la Aplicación

### Opción 1: Usando Scripts (Linux/macOS)
```bash
# Desde la raíz del proyecto
chmod +x run-ubuntu.sh
./run-ubuntu.sh
```

### Opción 2: Manual

#### Terminal 1 - Backend
```bash
cd backend
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows
python main.py
```

#### Terminal 2 - Frontend (opcional para desarrollo)
```bash
cd frontend
npm start
```

## 🛠️ Solución de Problemas

### Error de PyQt5 en Raspberry Pi
Si obtienes el error "PyQt5 no disponible en el sistema":

1. **Instalar PyQt5 a nivel del sistema:**
```bash
sudo apt install -y python3-pyqt5 python3-pyqt5-dev python3-pyqt5.qtwebengine
```

2. **Recrear entorno virtual con acceso al sistema:**
```bash
cd backend
rm -rf venv
python3 -m venv venv --system-site-packages
source venv/bin/activate
pip install -r requirements.txt
```

### Error de PyQt5 en Linux
```bash
sudo apt install -y python3-pyqt5 python3-pyqt5-dev python3-pyqt5.qtwebkit
```

### Error de permisos
```bash
sudo chown -R $USER:$USER /path/to/neeopilot
```

### Error de Node.js/npm
```bash
# Actualizar Node.js a la última versión LTS
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## 📁 Estructura del Proyecto

```
neeopilot/
├── backend/                 # Aplicación Python con PyQt5
│   ├── main.py             # Punto de entrada principal
│   ├── requirements.txt    # Dependencias Python
│   └── venv/              # Entorno virtual (no incluido en git)
├── frontend/               # Aplicación React
│   ├── src/               # Código fuente React
│   ├── build/             # Build de producción
│   └── package.json       # Dependencias Node.js
└── config/                # Configuraciones del sistema
```

## 🔧 Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto si necesitas configuraciones específicas:

```bash
# .env
FLASK_PORT=5000
WEBSOCKET_PORT=8765
DEBUG=False
```

## 📱 Acceso a la Aplicación

Una vez ejecutado:
- La aplicación de kiosko se abrirá automáticamente en pantalla completa
- Interface web disponible en: `http://localhost:5000`
- WebSocket server en: `ws://localhost:8765`

## 🔄 Actualizar el Código

```bash
# Obtener últimos cambios
git pull origin main

# Actualizar dependencias Python
cd backend
source venv/bin/activate
pip install -r requirements.txt

# Actualizar dependencias Node.js
cd ../frontend
npm install
npm run build
```

¡Listo! Tu entorno debería estar funcionando exactamente igual que en la PC original.

# NeoPilot

**Sistema de kiosko en pantalla completa con PyQt5 para Raspberry Pi 5 y Ubuntu**

## 🚀 Descripción

NeoPilot es una aplicación de kiosko desarrollada para ejecutarse en Raspberry Pi 5 con Raspberry Pi OS Lite, pero desarrollable en Ubuntu. Utiliza React.js para el frontend y PyQt5 con QtWebEngine para el modo kiosko en pantalla completa.

## 📁 Estructura del Proyecto

```
neeopilot/
├── frontend/                    # Frontend React.js
│   ├── src/
│   │   ├── components/         # Componentes React
│   │   ├── styles/            # Estilos CSS
│   │   └── App.js             # Componente principal
│   ├── public/                # Archivos públicos
│   └── build/                 # Frontend compilado
├── backend/                   # Backend Python
│   ├── main.py               # Aplicación PyQt5 básica
│   └── kiosk_launcher.py     # Launcher de kiosko con servidor integrado
├── run-ubuntu.sh             # Script para Ubuntu (desarrollo)
├── run-rpi.sh               # Script para Raspberry Pi (producción)
└── README.md                # Este archivo
```

## 🎯 Ejecución

### Ubuntu (Desarrollo)
```bash
./run-ubuntu.sh
```
- Configura entorno virtual automáticamente
- Instala PyQt5 en entorno aislado
- Compila frontend si es necesario
- Ejecuta kiosko en pantalla completa

### Raspberry Pi (Producción)
```bash
./run-rpi.sh
```
- Usa PyQt5 del sistema
- Optimizado para Raspberry Pi OS Lite
- Configuración específica para ARM

## 🔧 Instalación

### Ubuntu (Desarrollo)

1. **Instalar dependencias del sistema:**
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip nodejs npm git
```

2. **Ejecutar directamente:**
```bash
git clone <repository-url> neeopilot
cd neeopilot
./run-ubuntu.sh
```

### Raspberry Pi 5

1. **Preparar Raspberry Pi OS Lite:**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git
sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine
```

2. **Transferir proyecto compilado:**
```bash
# Desde Ubuntu, después de compilar
scp -r neeopilot/ pi@<raspberry-ip>:~/
```

3. **Ejecutar en Raspberry Pi:**
```bash
cd neeopilot
./run-rpi.sh
```

## 🎮 Características del Kiosko

### Modo Kiosko
- **Pantalla completa** sin bordes ni barras de título
- **Sin teclas de escape** (solo Alt+F4 para desarrollo)
- **Sin acceso al escritorio** durante ejecución
- **Servidor HTTP integrado** (puerto 8080)

### Interfaz de Usuario
- **Dashboard responsive** optimizado para pantalla completa
- **Controles táctiles** para operaciones básicas
- **Información del sistema** en tiempo real
- **Estilo moderno** con animaciones CSS

## 🛠️ Desarrollo

### Frontend (React.js)
```bash
cd frontend
npm install       # Instalar dependencias
npm start         # Desarrollo (puerto 3000)
npm run build     # Compilar para producción
```

### Backend (Python)
```bash
# Activar entorno virtual (Ubuntu)
source venv/bin/activate

# Ejecutar solo kiosko
python backend/kiosk_launcher.py
```

## 🐛 Solución de Problemas

### PyQt5 no funciona en Ubuntu
```bash
# El script automáticamente usa entorno virtual
./run-ubuntu.sh

# Verificar instalación manual
source venv/bin/activate
python -c "import PyQt5; print('PyQt5 OK')"
```

### Frontend no compila
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Problemas en Raspberry Pi
```bash
# Verificar dependencias del sistema
sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine

# Verificar display
echo $DISPLAY  # Debe mostrar :0
```

## 🔐 Configuración Kiosko

### Salir del Kiosko
- **Alt+F4**: Salir (solo en modo desarrollo)
- **Ctrl+C**: Cerrar desde terminal que ejecutó el script

### Configuración de Pantalla
El kiosko se adapta automáticamente a la resolución de pantalla disponible.

## 📊 Especificaciones Técnicas

- **Frontend**: React.js 18+, CSS3, HTML5
- **Backend**: Python 3.8+, PyQt5, QtWebEngine
- **Servidor**: HTTP integrado (threading)
- **Compatibilidad**: Ubuntu 20.04+, Raspberry Pi OS Lite
- **Arquitectura**: x86_64 (Ubuntu), ARM64 (Raspberry Pi 5)

## 📝 Flujo de Trabajo

1. **Desarrollo en Ubuntu**: Usar `./run-ubuntu.sh`
2. **Compilar frontend**: Se hace automáticamente
3. **Transferir a Raspberry Pi**: Todo el proyecto
4. **Ejecutar en producción**: `./run-rpi.sh`

---

**NeoPilot** - Kiosko PyQt5 para Raspberry Pi 5

## 🛠️ Desarrollo en Ubuntu

### Instalación Inicial
```bash
# Clonar y configurar
git clone <tu-repo> neeopilot
cd neeopilot

# Configurar entorno automáticamente
chmod +x setup-environment.sh
./setup-environment.sh
```

### Desarrollo del Frontend
```bash
cd frontend

# Instalar dependencias
npm install

# Desarrollo
npm start

# Build para producción
npm run build
```

### Ejecutar en Modo Desarrollo
```bash
# Opción 1: Modo kiosko (PyQt5) - Sistema
./run.sh

# Opción 2: Modo kiosko (PyQt5) - Entorno virtual (recomendado si hay conflictos)
./run-venv.sh

# Opción 3: Modo web (navegador) - Sin dependencias PyQt5
./run-web.sh
```

## 🍓 Deployment en Raspberry Pi 5

### Preparación de la Raspberry Pi
1. **Instalar Raspberry Pi OS Lite** (64-bit recomendado)
2. **Habilitar SSH**: `sudo systemctl enable ssh`
3. **Configurar WiFi** (si es necesario)
4. **Obtener IP**: `hostname -I`

### Deployment Automático
```bash
# Desde tu PC Ubuntu
./deploy-rpi.sh [IP_DE_LA_RASPBERRY_PI]

# Ejemplo:
./deploy-rpi.sh 192.168.1.100
```

El script automáticamente:
- ✅ Copia todos los archivos del proyecto
- ✅ Instala dependencias Python/Qt5
- ✅ Configura el modo kiosko
- ✅ Crea servicio systemd para autostart
- ✅ Configura autologin

### Gestión Remota
```bash
# Ver logs en tiempo real
ssh pi@192.168.1.100 'journalctl -u neeopilot -f'

# Reiniciar servicio
ssh pi@192.168.1.100 'sudo systemctl restart neeopilot'

# Acceso completo
ssh pi@192.168.1.100
```

## 🔧 Configuraciones por Entorno

### Ubuntu (Desarrollo)
- **Display**: X11 (xcb)
- **Resolución**: Automática
- **Modo**: Ventana/Pantalla completa
- **Shortcuts**: Ctrl+Q (salir), F11 (fullscreen)

### Raspberry Pi 5 (Producción)
- **Display**: DirectFB/EGL (eglfs)
- **Resolución**: 1920x1080 (configurable)
- **Modo**: Kiosko completo
- **Autostart**: systemd service
- **No shortcuts**: Modo kiosko puro

## 🚀 Características del Modo Kiosko

- **Pantalla completa sin bordes**
- **Bloqueo de atajos de sistema**
- **Auto-focus permanente**
- **Reinicio automático en caso de crash**
- **Interfaz táctil optimizada**
- **Carga automática del frontend React**

## 📱 Interfaces Disponibles

### 1. Aplicación Qt5 (Principal)
- Modo kiosko completo
- Rendimiento optimizado
- Integración directa con hardware

### 2. Servidor Web (Alternativo)
- Acceso via navegador
- Desarrollo más fácil
- Compatible con cualquier dispositivo

## 🔌 Hardware Soportado

- **Raspberry Pi 5** (recomendado)
- **Raspberry Pi 4** (compatible)
- **PC Ubuntu** (desarrollo)
- **Pantallas táctiles**
- **GPIO/Bluetooth/Audio**

## 🐛 Troubleshooting

### Error de PyQt5
```bash
# En Ubuntu - Usar entorno virtual
./run-venv.sh

# O instalar system-wide
sudo apt-get install python3-pyqt5 python3-pyqt5.qtwebengine

# En Raspberry Pi (automático con deploy)
./setup-environment.sh
```

### Conflictos con Snap packages
```bash
# Usar el launcher con entorno virtual
./run-venv.sh

# O usar la versión web
./run-web.sh
```

### Error de Display
```bash
# Verificar DISPLAY
echo $DISPLAY

# Para Raspberry Pi sin display físico
export QT_QPA_PLATFORM=eglfs
```

### Frontend no encontrado
```bash
# Construir frontend
cd frontend
npm run build
```

## 📊 Performance

### Raspberry Pi 5
- **Boot time**: ~30 segundos hasta kiosko
- **RAM usage**: ~200MB con frontend React
- **CPU usage**: ~5-15% en reposo

### Ubuntu Development
- **Boot time**: Inmediato
- **RAM usage**: ~150MB
- **Hot reload**: Soportado en modo web

## 🔄 Workflow de Desarrollo

1. **Desarrollar en Ubuntu**
   ```bash
   ./run-web.sh  # Para UI development
   ./run.sh      # Para testing kiosko
   ```

2. **Build del frontend**
   ```bash
   cd frontend && npm run build
   ```

3. **Deploy a Raspberry Pi**
   ```bash
   ./deploy-rpi.sh 192.168.1.100
   ```

4. **Test remoto**
   ```bash
   ssh pi@192.168.1.100 'journalctl -u neeopilot -f'
   ```

## 🎨 Personalización

### Resolución de pantalla
```bash
# En deploy-rpi.sh o directamente en RPi
export QT_QPA_EGLFS_WIDTH=1920
export QT_QPA_EGLFS_HEIGHT=1080
```

### Temas y colores
- Modificar `frontend/src/styles/App.css`
- Rebuild: `npm run build`
- Redeploy: `./deploy-rpi.sh [IP]`

### Hardware específico
- Modificar `backend/hardware.py`
- Agregar drivers en `setup-environment.sh`

---

**💡 Tip**: Usa `./run-web.sh` para desarrollo rápido de UI y `./deploy-rpi.sh` para testing en hardware real.
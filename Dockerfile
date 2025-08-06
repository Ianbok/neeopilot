FROM --platform=linux/arm64 ubuntu:24.04

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-pyqt5 \
    python3-pyqt5.qtwebengine \
    qt5-qmake \
    qtbase5-dev \
    qtwebengine5-dev \
    xvfb \
    x11vnc \
    fluxbox \
    wget \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias de Python
RUN pip3 install --no-cache-dir \
    flask \
    flask-socketio \
    PyQt5 \
    requests

# Crear script de inicio
RUN echo '#!/bin/bash\n\
export DISPLAY=:99\n\
Xvfb :99 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &\n\
fluxbox &\n\
x11vnc -display :99 -nopw -listen localhost -xkb -ncache 10 -ncache_cr -forever &\n\
cd /app/backend\n\
python3 main.py\n\
' > /app/start.sh && chmod +x /app/start.sh

# Exponer puerto para VNC (opcional, para ver la GUI)
EXPOSE 5900

# Comando por defecto
CMD ["/app/start.sh"]

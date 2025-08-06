#!/usr/bin/env python3
"""
NeoPilot - Launcher simplificado para modo kiosko
Version que intenta diferentes approaches para funcionar en Ubuntu y RPi
"""

import sys
import os
import subprocess
import platform

def detect_environment():
    """Detectar si estamos en Ubuntu, Raspberry Pi, o otro"""
    try:
        with open('/proc/cpuinfo', 'r') as f:
            if 'Raspberry Pi' in f.read():
                return 'raspberry'
    except:
        pass
    
    try:
        with open('/etc/os-release', 'r') as f:
            if 'Ubuntu' in f.read():
                return 'ubuntu'
    except:
        pass
    
    return 'unknown'

def get_frontend_path():
    """Obtener ruta al frontend"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    frontend_path = os.path.join(project_root, 'frontend', 'build', 'index.html')
    print(f"🔍 Ruta del frontend: {frontend_path}")
    return frontend_path

def launch_with_system_browser():
    """Lanzar usando el navegador del sistema en modo kiosko"""
    frontend_path = get_frontend_path()
    
    if not os.path.exists(frontend_path):
        print(f"❌ Frontend no encontrado: {frontend_path}")
        return False
    
    file_url = f"file://{frontend_path}"
    
    # Intentar diferentes navegadores en modo kiosko
    browsers = [
        ['chromium-browser', '--kiosk', '--no-first-run', '--disable-restore-session-state'],
        ['google-chrome', '--kiosk', '--no-first-run', '--disable-restore-session-state'],
        ['firefox', '--kiosk'],
        ['chromium', '--kiosk', '--no-first-run'],
    ]
    
    for browser_cmd in browsers:
        try:
            print(f"🌐 Intentando lanzar con: {browser_cmd[0]}")
            cmd = browser_cmd + [file_url]
            subprocess.run(cmd, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    
    print("❌ No se pudo encontrar un navegador compatible")
    return False

def launch_with_pyqt():
    """Lanzar usando PyQt5"""
    try:
        from PyQt5.QtWidgets import QApplication, QMainWindow
        from PyQt5.QtWebEngineWidgets import QWebEngineView
        from PyQt5.QtCore import QUrl, Qt
        from PyQt5.QtGui import QKeySequence
        
        print("✅ PyQt5 disponible, lanzando modo kiosko completo...")
        
        class SimpleKiosk(QMainWindow):
            def __init__(self):
                super().__init__()
                self.setWindowTitle("NeoPilot")
                self.setWindowFlags(Qt.FramelessWindowHint)
                
                self.webview = QWebEngineView()
                self.setCentralWidget(self.webview)
                
                # Cargar frontend
                frontend_path = get_frontend_path()
                if os.path.exists(frontend_path):
                    file_url = QUrl.fromLocalFile(frontend_path)
                    self.webview.load(file_url)
                else:
                    self.webview.setHtml("""
                    <html><body style='background:#1e3c72;color:white;font-family:Arial;text-align:center;padding:50px'>
                    <h1>NeoPilot</h1><p>Frontend no encontrado</p>
                    <p>Ejecuta: cd frontend && npm run build</p>
                    </body></html>
                    """)
                
                self.showFullScreen()
        
        app = QApplication(sys.argv)
        window = SimpleKiosk()
        
        print("💡 Presiona Alt+F4 para salir")
        app.exec_()
        return True
        
    except ImportError as e:
        print(f"❌ PyQt5 no disponible: {e}")
        return False

def main():
    print("🚀 NeoPilot - Launcher Universal")
    print("=" * 40)
    
    env = detect_environment()
    print(f"🔍 Entorno: {env}")
    
    # Intentar PyQt5 primero
    if launch_with_pyqt():
        return
    
    print("🌐 PyQt5 no disponible, intentando con navegador...")
    
    # Fallback a navegador del sistema
    if launch_with_system_browser():
        return
    
    # Si nada funciona, mostrar ayuda
    print("\n❌ No se pudo lanzar NeoPilot")
    print("\n💡 Opciones disponibles:")
    print("  1. Instalar PyQt5: sudo apt-get install python3-pyqt5 python3-pyqt5.qtwebengine")
    print("  2. Usar modo web: ./run-web.sh")
    print("  3. Instalar Chromium: sudo apt-get install chromium-browser")
    
    return 1

if __name__ == "__main__":
    sys.exit(main() or 0)

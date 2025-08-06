#!/usr/bin/env python3
"""
NeoPilot - Kiosk Mode Launcher (PyQt5 Only)
Aplicación de kiosko en pantalla completa usando PyQt5 + QtWebEngine
"""

import sys
import os
import subprocess
import signal
import time
import platform
import socket
from pathlib import Path

class KioskLauncher:
    def __init__(self):
        self.is_rpi = platform.machine().startswith(('arm', 'aarch'))
        self.frontend_path = Path(__file__).parent.parent / "frontend" / "build" / "index.html"
        self.server_port = 8080
        self.server_process = None
        
    def start_http_server(self):
        """Inicia el servidor HTTP integrado para servir el frontend"""
        try:
            import http.server
            import socketserver
            import threading
            
            # Directorio del frontend compilado
            frontend_dir = self.frontend_path.parent
            
            print(f"🔍 Sirviendo archivos desde: {frontend_dir}")
            
            class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, directory=str(frontend_dir), **kwargs)
                
                def log_message(self, format, *args):
                    # Silenciar logs HTTP
                    pass
            
            # Intentar crear servidor HTTP
            try:
                self.httpd = socketserver.TCPServer(("", self.server_port), CustomHTTPRequestHandler)
                # Permitir reutilizar el puerto inmediatamente
                self.httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            except OSError as e:
                if e.errno == 98:  # Address already in use
                    print(f"❌ Puerto {self.server_port} ya está en uso")
                    print("💡 Esperando 3 segundos para liberar puerto...")
                    
                    # Intentar matar procesos que usen el puerto y esperar
                    try:
                        import subprocess
                        subprocess.run(["pkill", "-f", "kiosk_launcher.py"], check=False)
                        time.sleep(3)
                        # Reintentar con reutilización de puerto
                        self.httpd = socketserver.TCPServer(("", self.server_port), CustomHTTPRequestHandler)
                        self.httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        print("✅ Puerto liberado, servidor iniciado")
                    except Exception as retry_error:
                        print(f"❌ No se pudo liberar puerto: {retry_error}")
                        return False
                else:
                    raise e
            
            print(f"✅ Servidor HTTP iniciado en puerto {self.server_port}")
            
            # Ejecutar servidor en hilo separado
            def serve_forever():
                self.httpd.serve_forever()
            
            self.server_thread = threading.Thread(target=serve_forever, daemon=True)
            self.server_thread.start()
            
            # Pequeña pausa para asegurar que el servidor está listo
            time.sleep(1)
            
            # Verificar que el servidor responde
            try:
                import urllib.request
                test_url = f"http://localhost:{self.server_port}"
                urllib.request.urlopen(test_url, timeout=2)
                print(f"🌐 Servidor verificado: {test_url}")
            except Exception as e:
                print(f"⚠️  Advertencia: No se pudo verificar servidor: {e}")
            
            # Guardar referencia al servidor
            self.server_process = self.httpd
            return True
                
        except Exception as e:
            print(f"❌ Error iniciando servidor HTTP: {e}")
            return False
    
    def start_pyqt5_kiosk(self):
        """Inicia el modo kiosko con PyQt5"""
        try:
            # Configuración para evitar conflictos
            os.environ.pop('SNAP', None)
            os.environ.pop('SNAP_DESKTOP_RUNTIME', None)
            
            from PyQt5.QtWidgets import QApplication, QMainWindow
            from PyQt5.QtWebEngineWidgets import QWebEngineView
            from PyQt5.QtCore import QUrl, Qt
            
            class KioskBrowser(QMainWindow):
                def __init__(self, server_port, parent_launcher):
                    super().__init__()
                    self.server_port = server_port
                    self.parent_launcher = parent_launcher
                    
                    # Configurar ventana kiosko
                    self.setWindowTitle("NeoPilot Kiosk")
                    self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
                    
                    # Crear WebEngine view
                    self.browser = QWebEngineView()
                    self.setCentralWidget(self.browser)
                    
                    # Cargar URL local
                    url = f"http://localhost:{self.server_port}"
                    self.browser.load(QUrl(url))
                    
                    # Pantalla completa
                    self.showFullScreen()
                    
                def keyPressEvent(self, event):
                    """Control de teclas en modo kiosko"""
                    # Solo Alt+F4 para salir en desarrollo
                    if event.key() == Qt.Key_F4 and event.modifiers() == Qt.AltModifier:
                        self.close()
                    else:
                        # Ignorar todas las demás teclas
                        event.ignore()
                        
                def closeEvent(self, event):
                    """Manejar cierre de ventana"""
                    print("🔧 Cerrando aplicación...")
                    # Limpiar servidor antes de cerrar
                    if self.parent_launcher:
                        self.parent_launcher.cleanup()
                    event.accept()
            
            app = QApplication(sys.argv)
            app.setQuitOnLastWindowClosed(True)
            
            window = KioskBrowser(self.server_port, self)
            
            print("✅ NeoPilot Kiosk iniciado - Presiona Alt+F4 para salir")
            result = app.exec_()
            
            # Asegurar cleanup al salir
            self.cleanup()
            return result
            
        except ImportError as e:
            print(f"❌ PyQt5 no disponible: {e}")
            print("💡 Instala PyQt5: pip install PyQt5 PyQtWebEngine")
            return 1
        except Exception as e:
            print(f"❌ Error con PyQt5: {e}")
            return 1
    
    def cleanup(self):
        """Limpia procesos al salir"""
        try:
            if hasattr(self, 'httpd') and self.httpd:
                print("🔧 Cerrando servidor HTTP...")
                try:
                    self.httpd.shutdown()
                    self.httpd.server_close()
                    
                    # Cerrar el socket explícitamente
                    if hasattr(self.httpd, 'socket'):
                        self.httpd.socket.close()
                    
                    print("✅ Servidor HTTP cerrado")
                except Exception as e:
                    print(f"⚠️  Error cerrando servidor: {e}")
            
            if hasattr(self, 'server_thread') and self.server_thread:
                try:
                    self.server_thread.join(timeout=2)
                except Exception as e:
                    print(f"⚠️  Error esperando hilo servidor: {e}")
                    
        except Exception as e:
            print(f"⚠️  Error en cleanup: {e}")
        finally:
            # Asegurar que las referencias se limpien
            self.httpd = None
            self.server_thread = None
            self.server_process = None
            
            # Pequeña pausa para asegurar liberación del puerto
            time.sleep(0.5)
    
    def run(self):
        """Ejecuta el launcher de kiosko PyQt5"""
        # Configurar manejador de señales
        signal.signal(signal.SIGINT, lambda s, f: self.cleanup() or sys.exit(0))
        signal.signal(signal.SIGTERM, lambda s, f: self.cleanup() or sys.exit(0))
        
        try:
            print("🚀 NeoPilot Kiosk Launcher (PyQt5)")
            print(f"📱 Sistema detectado: {'Raspberry Pi' if self.is_rpi else 'Ubuntu'}")
            
            # Verificar frontend
            if not self.frontend_path.exists():
                print("❌ Frontend no encontrado. Ejecuta: npm run build")
                return 1
            
            # Iniciar servidor HTTP
            if not self.start_http_server():
                print("❌ No se pudo iniciar el servidor HTTP")
                return 1
            
            try:
                # Ejecutar kiosko PyQt5
                return self.start_pyqt5_kiosk()
                    
            finally:
                self.cleanup()
                
        except KeyboardInterrupt:
            print("\n⚡ Cerrando NeoPilot...")
            self.cleanup()
            return 0
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            self.cleanup()
            return 1

if __name__ == "__main__":
    launcher = KioskLauncher()
    sys.exit(launcher.run())

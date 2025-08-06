#!/usr/bin/env python3
"""
NeoPilot - Kiosk Mode Launcher (Alternativo)
Aplicación de kiosko usando navegador del sistema
"""

import sys
import os
import subprocess
import signal
import time
import platform
import socket
import webbrowser
from pathlib import Path

class SimpleKioskLauncher:
    def __init__(self):
        self.is_rpi = platform.machine().startswith(('arm', 'aarch'))
        self.frontend_path = Path(__file__).parent.parent / "frontend" / "build" / "index.html"
        self.server_port = 8082
        self.server_process = None
        
    def start_http_server(self):
        """Inicia el servidor HTTP usando Python"""
        try:
            frontend_dir = self.frontend_path.parent
            print(f"🔍 Sirviendo archivos desde: {frontend_dir}")
            
            # Usar el servidor HTTP de Python
            cmd = [
                sys.executable, 
                "-m", "http.server", 
                str(self.server_port), 
                "--directory", str(frontend_dir)
            ]
            
            # Verificar si el puerto está libre
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(('localhost', self.server_port))
            except OSError:
                print(f"❌ Puerto {self.server_port} ya está en uso")
                return False
            
            self.server_process = subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            # Esperar un momento para que el servidor inicie
            time.sleep(2)
            
            # Verificar que el servidor responde
            try:
                import urllib.request
                test_url = f"http://localhost:{self.server_port}"
                urllib.request.urlopen(test_url, timeout=2)
                print(f"✅ Servidor HTTP iniciado en puerto {self.server_port}")
                print(f"🌐 Servidor verificado: {test_url}")
                return True
            except Exception as e:
                print(f"❌ Error verificando servidor: {e}")
                return False
                
        except Exception as e:
            print(f"❌ Error iniciando servidor HTTP: {e}")
            return False
    
    def start_browser_kiosk(self):
        """Inicia el navegador en modo kiosko"""
        try:
            url = f"http://localhost:{self.server_port}"
            
            if self.is_rpi:
                # En Raspberry Pi, usar Chromium
                cmd = [
                    "chromium-browser",
                    "--kiosk",
                    "--disable-infobars",
                    "--disable-session-crashed-bubble",
                    "--disable-restore-session-state",
                    "--no-first-run",
                    "--disable-dev-shm-usage",
                    "--no-sandbox",
                    url
                ]
            else:
                # En Ubuntu, intentar varios navegadores
                browsers = [
                    ["google-chrome", "--kiosk", "--disable-infobars", url],
                    ["chromium-browser", "--kiosk", "--disable-infobars", url],
                    ["firefox", "--kiosk", url]
                ]
                
                cmd = None
                for browser_cmd in browsers:
                    try:
                        # Verificar si el navegador existe
                        subprocess.run(["which", browser_cmd[0]], check=True, capture_output=True)
                        cmd = browser_cmd
                        break
                    except subprocess.CalledProcessError:
                        continue
                
                if not cmd:
                    print("❌ No se encontró navegador compatible")
                    print("💡 Abriendo en navegador por defecto...")
                    webbrowser.open(url)
                    return 0
            
            print(f"✅ Iniciando navegador en modo kiosko: {cmd[0]}")
            print("💡 Presiona Alt+F4 o Ctrl+C para salir")
            
            # Ejecutar navegador
            browser_process = subprocess.Popen(cmd)
            
            # Esperar a que termine
            try:
                browser_process.wait()
            except KeyboardInterrupt:
                print("\n⚡ Cerrando navegador...")
                browser_process.terminate()
                browser_process.wait()
            
            return 0
            
        except Exception as e:
            print(f"❌ Error con navegador: {e}")
            return 1
    
    def cleanup(self):
        """Limpia procesos al salir"""
        try:
            if self.server_process:
                print("🔧 Cerrando servidor HTTP...")
                self.server_process.terminate()
                self.server_process.wait(timeout=5)
                print("✅ Servidor HTTP cerrado")
        except Exception as e:
            print(f"⚠️  Error en cleanup: {e}")
        finally:
            self.server_process = None
    
    def run(self):
        """Ejecuta el launcher de kiosko simple"""
        # Configurar manejador de señales
        signal.signal(signal.SIGINT, lambda s, f: self.cleanup() or sys.exit(0))
        signal.signal(signal.SIGTERM, lambda s, f: self.cleanup() or sys.exit(0))
        
        try:
            print("🚀 NeoPilot Kiosk Launcher (Simple)")
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
                # Ejecutar navegador en modo kiosko
                return self.start_browser_kiosk()
                    
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
    launcher = SimpleKioskLauncher()
    sys.exit(launcher.run())

#!/usr/bin/env python3
"""
NeoPilot - Servidor HTTP simple para desarrollo
Alternativa que funciona sin PyQt5 para pruebas básicas
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

class NeoPilotHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=self.get_frontend_dir(), **kwargs)
    
    def get_frontend_dir(self):
        # Obtener directorio del frontend
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        frontend_dir = os.path.join(project_root, 'frontend', 'build')
        return frontend_dir
    
    def end_headers(self):
        # Agregar headers para CORS y cache
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Log personalizado
        print(f"🌐 {self.address_string()} - {format % args}")

def open_browser(url, delay=2):
    """Abrir el navegador después de un delay"""
    time.sleep(delay)
    try:
        print(f"🚀 Abriendo navegador en {url}")
        webbrowser.open(url)
    except Exception as e:
        print(f"❌ No se pudo abrir el navegador: {e}")

def main():
    PORT = 8080  # Puerto del servidor
    
    print("🌐 NeoPilot - Servidor HTTP de desarrollo")
    print("=" * 50)
    
    # Verificar si existe el frontend
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    frontend_dir = os.path.join(project_root, 'frontend', 'build')
    
    if not os.path.exists(frontend_dir):
        print(f"❌ Frontend no encontrado en: {frontend_dir}")
        print("💡 Asegúrate de que existe frontend/build/index.html")
        sys.exit(1)
    
    if not os.path.exists(os.path.join(frontend_dir, 'index.html')):
        print(f"❌ index.html no encontrado en: {frontend_dir}")
        sys.exit(1)
    
    print(f"📁 Sirviendo archivos desde: {frontend_dir}")
    print(f"🌐 Servidor iniciando en puerto {PORT}")
    
    # Crear servidor
    try:
        with socketserver.TCPServer(("", PORT), NeoPilotHTTPHandler) as httpd:
            url = f"http://localhost:{PORT}"
            
            print(f"✅ Servidor HTTP activo en: {url}")
            print("📱 NeoPilot disponible en tu navegador")
            print("")
            print("💡 Controles:")
            print("   - Ctrl+C para detener el servidor")
            print("   - F11 en el navegador para pantalla completa")
            print("")
            
            # Abrir navegador en un hilo separado
            browser_thread = threading.Thread(target=open_browser, args=(url,))
            browser_thread.daemon = True
            browser_thread.start()
            
            # Servir indefinidamente
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Puerto {PORT} ya está en uso")
            print("💡 Intenta con otro puerto o detén el servicio que lo usa")
        else:
            print(f"❌ Error del servidor: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

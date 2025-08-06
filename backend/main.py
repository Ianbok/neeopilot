from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, Qt, QTimer
from PyQt5.QtGui import QKeySequence
import sys
import os
import signal

class KioskWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("NeoPilot")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        # Crear vista web
        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)
        
        # Configurar WebEngine para modo kiosko
        settings = self.webview.settings()
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.ErrorPageEnabled, False)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        
        # Deshabilitar menú contextual
        self.webview.setContextMenuPolicy(Qt.NoContextMenu)
        
        # Obtener ruta del frontend
        frontend_path = self.get_frontend_path()
        
        if os.path.exists(frontend_path):
            file_url = QUrl.fromLocalFile(frontend_path)
            print(f"Cargando frontend desde: {frontend_path}")
            self.webview.load(file_url)
        else:
            print(f"Frontend no encontrado en: {frontend_path}")
            self.load_fallback_html()
        
        # Configurar atajos de teclado para salir (solo para desarrollo)
        exit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        exit_shortcut.activated.connect(self.close)
        
        fullscreen_shortcut = QShortcut(QKeySequence("F11"), self)
        fullscreen_shortcut.activated.connect(self.toggle_fullscreen)
        
        # Mostrar en pantalla completa
        self.showFullScreen()
        
        # Timer para mantener foco
        self.focus_timer = QTimer()
        self.focus_timer.timeout.connect(self.maintain_focus)
        self.focus_timer.start(1000)  # Revisar cada segundo
        
    def get_frontend_path(self):
        # Obtener directorio del script actual
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Ir un nivel arriba para llegar a la raíz del proyecto
        project_root = os.path.dirname(script_dir)
        # Construir ruta al frontend
        frontend_path = os.path.join(project_root, 'frontend', 'build', 'index.html')
        return frontend_path
        
    def load_fallback_html(self):
        """Cargar HTML de respaldo si no se encuentra el frontend"""
        fallback_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>NeoPilot - Error</title>
            <style>
                body { 
                    background: #1e3c72; 
                    color: white; 
                    font-family: Arial; 
                    display: flex; 
                    justify-content: center; 
                    align-items: center; 
                    height: 100vh; 
                    margin: 0;
                    text-align: center;
                }
                .error-container {
                    padding: 40px;
                    background: rgba(255,255,255,0.1);
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <div class="error-container">
                <h1>⚠️ NeoPilot</h1>
                <p>Frontend no encontrado</p>
                <p>Construye el frontend React ejecutando:</p>
                <code>cd frontend && npm run build</code>
                <br><br>
                <p><small>Presiona Ctrl+Q para salir</small></p>
            </div>
        </body>
        </html>
        """
        self.webview.setHtml(fallback_html)
        
    def maintain_focus(self):
        """Mantener la aplicación siempre en primer plano (modo kiosko)"""
        if not self.isActiveWindow():
            self.raise_()
            self.activateWindow()
            
    def toggle_fullscreen(self):
        """Alternar pantalla completa (para desarrollo)"""
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
            
    def keyPressEvent(self, event):
        """Manejar eventos de teclado"""
        # Deshabilitar Alt+F4, Alt+Tab, etc. en modo kiosko
        if event.key() == Qt.Key_F4 and event.modifiers() == Qt.AltModifier:
            event.ignore()
        elif event.key() == Qt.Key_Tab and event.modifiers() == Qt.AltModifier:
            event.ignore()
        else:
            super().keyPressEvent(event)

def signal_handler(signum, frame):
    """Manejar señales del sistema para cierre limpio"""
    print("Cerrando NeoPilot...")
    app.quit()

if __name__ == '__main__':
    # Configurar manejo de señales
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Crear aplicación Qt
    app = QApplication(sys.argv)
    app.setApplicationName("NeoPilot")
    app.setQuitOnLastWindowClosed(True)
    
    # Configuraciones para kiosko
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    print("Iniciando NeoPilot en modo kiosko...")
    print("Presiona Ctrl+Q para salir")
    
    # Crear y mostrar ventana principal
    window = KioskWindow()
    
    # Ejecutar aplicación
    sys.exit(app.exec_())
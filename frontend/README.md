# NeeOPiloT Frontend

Interfaz de usuario moderna y táctil para el sistema de asistencia al conductor NeeOPiloT.

## 🎨 Características

- **Diseño Responsivo**: Optimizado para pantallas táctiles de hasta 7 pulgadas
- **Interfaz Táctil**: Botones grandes y gestos intuitivos para uso durante la conducción
- **Modo Kiosko**: Interfaz de pantalla completa sin distracciones
- **Tema Oscuro**: Diseño elegante que reduce la fatiga visual
- **Animaciones Suaves**: Transiciones fluidas y feedback visual

## 🏗️ Arquitectura

- **Framework**: React 18
- **Estilos**: Tailwind CSS 3
- **Enrutamiento**: React Router DOM 6
- **Diseño**: Sistema de componentes modulares

## 📱 Pantallas Principales

### 1. Dashboard
- Acceso rápido a aplicaciones principales
- Destinos recientes
- Estado del sistema

### 2. Navegación
- Integración con Waze y Google Maps
- Búsqueda de ubicaciones
- Destinos rápidos
- Historial de búsquedas

### 3. Comunicaciones
- Gestión de contactos
- Llamadas rápidas
- Mensajes predefinidos
- Historial de llamadas

### 4. Navegador Web
- Navegador completo con marcadores
- Búsquedas rápidas
- Historial de navegación
- Interfaz optimizada para touch

### 5. Configuración
- Ajustes de sistema
- Control de brillo y volumen
- Configuración de conectividad
- Información del dispositivo

## 🎨 Sistema de Diseño

### Colores
- **Primario**: Azul (#3b82f6)
- **Secundario**: Púrpura (#8b5cf6)
- **Éxito**: Verde (#22c55e)
- **Advertencia**: Amarillo (#f59e0b)
- **Error**: Rojo (#ef4444)

### Tipografía
- **Fuente**: Inter (Google Fonts)
- **Tamaños**: Escalados para pantallas pequeñas
- **Peso**: Variable según jerarquía

### Componentes Táctiles
- **Botones**: Área mínima de 44px para touch
- **Espaciado**: Generoso para evitar toques accidentales
- **Feedback**: Animaciones de escala al presionar
- **Estados**: Hover, active, disabled claramente diferenciados

## 🚀 Scripts Disponibles

```bash
# Desarrollo
npm start          # Servidor de desarrollo (puerto 3000)
npm run build      # Compilación para producción
npm test           # Ejecutar tests
npm run eject      # Exponer configuración (irreversible)
```

## 📦 Estructura de Archivos

```
src/
├── components/           # Componentes React
│   ├── Dashboard.js     # Pantalla principal
│   ├── Navigation.js    # Navegación y mapas
│   ├── Communications.js # Llamadas y mensajes
│   ├── Browser.js       # Navegador web
│   ├── Settings.js      # Configuración
│   └── StatusBar.js     # Barra de estado
├── App.js               # Componente principal
├── index.js             # Punto de entrada
└── index.css            # Estilos globales + Tailwind
```

## 🔧 Configuración para Producción

### Variables de Entorno
```bash
REACT_APP_API_URL=http://localhost:5000  # URL del backend Python
REACT_APP_VERSION=1.0.0                 # Versión de la aplicación
```

### Compilación Optimizada
```bash
npm run build
```

Esto genera archivos optimizados en la carpeta `build/` listos para servir en la Raspberry Pi.

## 📱 Optimizaciones para Dispositivos Móviles

- **Viewport**: Configurado para pantallas pequeñas
- **Touch Events**: Optimizado para gestos táctiles
- **Performance**: Lazy loading y code splitting
- **PWA Ready**: Manifiesto configurado para instalación

## 🎯 Próximas Características

- [ ] Soporte para comandos de voz
- [ ] Integración con IA (v2.0)
- [ ] Temas personalizables
- [ ] Widgets configurables
- [ ] Sincronización con el teléfono

## 🛠️ Desarrollo

Para contribuir al desarrollo:

1. Clona el repositorio
2. Instala dependencias: `npm install`
3. Inicia el desarrollo: `npm start`
4. Haz tus cambios
5. Ejecuta tests: `npm test`
6. Compila: `npm run build`

## 📄 Licencia

Proyecto personal - NeeOPiloT v1.0

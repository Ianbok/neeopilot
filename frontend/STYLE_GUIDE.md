# Guía de Estilos - NeeOPiloT Frontend

## 🎨 Principios de Diseño

### Para Pantallas Táctiles
- **Área Mínima de Touch**: 44px x 44px
- **Espaciado Generoso**: Mínimo 16px entre elementos interactivos
- **Feedback Visual**: Animaciones de escala (scale-95) al presionar
- **Estados Claros**: Hover, active, disabled bien diferenciados

### Para Conducción
- **Alto Contraste**: Texto blanco sobre fondos oscuros
- **Iconos Grandes**: Mínimo 24px, preferible 32px+
- **Información Jerárquica**: Lo más importante primero
- **Mínimas Distracciones**: Sin animaciones excesivas

## 🎨 Paleta de Colores

```css
/* Colores Primarios */
--primary-50: #eff6ff;
--primary-500: #3b82f6;  /* Azul principal */
--primary-600: #2563eb;
--primary-900: #1e3a8a;

/* Colores de Estado */
--success-500: #22c55e;  /* Verde - GPS activo, conexiones ok */
--warning-500: #f59e0b;  /* Amarillo - Advertencias */
--danger-500: #ef4444;   /* Rojo - Errores, desconexiones */

/* Grises */
--gray-900: #111827;     /* Fondo principal */
--gray-800: #1f2937;     /* Fondo secundario */
--gray-300: #d1d5db;     /* Texto secundario */
```

## 🔲 Componentes Base

### Botones Táctiles
```css
.touch-button {
  @apply bg-white/10 backdrop-blur-sm border border-white/20 rounded-2xl 
         transition-all duration-200 active:scale-95 active:bg-white/20 
         shadow-lg hover:shadow-xl;
  min-height: 44px;
  min-width: 44px;
}
```

### Tarjetas de Cristal
```css
.glass-card {
  @apply bg-white/5 backdrop-blur-md border border-white/10 rounded-3xl shadow-2xl;
}
```

### Botones de Navegación
```css
.nav-button {
  @apply flex-1 flex items-center justify-center p-4 rounded-2xl 
         transition-all duration-300 active:scale-95;
  min-height: 64px;
}
```

## 📱 Responsive Design

### Breakpoints
- **touch**: 480px (pantallas pequeñas)
- **tablet**: 768px (pantallas medianas)

### Grid Systems
```css
/* Dashboard apps - 2 columnas en pantallas pequeñas */
.app-grid {
  @apply grid grid-cols-2 gap-4;
}

/* Configuraciones - 1 columna siempre */
.settings-grid {
  @apply grid grid-cols-1 gap-4;
}
```

## 🔤 Tipografía

### Jerarquía
- **h1**: 2xl (24px) - Títulos principales
- **h2**: xl (20px) - Subtítulos  
- **h3**: lg (18px) - Secciones
- **body**: base (16px) - Texto normal
- **small**: sm (14px) - Texto secundario

### Pesos
- **font-bold**: Títulos importantes
- **font-semibold**: Subtítulos
- **font-medium**: Botones y etiquetas
- **font-normal**: Texto de contenido

## 🎭 Estados de Interacción

### Botones
```css
/* Estado normal */
.button-normal {
  @apply bg-blue-600 text-white;
}

/* Estado hover (para debugging) */
.button-hover {
  @apply bg-blue-700;
}

/* Estado activo (mientras se presiona) */
.button-active {
  @apply scale-95 bg-blue-800;
}

/* Estado deshabilitado */
.button-disabled {
  @apply bg-gray-600 text-gray-400 cursor-not-allowed;
}
```

### Indicadores de Estado
```css
/* GPS/Conectividad */
.status-online { @apply bg-green-400; }
.status-offline { @apply bg-red-400; }
.status-away { @apply bg-yellow-400; }
```

## 🔧 Utilidades Personalizadas

### Para Touch
```css
.touch-manipulation {
  touch-action: manipulation;
}

.no-select {
  -webkit-user-select: none;
  user-select: none;
}
```

### Para Scroll
```css
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
```

## 📐 Espaciado y Tamaños

### Espaciado Estándar
- **xs**: 4px - Espacios muy pequeños
- **sm**: 8px - Espacios pequeños
- **md**: 16px - Espacios normales
- **lg**: 24px - Espacios grandes
- **xl**: 32px - Espacios muy grandes

### Tamaños de Iconos
- **Iconos pequeños**: 16px (w-4 h-4)
- **Iconos normales**: 24px (w-6 h-6)
- **Iconos grandes**: 32px (w-8 h-8)
- **Iconos de apps**: 64px (w-16 h-16)

## 🎯 Mejores Prácticas

### Accesibilidad
- **Contraste mínimo**: 4.5:1 para texto normal
- **Área de touch**: Mínimo 44x44px
- **Focus visible**: Outline claro en navegación por teclado

### Performance
- **Lazy loading**: Para imágenes y componentes grandes
- **Memorización**: useMemo para cálculos costosos
- **Optimización de re-renders**: useCallback para funciones

### Consistencia
- **Usar classes utilitarias**: Preferir Tailwind sobre CSS custom
- **Componentes reutilizables**: Crear componentes para patrones repetidos
- **Naming consistente**: Usar convenciones claras para nombres

## 🚀 Deployment

### Optimizaciones para Producción
```bash
# Variables de entorno de producción
GENERATE_SOURCEMAP=false
REACT_APP_VERSION=$npm_package_version

# Build optimizado
npm run build
```

### Checklist de Deployment
- [ ] Todas las dependencias instaladas
- [ ] Variables de entorno configuradas
- [ ] Build sin errores ni warnings
- [ ] Tests pasando
- [ ] Performance optimizada
- [ ] Funcionalidad táctil validada

# Blog por Consola - Organización Modular

Sistema interactivo de gestión y auditoría de publicaciones de blog por consola en Python, refactorizado y estructurado mediante módulos y paquetes para garantizar una clara separación de responsabilidades.

## Estructura del Proyecto

```text
blog_consola/
│
├── main.py               # Punto de entrada que orquesta el menú y la ejecución del sistema
├── README.md             # Documentación, descripción y guía de ejecución del proyecto
│
└── blog/                 # Paquete principal de la aplicación
    ├── __init__.py       # Identificador de paquete de Python
    ├── datos.py          # Estructuras de datos base (autor, estados, etiquetas, posts)
    ├── menu.py           # Despliegue del menú y captura segura de inputs con try-except
    ├── operaciones.py    # Lógica de listado, búsqueda por título y filtrado por tag
    └── validaciones.py   # Reglas de negocio y auditoría estructural de publicaciones
```

## Requisitos
- Python 3.8 o superior.

## Cómo ejecutar el sistema
1. Abre tu terminal o consola de comandos.
2. Posiciónate en la carpeta raíz del proyecto (`blog_consola/`):
   ```bash
   cd blog_consola
   ```
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

## Funcionalidades del Menú
1. **Ver todos los posts**: Muestra los posts almacenados con su respectivo título, autor anidado y estado de publicación.
2. **Buscar por título**: Búsqueda flexible e insensible a mayúsculas/minúsculas (`.lower()`).
3. **Filtrar por tag**: Filtrado de posts según la etiqueta solicitada sin distinción de mayúsculas/minúsculas.
4. **Validar posts**: Audita todas las publicaciones verificando presencia de claves, campos no vacíos, autor como diccionario y estados válidos según la tupla permitida.
5. **Salir**: Despliega un mensaje de despedida y finaliza la sesión de manera segura.
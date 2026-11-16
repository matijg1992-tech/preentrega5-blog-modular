# Blog por Consola - Refactorización a POO y Persistencia JSON

Sistema interactivo de gestión y auditoría de publicaciones de blog por consola en Python, refactorizado bajo los principios de **Programación Orientada a Objetos (POO)** y con persistencia completa en archivos **JSON**.

---

## Estructura del Proyecto

```text
blog_consola/
│
├── main.py               # Punto de entrada que orquesta el menú y la instancia de Blog
├── README.md             # Documentación, diseño de clases y guía de ejecución
├── posts.json            # Archivo de persistencia de publicaciones en formato JSON
│
└── blog/                 # Paquete principal de la aplicación
    ├── __init__.py       # Identificador de paquete de Python
    ├── datos.py          # Persistencia: funciones cargar_posts_json y guardar_posts_json
    ├── modelos.py        # Clases de POO: Autor, Post y Blog
    ├── menu.py           # Menú y captura segura de inputs con try-except
    ├── operaciones.py    # Formateo y presentación de datos por consola
    └── validaciones.py   # Auditoría y validación de objetos Post
```

---

## Arquitectura de Clases (POO)

En `blog/modelos.py` se definen las 3 entidades centrales:

1. **`Autor`**:
   - **Atributos**: `nombre`, `bio`, `especialidad`, `redes_sociales`.
   - **Métodos**: `to_dict()`, `from_dict(data)`.
2. **`Post`**:
   - **Atributos**: `id`, `titulo`, `contenido`, `autor` (instancia de `Autor` por composición), `tags`, `estado`.
   - **Métodos**: `to_dict()`, `from_dict(data)`.
3. **`Blog`**:
   - **Atributos**: `posts` (lista de objetos `Post`).
   - **Métodos**: `agregar_post()`, `crear_post()`, `listar_posts()`, `buscar_por_titulo()`, `filtrar_por_tag()`, `to_dict_list()`.

---

## Persistencia y Manejo de Errores con JSON

- **Carga de datos (`cargar_posts_json`)**:
  - Al iniciar, el sistema lee `posts.json`.
  - Si el archivo no existe o está vacío, se inicializa automáticamente con datos semilla.
  - Si el contenido JSON está corrupto, se captura con `json.JSONDecodeError` y se cargan los datos base de forma segura sin abortar la ejecución.
  - Cada elemento del JSON se reconstruye como un objeto `Post` con su correspondiente objeto `Autor`.
- **Guardado de datos (`guardar_posts_json`)**:
  - Serializa los objetos utilizando `to_dict()` para garantizar compatibilidad con `json.dump()`.
  - Permite guardar manualmente (Opción 6) o automáticamente al salir (Opción 7).

---

## ¿Qué cambió respecto a la Preentrega 5?

1. **De Diccionarios a Clases y Objetos**: Se reemplazó el uso directo de estructuras sueltas por las clases `Autor`, `Post` y `Blog`.
2. **Composición de Objetos**: Cada objeto `Post` contiene una referencia a un objeto `Autor`.
3. **Persistencia Real**: Los posts ya no se pierden al cerrar el programa; se almacenan y leen desde `posts.json`.
4. **Creación Dinámica de Posts**: El usuario puede crear publicaciones desde el menú con ID autoincremental y guardarlas en disco.
5. **Menú ampliado a 7 opciones**: Incluye creación y persistencia manual en JSON.

---

## Requisitos y Ejecución

- **Requisitos**: Python 3.8 o superior.
- **Ejecución**:
  ```bash
  cd blog_consola
  python main.py
  ```

---

## Opciones del Menú
1. **Ver todos los posts**: Lista las publicaciones usando los métodos de la clase `Blog`.
2. **Buscar por título**: Búsqueda insensible a mayúsculas y minúsculas (`.lower()`).
3. **Filtrar por tag**: Filtra publicaciones por etiqueta (`.lower()`).
4. **Crear nuevo post**: Pide datos por consola, instancia `Autor` y `Post`, y lo agrega al `Blog`.
5. **Validar posts**: Audita cada objeto `Post` verificando campos requeridos, contenido no vacío y estados válidos.
6. **Guardar posts en JSON**: Persiste todos los objetos en el archivo `posts.json`.
7. **Salir**: Guarda cambios de seguridad y finaliza el programa.
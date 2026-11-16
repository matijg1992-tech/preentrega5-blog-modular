# ==============================================================================
# Módulo de persistencia y datos (JSON y estructuras base)
# Archivo: blog/datos.py
# ==============================================================================

import json
import os
from blog.modelos import Autor, Post

# Constantes del sistema
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Backend", "POO", "JSON"}

# Datos iniciales para inicializar el sistema si no existe posts.json
_perfil_autor_base = {
    "nombre": "Ana López",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@ana_dev", "@ana_python"]
}

_posts_semilla = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "Python es un lenguaje de programación versátil, legible y potente.",
        "autor": _perfil_autor_base,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web de alto nivel para desarrollo ágil y seguro.",
        "autor": _perfil_autor_base,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Aprende a estructurar colecciones complejas usando diccionarios y listas anidadas.",
        "autor": _perfil_autor_base,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    },
    {
        # Post con error para comprobar las validaciones
        "id": 4,
        "titulo": "Post incompleto de prueba",
        "contenido": "",
        "autor": _perfil_autor_base,
        "tags": ["Testing"],
        "estado": "revision"
    }
]


def cargar_posts_json(ruta_archivo="posts.json"):
    """
    Carga las publicaciones desde un archivo JSON y las reconstruye en objetos Post y Autor.
    Maneja excepciones en caso de que el archivo no exista, esté vacío o tenga formato inválido.
    """
    if not os.path.exists(ruta_archivo):
        print(f"[Aviso] No se encontró '{ruta_archivo}'. Inicializando con datos semilla...")
        posts_objetos = [Post.from_dict(p) for p in _posts_semilla]
        guardar_posts_json(posts_objetos, ruta_archivo)
        return posts_objetos

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                print(f"[Aviso] '{ruta_archivo}' está vacío. Cargando publicaciones por defecto...")
                posts_objetos = [Post.from_dict(p) for p in _posts_semilla]
                guardar_posts_json(posts_objetos, ruta_archivo)
                return posts_objetos

            datos = json.loads(contenido)
            if not isinstance(datos, list):
                print(f"[Error] El formato interno de '{ruta_archivo}' no es una lista válida. Reestableciendo...")
                return [Post.from_dict(p) for p in _posts_semilla]

            posts_objetos = []
            for item in datos:
                post = Post.from_dict(item)
                if post is not None:
                    posts_objetos.append(post)

            print(f"[OK] Se cargaron {len(posts_objetos)} publicaciones exitosamente desde '{ruta_archivo}'.")
            return posts_objetos

    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"[Error] No se pudo decodificar el archivo JSON ({e}). Utilizando datos base...")
        return [Post.from_dict(p) for p in _posts_semilla]
    except OSError as e:
        print(f"[Error] Ocurrió un error de entrada/salida al leer el archivo: {e}")
        return [Post.from_dict(p) for p in _posts_semilla]


def guardar_posts_json(posts, ruta_archivo="posts.json"):
    """
    Serializa la lista de objetos Post a formato JSON y los persiste en disco.
    """
    try:
        # Permite recibir una lista de posts o un objeto Blog
        if hasattr(posts, "to_dict_list"):
            lista_dict = posts.to_dict_list()
        else:
            lista_dict = [p.to_dict() if hasattr(p, "to_dict") else p for p in posts]

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(lista_dict, f, indent=4, ensure_ascii=False)

        print(f"[OK] Datos guardados exitosamente en '{ruta_archivo}'.")
        return True
    except (OSError, TypeError) as e:
        print(f"[Error] No se pudieron guardar los posts en '{ruta_archivo}': {e}")
        return False
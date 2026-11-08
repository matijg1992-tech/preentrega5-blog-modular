# ==============================================================================
# Módulo de datos base del blog
# Archivo: blog/datos.py
# ==============================================================================

# 1. Perfil del autor (Diccionario con lista anidada)
perfil_autor = {
    "nombre": "Ana López",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@ana_dev", "@ana_python"]
}

# 2. Estados posibles de una publicación (Tupla inmutable)
estados_post = ("borrador", "publicado", "archivado")

# 3. Etiquetas únicas del blog (Set para evitar duplicados)
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# 4. Catálogo de publicaciones (Lista de diccionarios)
# Incluye publicaciones válidas y publicaciones con errores para pruebas de validación
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "Python es un lenguaje de programación versátil, legible y potente.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web de alto nivel para desarrollo ágil y seguro.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Aprende a estructurar colecciones complejas usando diccionarios y listas anidadas.",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    },
    {
        # Post con error 1: Falta la clave obligatoria 'contenido' y estado inválido
        "id": 4,
        "titulo": "Post con errores de prueba",
        "autor": perfil_autor,
        "tags": ["Testing"],
        "estado": "revision"
    },
    {
        # Post con error 2: Título vacío
        "id": 5,
        "titulo": "",
        "contenido": "Este post tiene un título vacío para comprobar la validación.",
        "autor": perfil_autor,
        "tags": ["Errores"],
        "estado": "borrador"
    }
]
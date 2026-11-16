# ==============================================================================
# Módulo de validación de reglas de negocio y estructuras
# Archivo: blog/validaciones.py
# ==============================================================================

from blog.datos import estados_post
from blog.modelos import Autor, Post

def validar_post(post):
    """
    Verifica que un post cumpla con los requisitos mínimos de estructura:
    1. Que sea una instancia de Post (o un diccionario compatible).
    2. Que 'titulo' y 'contenido' sean cadenas de texto no vacías.
    3. Que 'autor' sea un objeto Autor (o diccionario) con 'nombre' no vacío.
    4. Que 'tags' sea una lista.
    5. Que 'estado' pertenezca a la tupla estados_post.

    Retorna una tupla: (bool es_valido, str mensaje)
    """
    if isinstance(post, Post):
        # Validación de objeto Post
        if post.id is None:
            return False, "Falta el ID del post"

        if not isinstance(post.titulo, str) or not post.titulo.strip():
            return False, "El 'titulo' no puede estar vacío"

        if not isinstance(post.contenido, str) or not post.contenido.strip():
            return False, "El 'contenido' no puede estar vacío"

        if not isinstance(post.autor, Autor) or not getattr(post.autor, "nombre", "").strip():
            return False, "El 'autor' debe ser un objeto Autor con un nombre válido"

        if not isinstance(post.tags, list):
            return False, "El campo 'tags' debe ser una lista"

        if post.estado not in estados_post:
            return False, f"El estado '{post.estado}' no es válido (permitidos: {estados_post})"

        return True, "Válido"

    elif isinstance(post, dict):
        # Soporte para validación de diccionarios
        claves_requeridas = ["id", "titulo", "contenido", "autor", "tags", "estado"]
        for clave in claves_requeridas:
            if clave not in post:
                return False, f"Falta la clave obligatoria '{clave}'"

        titulo = post.get("titulo")
        if not isinstance(titulo, str) or not titulo.strip():
            return False, "El 'titulo' no puede estar vacío"

        contenido = post.get("contenido")
        if not isinstance(contenido, str) or not contenido.strip():
            return False, "El 'contenido' no puede estar vacío"

        autor = post.get("autor")
        if not isinstance(autor, (dict, Autor)):
            return False, "El 'autor' debe ser un diccionario o instancia de Autor"
        nombre = autor.nombre if isinstance(autor, Autor) else autor.get("nombre", "")
        if not str(nombre).strip():
            return False, "El 'autor' debe tener un nombre válido"

        if not isinstance(post.get("tags"), list):
            return False, "El campo 'tags' debe ser una lista"

        estado = post.get("estado")
        if estado not in estados_post:
            return False, f"El estado '{estado}' no es válido (permitidos: {estados_post})"

        return True, "Válido"

    return False, "El post debe ser un objeto Post o un diccionario"
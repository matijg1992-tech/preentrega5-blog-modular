# ==============================================================================
# Módulo de validación de reglas de negocio y estructuras
# Archivo: blog/validaciones.py
# ==============================================================================

from blog.datos import estados_post

def validar_post(post):
    """
    Verifica que un post cumpla con los requisitos mínimos de estructura:
    1. Que sea un diccionario.
    2. Que contenga las claves obligatorias: id, titulo, contenido, autor, tags, estado.
    3. Que 'titulo' y 'contenido' sean cadenas de texto no vacías.
    4. Que 'autor' sea un diccionario y contenga la clave 'nombre'.
    5. Que 'tags' sea una lista.
    6. Que 'estado' pertenezca a la tupla estados_post.

    Retorna una tupla: (bool es_valido, str mensaje)
    """
    if not isinstance(post, dict):
        return False, "El post debe ser un diccionario"

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
    if not isinstance(autor, dict) or "nombre" not in autor or not str(autor.get("nombre")).strip():
        return False, "El 'autor' debe ser un diccionario con la clave 'nombre'"

    tags = post.get("tags")
    if not isinstance(tags, list):
        return False, "El campo 'tags' debe ser una lista"

    estado = post.get("estado")
    if estado not in estados_post:
        return False, f"El estado '{estado}' no es válido (permitidos: {estados_post})"

    return True, "Válido"
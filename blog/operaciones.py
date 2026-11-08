# ==============================================================================
# Módulo de operaciones sobre los posts (listado, búsqueda, filtrado)
# Archivo: blog/operaciones.py
# ==============================================================================

def listar_posts(lista):
    """
    Muestra en consola las publicaciones recibidas con su título, autor y estado.
    Utiliza .get() para acceder de forma segura a datos anidados sin generar KeyError.
    """
    print("\n--- LISTADO DE PUBLICACIONES ---")
    if not lista:
        print("No hay publicaciones disponibles para mostrar.")
        return

    for post in lista:
        titulo = post.get("titulo", "Sin título")
        autor = post.get("autor")
        nombre_autor = autor.get("nombre", "Autor desconocido") if isinstance(autor, dict) else "Autor no especificado"
        estado = post.get("estado", "Desconocido")
        print(f"- ID {post.get('id', '?')}: '{titulo}' | Autor: {nombre_autor} | Estado: {estado}")


def buscar_por_titulo(lista, termino):
    """
    Busca publicaciones cuyo título contenga el término especificado.
    La comparación es insensible a mayúsculas y minúsculas gracias a .lower().
    Retorna una lista con los posts que coinciden.
    """
    if not termino:
        print("El término de búsqueda no puede estar vacío.")
        return []

    termino_lower = termino.strip().lower()
    coincidencias = []

    for post in lista:
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino_lower in titulo.lower():
            coincidencias.append(post)

    return coincidencias


def filtrar_por_tag(lista, tag):
    """
    Filtra publicaciones que incluyan una etiqueta determinada en su lista de tags.
    La comparación es insensible a mayúsculas y minúsculas usando .lower().
    Retorna una lista con los posts que contienen la etiqueta.
    """
    if not tag:
        print("La etiqueta a filtrar no puede estar vacía.")
        return []

    tag_lower = tag.strip().lower()
    coincidencias = []

    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_lower = [str(t).lower() for t in tags]
            if tag_lower in tags_lower:
                coincidencias.append(post)

    return coincidencias
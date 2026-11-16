# ==============================================================================
# Módulo de operaciones y formateo de salida por consola
# Archivo: blog/operaciones.py
# ==============================================================================

from blog.modelos import Autor, Post

def mostrar_posts_en_consola(lista):
    """
    Imprime en consola una lista de objetos Post con formato claro.
    """
    print("\n--- LISTADO DE PUBLICACIONES ---")
    if not lista:
        print("No hay publicaciones disponibles para mostrar.")
        return

    for post in lista:
        if isinstance(post, Post):
            nombre_autor = post.autor.nombre if isinstance(post.autor, Autor) else str(post.autor)
            print(f"- ID {post.id}: '{post.titulo}' | Autor: {nombre_autor} | Estado: {post.estado}")
        elif isinstance(post, dict):
            autor_info = post.get("autor", {})
            nombre = autor_info.get("nombre", "Desconocido") if isinstance(autor_info, dict) else str(autor_info)
            print(f"- ID {post.get('id', '?')}: '{post.get('titulo')}' | Autor: {nombre} | Estado: {post.get('estado')}")


def mostrar_detalle_post(post):
    """
    Muestra todos los campos detallados de una publicación.
    """
    if isinstance(post, Post):
        nombre_autor = post.autor.nombre if isinstance(post.autor, Autor) else str(post.autor)
        print(f"\n[ID {post.id}] {post.titulo}")
        print(f"Autor: {nombre_autor}")
        print(f"Estado: {post.estado}")
        print(f"Tags: {', '.join(post.tags) if post.tags else 'Sin tags'}")
        print(f"Contenido: {post.contenido}")
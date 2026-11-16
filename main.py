# ==============================================================================
# Punto de entrada principal del blog con POO y persistencia JSON
# Archivo: main.py
# ==============================================================================

from blog.modelos import Autor, Post, Blog
from blog.datos import cargar_posts_json, guardar_posts_json, estados_post
from blog.menu import mostrar_menu
from blog.operaciones import mostrar_posts_en_consola, mostrar_detalle_post
from blog.validaciones import validar_post


def crear_post_consola(blog_instancia):
    """
    Solicita interactivamente los datos para crear un nuevo post,
    instancia los objetos Autor y Post, y los agrega a la instancia de Blog.
    """
    print("\n--- CREAR NUEVA PUBLICACIÓN ---")
    titulo = input("Título del post: ").strip()
    if not titulo:
        print("[Error] El título no puede estar vacío.")
        return

    contenido = input("Contenido: ").strip()
    if not contenido:
        print("[Error] El contenido no puede estar vacío.")
        return

    nombre_autor = input("Nombre del autor [Ana López]: ").strip()
    if not nombre_autor:
        nombre_autor = "Ana López"

    bio_autor = input("Bio del autor (opcional): ").strip()
    especialidad = input("Especialidad del autor (opcional): ").strip()
    autor_obj = Autor(
        nombre=nombre_autor,
        bio=bio_autor if bio_autor else "Autor de contenido tech.",
        especialidad=especialidad if especialidad else "Python"
    )

    tags_raw = input("Etiquetas separadas por coma (ej: Python, Web): ").strip()
    tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else ["General"]

    print(f"Estados permitidos: {', '.join(estados_post)}")
    estado = input("Estado de la publicación [publicado]: ").strip().lower()
    if estado not in estados_post:
        estado = "publicado"

    nuevo_post = blog_instancia.crear_post(
        titulo=titulo,
        contenido=contenido,
        autor=autor_obj,
        tags=tags,
        estado=estado
    )
    print(f"\n[Éxito] ¡Post #{nuevo_post.id} '{nuevo_post.titulo}' creado exitosamente como objeto Post!")


def main():
    """
    Función orquestadora del sistema interactivo del blog con POO.
    """
    # 1. Cargar datos persistidos desde JSON a instancias de Post y Autor
    posts_iniciales = cargar_posts_json("posts.json")

    # 2. Instanciar la clase Blog centralizando la colección de objetos
    mi_blog = Blog(posts_iniciales)

    # 3. Bucle interactivo
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            print("Opción inválida: Debes ingresar un número entero del 1 al 7.")
            continue

        if opcion == 1:
            # Opción 1: Ver todos los posts consumiendo la clase Blog
            posts_actuales = mi_blog.listar_posts()
            mostrar_posts_en_consola(posts_actuales)

        elif opcion == 2:
            # Opción 2: Buscar posts por título con método de Blog
            termino = input("Ingresa el término a buscar en el título: ").strip()
            resultados = mi_blog.buscar_por_titulo(termino)
            if resultados:
                print(f"\nResultados encontrados ({len(resultados)}):")
                mostrar_posts_en_consola(resultados)
            else:
                print("No se encontraron publicaciones con ese término.")

        elif opcion == 3:
            # Opción 3: Filtrar posts por tag con método de Blog
            tag = input("Ingresa la etiqueta (tag) por la que deseas filtrar: ").strip()
            resultados = mi_blog.filtrar_por_tag(tag)
            if resultados:
                print(f"\nPublicaciones con la etiqueta '{tag}' ({len(resultados)}):")
                mostrar_posts_en_consola(resultados)
            else:
                print("No se encontraron publicaciones con esa etiqueta.")

        elif opcion == 4:
            # Opción 4: Crear nuevo post instanciando clases
            crear_post_consola(mi_blog)

        elif opcion == 5:
            # Opción 5: Validar posts
            print("\n--- VALIDACIÓN Y AUDITORÍA DE OBJETOS POST ---")
            for post in mi_blog.posts:
                es_valido, motivo = validar_post(post)
                post_id = getattr(post, "id", "?")
                if es_valido:
                    print(f"Post #{post_id}: Válido ({post.titulo})")
                else:
                    print(f"Post #{post_id}: Error -> {motivo}")

        elif opcion == 6:
            # Opción 6: Guardar posts en JSON
            guardar_posts_json(mi_blog.posts, "posts.json")

        elif opcion == 7:
            # Opción 7: Salir (guardado automático de seguridad)
            guardar_posts_json(mi_blog.posts, "posts.json")
            print("\n¡Gracias por utilizar el Sistema de Blog! Hasta pronto.")
            break

        else:
            print("Opción fuera de rango: Por favor ingresa un número entre 1 y 7.")


if __name__ == "__main__":
    main()
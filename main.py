# ==============================================================================
# Archivo principal de ejecución del sistema de blog
# Archivo: main.py
# ==============================================================================

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

def main():
    """
    Función orquestadora del sistema interactivo del blog.
    Controla el bucle principal y coordina las llamadas a los módulos.
    """
    while True:
        opcion = mostrar_menu()

        # Validación de entradas no numéricas controladas por try-except en menu.py
        if opcion is None:
            print("Opción inválida: Debes ingresar un número entero del 1 al 5.")
            continue

        if opcion == 1:
            # Opción 1: Listar todos los posts
            listar_posts(posts)

        elif opcion == 2:
            # Opción 2: Buscar publicaciones por título
            termino = input("Ingresa el término o palabra a buscar en el título: ").strip()
            resultados = buscar_por_titulo(posts, termino)
            if resultados:
                print(f"\nResultados encontrados ({len(resultados)}):")
                listar_posts(resultados)
            else:
                print("No se encontraron publicaciones con ese término en el título.")

        elif opcion == 3:
            # Opción 3: Filtrar publicaciones por etiqueta
            tag = input("Ingresa la etiqueta (tag) por la cual deseas filtrar: ").strip()
            resultados = filtrar_por_tag(posts, tag)
            if resultados:
                print(f"\nPublicaciones con la etiqueta '{tag}' ({len(resultados)}):")
                listar_posts(resultados)
            else:
                print("No se encontraron publicaciones asociadas a esa etiqueta.")

        elif opcion == 4:
            # Opción 4: Auditar y validar los posts en memoria
            print("\n--- VALIDACIÓN DE PUBLICACIONES ---")
            for post in posts:
                post_id = post.get("id", "Desconocido")
                es_valido, motivo = validar_post(post)
                if es_valido:
                    print(f"Post {post_id}: Válido")
                else:
                    print(f"Post {post_id}: Error -> {motivo}")

        elif opcion == 5:
            # Opción 5: Salir del programa
            print("\n¡Gracias por utilizar el Sistema de Blog! Hasta pronto.")
            break

        else:
            print("Opción fuera de rango: Por favor ingresa un número entre 1 y 5.")


if __name__ == "__main__":
    main()
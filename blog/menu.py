# ==============================================================================
# Módulo de interfaz y menú de usuario
# Archivo: blog/menu.py
# ==============================================================================

def mostrar_menu():
    """
    Muestra las opciones del menú principal en consola y captura la elección del usuario.
    Maneja excepciones con try-except para evitar cierres inesperados por entradas no numéricas.
    Retorna la opción como entero, o None si la entrada no es un número válido.
    """
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    entrada = input("Elige una opción (1-5): ").strip()
    try:
        opcion = int(entrada)
        return opcion
    except ValueError:
        return None
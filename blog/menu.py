# ==============================================================================
# Módulo de interfaz y menú de usuario
# Archivo: blog/menu.py
# ==============================================================================

def mostrar_menu():
    """
    Muestra las opciones del menú principal en consola y captura la elección del usuario.
    Maneja excepciones con try-except para evitar cierres inesperados ante entradas no numéricas.
    Retorna la opción como entero, o None si la entrada no es un número válido.
    """
    print("\n--- MENU DEL BLOG (POO + JSON) ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    entrada = input("Elige una opción (1-7): ").strip()
    try:
        opcion = int(entrada)
        return opcion
    except ValueError:
        return None
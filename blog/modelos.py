# ==============================================================================
# Modelos de Programación Orientada a Objetos (POO)
# Archivo: blog/modelos.py
# ==============================================================================

class Autor:
    """
    Representa a una persona autora de publicaciones en el blog.
    """
    def __init__(self, nombre, bio, especialidad="General", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def to_dict(self):
        """Convierte la instancia de Autor a un diccionario serializable en JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def from_dict(cls, data):
        """Reconstruye una instancia de Autor a partir de un diccionario."""
        if not isinstance(data, dict):
            return cls(nombre="Autor desconocido", bio="Sin bio")
        return cls(
            nombre=data.get("nombre", "Sin nombre"),
            bio=data.get("bio", ""),
            especialidad=data.get("especialidad", "General"),
            redes_sociales=data.get("redes_sociales", [])
        )

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Post:
    """
    Representa una publicación individual del blog, relacionada por composición
    con una instancia de la clase Autor.
    """
    def __init__(self, id_post, titulo, contenido, autor, tags=None, estado="borrador"):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        # Composición: autor debe ser una instancia de Autor
        if isinstance(autor, dict):
            self.autor = Autor.from_dict(autor)
        else:
            self.autor = autor
        self.tags = tags if tags is not None else []
        self.estado = estado

    def to_dict(self):
        """Convierte el objeto Post a un diccionario compatible con JSON."""
        autor_dict = self.autor.to_dict() if isinstance(self.autor, Autor) else self.autor
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": autor_dict,
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, data):
        """Reconstruye un objeto Post a partir de un diccionario."""
        if not isinstance(data, dict):
            return None
        autor_data = data.get("autor", {})
        autor_obj = Autor.from_dict(autor_data) if isinstance(autor_data, dict) else autor_data

        return cls(
            id_post=data.get("id"),
            titulo=data.get("titulo", ""),
            contenido=data.get("contenido", ""),
            autor=autor_obj,
            tags=data.get("tags", []),
            estado=data.get("estado", "borrador")
        )

    def __str__(self):
        nombre_autor = self.autor.nombre if isinstance(self.autor, Autor) else str(self.autor)
        return f"- ID {self.id}: '{self.titulo}' | Autor: {nombre_autor} | Estado: {self.estado}"


class Blog:
    """
    Centraliza la colección de publicaciones y la lógica principal del negocio.
    """
    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def agregar_post(self, post):
        """Agrega un objeto Post a la lista interna."""
        if isinstance(post, Post):
            self.posts.append(post)

    def crear_post(self, titulo, contenido, autor, tags=None, estado="publicado"):
        """
        Crea e instancia un nuevo objeto Post con ID incremental automático,
        y lo agrega a la lista de posts del blog.
        """
        nuevo_id = 1
        if self.posts:
            ids_existentes = [p.id for p in self.posts if isinstance(p.id, int)]
            if ids_existentes:
                nuevo_id = max(ids_existentes) + 1

        nuevo_post = Post(
            id_post=nuevo_id,
            titulo=titulo,
            contenido=contenido,
            autor=autor,
            tags=tags if tags is not None else [],
            estado=estado
        )
        self.agregar_post(nuevo_post)
        return nuevo_post

    def listar_posts(self):
        """Retorna todos los objetos Post registrados."""
        return self.posts

    def buscar_por_titulo(self, termino):
        """
        Busca posts cuyo título contenga el término, insensible a mayúsculas/minúsculas.
        """
        if not termino:
            return []
        termino_lower = termino.strip().lower()
        return [
            p for p in self.posts
            if isinstance(p.titulo, str) and termino_lower in p.titulo.lower()
        ]

    def filtrar_por_tag(self, tag):
        """
        Filtra posts que contengan la etiqueta especificada, insensible a mayúsculas/minúsculas.
        """
        if not tag:
            return []
        tag_lower = tag.strip().lower()
        coincidencias = []
        for p in self.posts:
            if isinstance(p.tags, list):
                tags_lower = [str(t).lower() for t in p.tags]
                if tag_lower in tags_lower:
                    coincidencias.append(p)
        return coincidencias

    def to_dict_list(self):
        """Convierte toda la colección de posts a una lista de diccionarios para JSON."""
        return [p.to_dict() for p in self.posts if hasattr(p, "to_dict")]
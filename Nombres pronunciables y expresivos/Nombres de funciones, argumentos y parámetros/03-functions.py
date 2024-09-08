class MovieService:
    # Clase para manejar operaciones relacionadas con películas

    def get_movie_by_id(self, movie_id: str) -> None:
        # Obtener información de una película por su ID
        print({"movie_id": movie_id})

    def get_movie_cast(self, movie_id: str) -> None:
        # Obtener información del elenco de una película por su ID
        print({"movie_id": movie_id})

    def get_actor_bio(self, actor_id: str) -> None:
        # Obtener biografía de un actor por su ID
        print({"actor_id": actor_id})

    def create_movie(self, title: str, description: str, rating: float, cast: list) -> None:
        # Crear una nueva película con título, descripción, calificación y elenco
        print({"title": title, "description": description, "rating": rating, "cast": cast})


class ActorService:
    # Clase para manejar operaciones relacionadas con actores

    def create_actor_if_not_exists(self, full_name: str, birthdate: str) -> bool:
        # Crear un nuevo actor si no existe
        if self.is_actor_exists(full_name):
            return False

        print('Crear actor')
        return True

    def is_actor_exists(self, full_name: str) -> bool:
        # Verificar si un actor ya existe (simulación de verificación asincrónica)
        # ...
        return full_name == 'fernando'


# Ejemplo de uso de las clases y métodos definidos
movie_service = MovieService()
actor_service = ActorService()

# Obtener información de una película por ID
movie_service.get_movie_by_id("123")

# Crear un nuevo actor si no existe
actor_service.create_actor_if_not_exists("fernando", "1990-01-01")

(() => {

    // Función para obtener información de una película por Id
    function getMovieById(movieId: string) {
        console.log({ movieId });
    }

    // Función para obtener información de los actores de una película
    function getMovieCastById(movieId: string) {
        console.log({ movieId });
    }

    // Función para obtener la biografía del actor por Id
    function getActorBioById(actorId: string) {
        console.log({ actorId });
    }
    
    // Crear una película
    function createMovie(title: string, description: string, rating: number, cast: string[]) {
        console.log({ title, description, rating, cast });
    }

    // Crear un nuevo actor si no existe
    function createActorIfNotExists(fullName: string, birthdate: Date): boolean {
        
        // Tarea asincrónica para verificar nombre
        // ..
        // ..
        if (fullName === 'fernando') return false;

        console.log('Crear actor');
        return true;        
    }

})();

//Explicación de los cambios:
//getMovieById: Cambié getAllMovies a getMovieById para indicar claramente que la función obtiene información de una película específica por su ID.
//getMovieCastById: Cambié getAllMovieActors a getMovieCastById para especificar que la función obtiene el reparto de una película por su ID.
//getActorBioById: Cambié getUsuario a getActorBioById para indicar que la función obtiene la biografía de un actor por su ID.
//createMovie: Cambié movie a createMovie para indicar que la función crea una nueva película.
//createActorIfNotExists: Cambié createActorIfActorNotExists a createActorIfNotExists para simplificar y hacer más claro el propósito de la función
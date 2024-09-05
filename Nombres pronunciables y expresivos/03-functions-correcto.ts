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

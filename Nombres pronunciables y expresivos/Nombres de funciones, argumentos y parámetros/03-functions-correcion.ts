(() => {

    // Obtener información de una película por Id
    function getMovieById(movieId: string): void {
        console.log({ movieId });
    }

    // Obtener información de los actores de una película
    function getMovieCast(movieId: string): void {
        console.log({ movieId });
    }

    // Obtener biografía del actor por Id
    function getActorBio(actorId: string): void {
        console.log({ actorId });
    }

    // Crear una película
    function createMovie(title: string, description: string, rating: number, cast: string[]): void {
        console.log({ title, description, rating, cast });
    }

    // Crear un nuevo actor si no existe
    function createActorIfNotExists(fullName: string, birthdate: Date): boolean {
        if (isActorExists(fullName)) return false;

        console.log('Crear actor');
        return true;
    }

    // Verificar si el actor ya existe
    function isActorExists(fullName: string): boolean {
        // Simulación de verificación asincrónica
        // ...
        return fullName === 'fernando';
    }

})();

(() => {
    // Archivos a evaluar
    const archivos = [
        { id: 1, paraBorrar: false },
        { id: 2, paraBorrar: false },
        { id: 3, paraBorrar: true },
        { id: 4, paraBorrar: false },
        { id: 5, paraBorrar: false },
        { id: 7, paraBorrar: true },
    ];

    // Archivos marcados para borrar
    const archivosMarcados = archivos.map(archivo => archivo.paraBorrar);

    // Clases y interfaces de usuario
    class Usuario { };
    interface Usuario { };

    // Fecha actual
    const fechaActual = new Date();
    
    // Días transcurridos
    const diasTranscurridos: number = 23;
    
    // Número de archivos en el directorio
    const cantidadArchivos = 33;
    
    // Nombre completo
    const nombre = 'Fernando';
    const apellido = 'Herrera';

    // Días desde la última modificación
    const diasDesdeModificacion = 12;
    
    // Cantidad máxima de clases por estudiante
    const maxClasesPorEstudiante = 6;
})();

(() => {

    // Ejemplo
    // Archivos a evaluar - files to evaluate
    const filesToEvaluate = [
        { id: 1, isFlagged: false },
        { id: 2, isFlagged: false },
        { id: 3, isFlagged: true },
        { id: 4, isFlagged: false },
        { id: 5, isFlagged: false },
        { id: 7, isFlagged: true },
    ]; 
    
    // Archivos marcados para borrar - files to delete
    const filesToDelete = filesToEvaluate.map(file => file.isFlagged);

    class User { };
    interface IUser { };

    // Todo: Tarea
        
    // día de hoy - today
    const today = new Date();
    
    // días transcurridos - elapsed time in days
    const elapsedTimeInDays: number = 23;
    
    // número de archivos en un directorio - number of files in directory
    const numberOfFilesInDirectory = 33;
    
    // primer nombre - first name
    const firstName = 'Fernando';
    
    // primer apellido - last name
    const lastName = 'Herrera';

    // días desde la última modificación - days since modification
    const daysSinceLastModification = 12;
    
    // cantidad máxima de clases por estudiante - max classes per student
    const maxClassesPerStudent = 6;

})();

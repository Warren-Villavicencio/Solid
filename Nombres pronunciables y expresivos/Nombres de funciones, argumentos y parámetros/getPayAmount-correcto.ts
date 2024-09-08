const getPayAmount = ({ isDead = false, isSeparated = true, isRetired = false }) => {
    if (isDead) return 1500;
    if (isSeparated) return 2500;
    return isRetired ? 3000 : 4000;
};

//Explicación de los cambios:
//Uso de retornos tempranos: Utilicé retornos tempranos para simplificar la lógica y evitar anidamientos innecesarios.
//Operador ternario: Utilicé el operador ternario para reducir el número de líneas de código y hacer la función más compacta.
//Nombres de parámetros: Mantengo los nombres de los parámetros ya que son claros y descriptivos.
//Estos cambios hacen que la función sea más fácil de leer y mantener, además de reducir la cantidad de líneas de código.
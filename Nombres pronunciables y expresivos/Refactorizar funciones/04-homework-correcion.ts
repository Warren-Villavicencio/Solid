(() => {

    // Verifica si una fruta es roja
    function isRedFruit(fruit: string): boolean {
        const redFruits = ['manzana', 'cereza', 'ciruela'];
        return redFruits.includes(fruit);
    }

    // Obtiene las frutas según su color
    function getFruitsByColor(color: string): string[] {
        const fruitsByColor: { [key: string]: string[] } = {
            red: ['manzana', 'fresa'],
            yellow: ['piña', 'banana'],
            purple: ['moras', 'uvas']
        };

        if (!fruitsByColor[color]) {
            throw new Error('El color debe ser: red, yellow, purple');
        }

        return fruitsByColor[color];
    }

    // Verifica el estado de los pasos de trabajo
    function workingSteps(): string {
        const steps = [
            { step: 'First step', isWorking: isFirstStepWorking },
            { step: 'Second step', isWorking: isSecondStepWorking },
            { step: 'Third step', isWorking: isThirdStepWorking },
            { step: 'Fourth step', isWorking: isFourthStepWorking }
        ];

        for (const { step, isWorking } of steps) {
            if (!isWorking) {
                return `${step} broken.`;
            }
        }

        return 'Working properly!';
    }

    // Variables de estado de los pasos de trabajo
    const isFirstStepWorking = true;
    const isSecondStepWorking = true;
    const isThirdStepWorking = true;
    const isFourthStepWorking = true;

    // Ejemplos de uso de las funciones
    console.log({ isRedFruit: isRedFruit('cereza'), fruit: 'cereza' }); // true
    console.log({ isRedFruit: isRedFruit('piña'), fruit: 'piña' }); // false

    console.log({ redFruits: getFruitsByColor('red') }); // ['manzana', 'fresa']
    console.log({ yellowFruits: getFruitsByColor('yellow') }); // ['piña', 'banana']
    console.log({ purpleFruits: getFruitsByColor('purple') }); // ['moras', 'uvas']
    // console.log({ pinkFruits: getFruitsByColor('pink') }); // Error: El color debe ser: red, yellow, purple

    console.log({ workingSteps: workingSteps() }); // Cambiar los valores de las variables de estado y esperar los resultados

})();

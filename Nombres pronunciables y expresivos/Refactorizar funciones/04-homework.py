class FruitService:
    # Clase para manejar operaciones relacionadas con frutas

    def is_red_fruit(self, fruit: str) -> bool:
        # Verifica si una fruta es roja
        red_fruits = ['manzana', 'cereza', 'ciruela']
        return fruit in red_fruits

    def get_fruits_by_color(self, color: str) -> list:
        # Obtiene las frutas según su color
        fruits_by_color = {
            'red': ['manzana', 'fresa'],
            'yellow': ['piña', 'banana'],
            'purple': ['moras', 'uvas']
        }

        if color not in fruits_by_color:
            raise ValueError('El color debe ser: red, yellow, purple')

        return fruits_by_color[color]


class StepService:
    # Clase para manejar el estado de los pasos de trabajo

    def __init__(self, steps: dict):
        self.steps = steps

    def working_steps(self) -> str:
        # Verifica el estado de los pasos de trabajo
        for step, is_working in self.steps.items():
            if not is_working:
                return f'{step} broken.'

        return 'Working properly!'


# Variables de estado de los pasos de trabajo
steps_status = {
    'First step': True,
    'Second step': True,
    'Third step': True,
    'Fourth step': True
}

# Ejemplos de uso de las clases y métodos definidos
fruit_service = FruitService()
step_service = StepService(steps_status)

# Verificar si una fruta es roja
print(fruit_service.is_red_fruit('cereza'))  # True
print(fruit_service.is_red_fruit('piña'))    # False

# Obtener frutas por color
print(fruit_service.get_fruits_by_color('red'))    # ['manzana', 'fresa']
print(fruit_service.get_fruits_by_color('yellow')) # ['piña', 'banana']
print(fruit_service.get_fruits_by_color('purple')) # ['moras', 'uvas']
# print(fruit_service.get_fruits_by_color('pink')) # Error: El color debe ser: red, yellow, purple

# Verificar el estado de los pasos de trabajo
print(step_service.working_steps())  # Cambiar los valores de steps_status y esperar los resultados

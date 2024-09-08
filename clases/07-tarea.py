# Clase base para representar un elemento HTML
class HtmlElement:
    def __init__(self, id: str, type: str):
        # Identificador único del elemento
        self.id = id
        # Tipo de elemento HTML (input, select, textarea, radio)
        self.type = type

# Clase para representar los atributos de un input
class InputAttributes:
    def __init__(self, value: str, placeholder: str):
        # Valor actual del input
        self.value = value
        # Texto que se muestra cuando el input está vacío
        self.placeholder = placeholder

# Clase para manejar los eventos de un input
class InputEvents:
    def __init__(self, html_element: HtmlElement, attributes: InputAttributes):
        # Elemento HTML asociado
        self.html_element = html_element
        # Atributos del input
        self.attributes = attributes

    # Establece el foco en el input
    def set_focus(self):
        print(f"Foco en el elemento con id: {self.html_element.id}")

    # Obtiene el valor actual del input
    def get_value(self):
        return self.attributes.value

    # Verifica si el input está activo (tiene el foco)
    def is_active(self):
        # Simulación de verificación de elemento activo
        return True  # Aquí deberías implementar la lógica real

    # Elimina el valor del input
    def remove_value(self):
        self.attributes.value = ''

# Creación de un nuevo campo de nombre con eventos asociados
name_field = InputEvents(
    HtmlElement('txtName', 'input'),
    InputAttributes('Fernando', 'Enter first name')
)

# Imprime los atributos del campo de nombre
print(vars(name_field))

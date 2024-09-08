from datetime import datetime
from typing import Literal

# Definición del tipo Gender
Gender = Literal['M', 'F']

# Clase Person que representa a una persona
class Person:
    def __init__(self, name: str, gender: Gender, birthdate: datetime):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate

# Clase User que representa a un usuario y extiende de Person
class User(Person):
    def __init__(self, name: str, gender: Gender, birthdate: datetime, email: str, role: str):
        super().__init__(name, gender, birthdate)
        self.email = email
        self.role = role
        self.last_access = datetime.now()

    # Método para verificar las credenciales del usuario
    def check_credentials(self) -> bool:
        return True

# Clase UserSettings que representa la configuración del usuario y extiende de User
class UserSettings(User):
    def __init__(self, name: str, gender: Gender, birthdate: datetime, email: str, role: str, working_directory: str, last_open_folder: str):
        super().__init__(name, gender, birthdate, email, role)
        self.working_directory = working_directory
        self.last_open_folder = last_open_folder

# Creación de una instancia de UserSettings con datos de ejemplo
user_settings = UserSettings(
    name='Fernando',
    gender='M',
    birthdate=datetime(1985, 10, 21),
    email='fernando@google.com',
    role='Admin',
    working_directory='/usr/home',
    last_open_folder='/home'
)

print(user_settings.__dict__)

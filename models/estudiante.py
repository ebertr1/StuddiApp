from models.persona import Persona

class Estudiante(Persona):
    def __init__(self):
        self.numeroMatricula = "numeroMatricula"
        super().__init__()
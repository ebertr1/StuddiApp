from models.persona import Persona

class Docente(Persona):
    def __init__(self):
        self.tituloAcademico = "tituloAcademico"
        super().__init__()
from models.persona import Persona
class Cuenta:
    def __init__(self):
        self.persona = Persona()
        self.__correo = ''
        self.__contrasena = ''
    

    def get_persona(self):
        return self.persona

    def set_persona(self, value):
        self.persona = value

    @property
    def _correo(self):
        return self.__correo

    @_correo.setter
    def _correo(self, value):
        self.__correo = value

    @property
    def _contrasena(self):
        return self.__contrasena

    @_contrasena.setter
    def _contrasena(self, value):
        self.__contrasena = value

@property
def serializable(self):
     return{
            'persona': self.persona.serializable,
            'correo': self._correo,
            'contrasena': self._contraseña
     }
def deserializar(self, data):
    self.persona.deserializable(data['persona'])
    self._correo = data['correo']
    self._contrasena = data['contraseña']
    return self

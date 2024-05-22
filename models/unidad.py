class Unidad:
    def __init__(self):
        self.__numero_unidad = ''

    @property
    def _numero_unidad(self):
        return self.__numero_unidad

    @_numero_unidad.setter
    def _numero_unidad(self, value):
        self.__numero_unidad = value

    @property
    def serializable(self):
        return {
            'numero_unidad': self.__numero_unidad
        }
    def deserializable(self, data):
        self.__numero_unidad = data['numero_unidad']
        return self
    


    
        
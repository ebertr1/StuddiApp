class PeriodoAcademico:
    def __init__(self):
        self.__periodo = ''
    
    @property
    def get_periodo(self):
        return self.__periodo

    @get_periodo.setter
    def set_periodo(self, value):
        self.__periodo = value


    @property
    def serializable(self):
        return {
            'periodo': self.__periodo
        }
    def deserializable(self, data):
        self.__periodo = data['periodo']
        return self
    
    def __str__(self):
        return f'Periodo: {self.__periodo}'
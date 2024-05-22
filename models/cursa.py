class Cursa:
    def __init__(self, estudiante='', materia='', unidad='', periodo_academico=''):
        self.__estudiante = estudiante
        self.__materia = materia
        self.__unidad = unidad
        self.__periodo_academico = periodo_academico


    @property
    def _estudiante(self):
        return self.__estudiante

    @_estudiante.setter
    def _estudiante(self, value):
        self.__estudiante = value

    @property
    def _materia(self):
        return self.__materia

    @_materia.setter
    def _materia(self, value):
        self.__materia = value

    @property
    def _unidad(self):
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _periodo_academico(self):
        return self.__periodo_academico

    @_periodo_academico.setter
    def _periodo_academico(self, value):
        self.__periodo_academico = value


    @property
    def serializable(self):
        return {
            'estudiante': self.__estudiante,
            'materia': self.__materia,
            'unidad': self.__unidad,
            'periodo_academico': self.__periodo_academico
        }
    def deserializable(self, data):
        self.__estudiante = data['estudiante']
        self.__materia = data['materia']
        self.__unidad = data['unidad']
        self.__periodo_academico = data['periodo_academico']
        return self
    

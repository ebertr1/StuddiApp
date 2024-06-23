class MallaCurricular:
    def __init__(self):
        self.__nombre=''

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

#aqui se pone la malla curricular que es estatico, no se medifica
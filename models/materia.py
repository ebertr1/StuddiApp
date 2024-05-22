from models.enumCodigo import EnumCodigo
class Materia:
    def __init__(self):
        self.__nombre=''
        self.__codigo=EnumCodigo.CODIGO
        
    @property
    def _codigo(self):
        return self.__codigo

    @__codigo.setter
    def _codigo(self, value):
        self.__codigo = value
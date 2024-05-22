import models.enumCiclo import EnumCiclo
class Ciclo:
    def __init__(self):
        self.__numero:EnumCiclo.CICLO
        
    @property
    def _numero(self):
        return self.__numero
    
    @_numero.setter
    def _numero(self, value):
        self.__numero= value
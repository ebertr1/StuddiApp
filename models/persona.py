class Persona():
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__dni = ''
        self.__apellido = ''
        self.__direccion = ''
        self.__telefono = ''
        self.__correo = ''
        self.__nacimiento = ''
        self.__rol = ''

    @property
    def _rol(self):
        return self.__rol

    @_rol.setter
    def _rol(self, value):
        self.__rol = value

      

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value


    @property
    def _nacimiento(self):
        return self.__nacimiento

    @_nacimiento.setter
    def _nacimiento(self, value):
        self.__nacimiento = value

   
    @property
    def serializable(self):
     return{
        'id': self._id,
         'rol': self._rol,
        'nombre': self._nombre,
        'dni': self._dni,
        'apellido': self._apellido,
        'direccion': self._direccion,
        'telefono': self._telefono,
        'nacimiento': self._nacimiento,
       
     }
    def deserializar(self, data):
        persona = Persona()
        
        persona._id = data['id']
        persona._rol = data['rol']
        persona._nombre = data['nombre']
        persona._dni = data['dni']
        persona._apellido = data['apellido']
        persona._direccion = data['direccion']
        persona._telefono = data['telefono']
        persona._nacimiento = data['nacimiento']
      
        return persona

  
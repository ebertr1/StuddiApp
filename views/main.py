import sys
sys.path.append('../')
from controls.personaDaoControl import PersonaDaoControl
from controls.cuentaDaoControl import CuentaDaoControl



per = PersonaDaoControl()



try:

    
    per._persona._rol = "Administrador"
    per._persona._nombre = "Anthony Fernando"
    per._persona._dni = "12020280"
    per._persona._apellido = "Gutierrez Gutierre"
    per._persona._direccion = "Ciudad Victoria"
    per._persona._telefono = "0997288985"
    per._persona._nacimiento = "1999-12-12"
    per.save
    per._persona = None
    per._persona._nombre = "Eber Daniel"
    per._persona._rol = "Estudiante"
    per._persona._dni = "12020280"
    per._persona._apellido = "Guayllas Poma"
    per._persona._direccion = "CVicentino"
    per._persona._telefono = "123456"
    per._persona._nacimiento = "1999-12-12"
    per.save
    per._persona = None
    per._persona._nombre = "Ariana Sophia"
    per._persona._rol = "Profesor"
    per._persona._dni = "12020280"
    per._persona._apellido = "Sarango Tandazo"
    per._persona._direccion = "Loja"
    per._persona._telefono = "123456"
    per._persona._nacimiento = "1999-12-12"
    per.save
    per._persona = None

except Exception as e:
    print(e)
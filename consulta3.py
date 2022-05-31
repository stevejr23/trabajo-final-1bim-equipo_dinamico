from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

canNum =  session.query(Canton, Establecimiento).join(Establecimiento).\
        filter(or_(Establecimiento.numDocentes == "0", Establecimiento.numDocentes == "5", Establecimiento.numDocentes == "11")).all()

print("Consulta 1")

for j in canNum:
	print(j)

esJor = session.query(Establecimiento, Parroquia).join(Parroquia).\
        filter(and_(Establecimiento.numEstudiantes >= "21", Parroquia.nombre == "Pindal")).all()

print("Consulta 2")

for e in esJor:
	print(e)
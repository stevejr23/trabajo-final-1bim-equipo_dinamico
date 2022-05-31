from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

esCod = session.query(Establecimiento).\
        filter(and_(Establecimiento.numDocentes == "100").order_by(Establecimiento.numEstudiantes)).all()

print("Consulta 1")

for c in esCod:
	print(c)

esCod = session.query(Establecimiento).\
        filter(and_(Establecimiento.numDocentes == "100").order_by(Establecimiento.numDocentes)).all()

print("Consulta 2")

for c in esCod:
	print(c)
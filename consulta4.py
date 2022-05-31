from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

esOr = session.query(Establecimiento, Parroquia).join(Parroquia).\
        filter(and_(Establecimiento.numDocentes >= "40", Establecimiento.tipoEducacion == "Educación regular").order_by(Parroquia.nombre)).all()

print("Consulta 1")

for e in esOr:
	print(e)

esCod = session.query(Establecimiento).\
        filter(and_(Establecimiento.codDistrito == "11D04").order_by(Establecimiento.sostenimiento)).all()

print("Consulta 2")

for c in esCod:
	print(c)
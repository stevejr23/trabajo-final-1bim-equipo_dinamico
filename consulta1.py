from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

codPar = session.query(Establecimiento, Parroquia).join(Parroquia).\
        filter(Parroquia.codigo == "110553").all()

print("Consulta 1")

for e in codPar:
	print(e)

provAu = session.query(Establecimiento, Provincia).join(Provincia).\
        filter(Provincia.nombre == "Oro").all()

print("Consulta 2")

for o in provAu:
	print(o)

canPor = session.query(Establecimiento, Canton).join(Canton).\
        filter(Canton.nombre == "Portovelo").all()

print("Consulta 3")

for p in canPor:
	print(p)

canZam = session.query(Establecimiento, Canton).join(Canton).\
        filter(Canton.nombre == "Zamora").all()

print("Consulta 4")

for z in canZam:
	print(z)

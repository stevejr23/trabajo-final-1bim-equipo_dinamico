from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tabla import Establecimiento

# se importa la clase(s) del
# archivo genera_tablas
from crear_tablas import Provincia, Canton

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

establecimiento = []

with open('data/Listado-Instituciones-Educativas.csv', 'r', encoding="utf8") as archivo:
    next(archivo, None)

    for r in archivo:
        r = r.split('|')
        establecimiento.append((r[0], r[1], r[8], r[9], r[10], r[11],
                                r[12], r[13], r[14], r[15].replace('\n', ''), r[6]))

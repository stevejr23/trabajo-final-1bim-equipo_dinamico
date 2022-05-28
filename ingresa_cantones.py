from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from crear_tabla import Provincia, Canton

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

provincias = []

with open('data/Listado-Instituciones-Educativas.csv', 'r', encoding="utf8") as archivo:
    next(archivo, None)

    for r in archivo:
        r = r.split('|')
        provincias.append((r[4], r[5], r[6]))

import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from crear_tabla import Parroquia, Provincia, Canton

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Lectura del archivo
with open('data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    next(reader)

    # Lista donde se guardan los cantones (vacia)
    parroquia = []

    # Ciclo repetitivo
    for row in reader:
        # Que no se presenten valores repetitivos 
        if row[7] not in parroquia:
            
            parroquia.append(row[7])

            id_p = session.query(Canton).filter_by(nombre=row[5]).first()

            # Creación del objeto de tipo Canton
            can = Parroquia(
                nombre=row[7], codigo=row[6], canton=id_p)
            session.add(can)
# commit de transacciones
session.commit()
import csv
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

# Lectura del archivo
with open('data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    next(reader)

    # Lista donde se guardan los cantones (vacia)
    cantones = []

    # Ciclo repetitivo
    for row in reader:
        # Que no se presenten valores repetitivos 
        if row[5] not in cantones:
            
            cantones.append(row[5])

            id_p = session.query(Provincia).filter_by(nombre=row[3]).first()

            # Creación del objeto de tipo Canton
            can = Canton(
                nombre=row[5], codigo=row[4], provincia_id=id_p.id)
            session.add(can)
# commit de transacciones
session.commit()

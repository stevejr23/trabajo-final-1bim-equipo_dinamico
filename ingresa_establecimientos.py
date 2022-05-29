import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from crear_tabla import Establecimiento, Parroquia, Provincia, Canton

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
        num_Estudiantes = int (row[14],base=0)
        num_Docentes = int (row[15],base=0)

        id_p = session.query(Parroquia).filter_by(nombre=row[7]).first()

        # Creación del objeto de tipo Canton
        establecimiento = Establecimiento( codigoAMIE = row [0], nombreInstitucion = row [1], codDistrito = row[8],sostenimiento = row[9], tipoEducacion = row[10],
        modalidad = row[11], jornada = row[12], acceso = row[13], numEstudiantes = num_Estudiantes, 
        numDocentes = num_Docentes, parroquia = id_p)
        session.add(establecimiento)
# commit de transacciones
session.commit()

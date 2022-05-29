from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Ejemplo que representa la relación entre dos clases
# One to Many
# Un club tiene muchos jugadores asociados


class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(100))
    nombre = Column(String(100))
    # Mapea la relación entre las clases
    # Club puede acceder a los jugadores asociados
    # por la llave foránea
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: codigo=%s | nombre=%s " % (
            self.codigo,
            self.nombre)

# Un cantón pertence a un provincia.


class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(100))
    nombre = Column(String(100), nullable=False)
    # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # Mapea la relación entre las clases
    # Jugador tiene una relación con Club
    provincia = relationship("Provincia", back_populates="cantones")
    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: codigo:%s - nombre: %s" % (
            self.codigo,
            self.nombre)

# Una parroquia pertence a un cantón.


class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(100))
    nombre = Column(String(100), nullable=False)
    # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    canton_id = Column(Integer, ForeignKey('canton.id'))
    # Mapea la relación entre las clases
    # Jugador tiene una relación con Club
    canton = relationship("Canton", back_populates="parroquia")
    establecimiento = relationship(
        "Establecimiento", back_populates="parroquia")

    def __repr__(self):
        return "Parroquia: codigo:%s - nombre: %s" % (
            self.codigo,
            self.nombre)

# Un establecimiento pertenece a una parroquia.


class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigoAMIE = Column(String(100))
    nombreInstitucion = Column(String(100))
    codDistrito = Column(String(50))
    sostenimiento = Column(String(100))
    tipoEducacion = Column(String(100))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    numEstudiantes = Column(Integer)
    numDocentes = Column(Integer)
    # se agrega la columna parroquia_id como ForeignKey
    # se hace referencia al id de la entidad parroquia
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    # Mapea la relación entre las clases
    # Establecimiento tiene una relación con Parroquias
    parroquia = relationship("Parroquia", back_populates="establecimiento")

    def __repr__(self):
        return "Establecimiento: codigoAMIE=%s - nombreInstitucion=%s - codDistrito=%s - sostenimiento=%s - tipoEducacion=%s - modalidad=%s - jornada=%s - acceso=%s - numEstudiantes=%d - numDocentes=%d " % (
            self.codigoAMIE,
            self.nombreInstitucion,
            self.codDistrito,
            self.sostenimiento,
            self.tipoEducacion,
            self.modalidad,
            self.jornada,
            self.acceso,
            self.numEstudiantes,
            self.numDocentes)


Base.metadata.create_all(engine)

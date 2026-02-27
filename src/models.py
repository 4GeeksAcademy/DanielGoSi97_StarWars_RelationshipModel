from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class Personaje(db.Model):

    __tablename__ = "personaje"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    id_planeta: Mapped[int] = mapped_column(ForeignKey("planeta.id"), nullable=False)
    id_especie: Mapped[int] = mapped_column(ForeignKey("especie.id"), nullable=False)
    id_nave: Mapped[[int]] = mapped_column(ForeignKey("nave.id"), nullable=True)
    id_pelicula: Mapped[[int]] = mapped_column(ForeignKey("pelicula.id"), nullable=True)

    planeta: Mapped["Planeta"] = relationship(back_populates="residentes")
    especie: Mapped["Especie"] = relationship(back_populates="miembros")
    nave: Mapped["Nave"] = relationship(back_populates="pilotos")
    pelicula: Mapped["Pelicula"] = relationship(back_populates="personajes")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }

class Planeta(db.Model):

    __tablename__ = "planeta"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    clima: Mapped[str] = mapped_column(String(120), nullable=False)

    residentes: Mapped[List["Personaje"]] = relationship(back_populates="planeta")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima
        }

class Especie(db.Model):

    __tablename__ = "especie"

    id: Mapped[int] = mapped_column(primary_key=True)

    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    
    miembros: Mapped[List["Personaje"]] = relationship(back_populates="especie")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Nave(db.Model):
    __tablename__ = "nave"

    id: Mapped[int] = mapped_column(primary_key=True)

    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    modelo: Mapped[str] = mapped_column(String(120), nullable=False)

    pilotos: Mapped[List["Personaje"]] = relationship(back_populates="nave")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo": self.model
        }
    
class Pelicula(db.Model):
    __tablename__ = "pelicula"

    id: Mapped[int] = mapped_column(primary_key=True)

    titulo: Mapped[str] = mapped_column(String(120), nullable=False)
    año: Mapped[int] = mapped_column(nullable=False)

    personajes: Mapped[List["Personaje"]] = relationship(back_populates="pelicula")

    def serialize(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "año": self.año
        }
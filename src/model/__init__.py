from sqlalchemy import String, Integer, Column, ForeignKey, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.orm import DeclarativeBase, Mapped, Session
from typing import List
from flask_login import UserMixin
from config.config_database import USER, HOST, PORT, DATABASE, PASSWORD
from datetime import date
from insert import insert_relevancia, insert_tipo_evento

ENGINE = create_engine(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
session = Session(ENGINE)


class Base(DeclarativeBase, UserMixin):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    eventos: Mapped[List["DataEvento"]] = relationship(back_populates="user")


class Relevancia(Base):
    __tablename__ = "relevancia"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nivel: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    eventos: Mapped[List["DataEvento"]] = relationship(back_populates="relevancia")


class TipoEvento(Base):
    __tablename__ = "tipo_evento"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
    eventos: Mapped[List["DataEvento"]] = relationship(back_populates="tipo_evento")


class DataEvento(Base):
    __tablename__ = "data_evento"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo_evento: Mapped[str] = mapped_column(String(100), nullable=False)
    data: Mapped[str] = mapped_column(Date, nullable=False, default=date.today())

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="eventos")

    relevancia_id: Mapped[int] = mapped_column(ForeignKey("relevancia.id"))
    relevancia: Mapped["Relevancia"] = relationship(back_populates="eventos")
    
    tipo_evento_id: Mapped[int] = mapped_column(ForeignKey("tipo_evento.id"))
    tipo_evento: Mapped["TipoEvento"] = relationship(back_populates="eventos")

# Inserindo dados de tabelas de domínio
insert_relevancia()
insert_tipo_evento()
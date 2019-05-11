# Author: Junior Tada
from app.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Produtor(Base):
    __tablename__ = 'produtor'

    nome = Column(String)
    nome_propriedade = Column(String)
    tamanho = Column(String)


class Producao(Base):
    __tablename__ = 'producao'

    produtor_id = Column(Integer, ForeignKey('produtor.id'))
    produtor = relationship("Produtor", backref="producoes", lazy="joined")

    data = Column(DateTime, default=datetime.now)
    quantidade = Column(String)
    ccs = Column(String)
    cmt = Column(String)
    cbt = Column(String)
    gordura = Column(String)
    proteina = Column(String)
    lactose = Column(String)
    solidos = Column(String)

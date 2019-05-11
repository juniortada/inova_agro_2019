# Author: Junior Tada
from app.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship


class Produtor(Base):
    __tablename__ = 'produtor'

    nome = Column(String)
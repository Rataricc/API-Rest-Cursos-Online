from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

#Modelo: archivo models.py, estos modelos son la representacion en codigo, de lo que despues (una vez se migre)
# veremos en la base de datos, el nombre de la clase, seria el nombre de la tabla. 
# y los atributos de la clase serian, los campos de la tabla users.

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

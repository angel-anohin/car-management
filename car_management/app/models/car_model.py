# app/models/car_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from sqlalchemy import Table, Column, ForeignKey


# Междинна таблица за релация много към много
car_garages = Table(
    'car_garages',
    Base.metadata,
    Column('carId', ForeignKey('cars.id', ondelete="CASCADE"), primary_key=True),
    Column('garageId', ForeignKey('garages.id', ondelete="CASCADE"), primary_key=True),
)

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    productionYear = Column(Integer, nullable=False)
    licensePlate = Column(String(10), nullable=False, unique=True)
    
     # Свързване със сервизите чрез междинната таблица
    garages = relationship(
        "Garage",
        secondary=car_garages,
        back_populates="cars",
    )
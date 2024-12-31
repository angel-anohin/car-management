from sqlalchemy import Column, Integer, String
from app.models.base import Base
from sqlalchemy.orm import relationship
from app.models.car_model import car_garages

class Garage(Base):
    __tablename__ = "garages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    
     
    cars = relationship(
        "Car",
        secondary=car_garages,
        back_populates="garages",
    )
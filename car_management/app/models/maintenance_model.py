# app/models/maintenance_model.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class Maintenance(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True, index=True)
    carId = Column(Integer, ForeignKey("cars.id"), nullable=False)
    serviceType = Column(String(200), nullable=False)
    scheduledDate = Column(Date, nullable=False)
    garageId = Column(Integer, ForeignKey("garages.id"), nullable=False)
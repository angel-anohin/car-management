# app/repositories/maintenance_repository.py
from sqlalchemy.orm import Session
from app.models.maintenance_model import Maintenance
from app.models.car_model import Car
from app.models.garage_model import Garage

class MaintenanceRepository:
    @staticmethod
    def create(db: Session, maintenance: Maintenance):
        db_maintenance = Maintenance(
        serviceType=maintenance.serviceType,
        scheduledDate=maintenance.scheduledDate,
        carId=maintenance.carId,
        garageId=maintenance.garageId
    )
        db.add(db_maintenance)
        db.commit()
        db.refresh(db_maintenance)
        return db_maintenance

    @staticmethod
    def get_by_id(db: Session, maintenance_id: int):
        return db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Maintenance).all()

    @staticmethod
    def update(db: Session, maintenance: Maintenance):
        db.commit()
        db.refresh(maintenance)
        return maintenance

    @staticmethod
    def delete(db: Session, maintenance: Maintenance):
        db.delete(maintenance)
        db.commit()
        
        
    def get_car_by_id(db: Session, carId: int):
        return db.query(Car).filter(Car.id == carId).first()

    def get_garage_by_id(db: Session, garageId: int):
        return db.query(Garage).filter(Garage.id == garageId).first()
    
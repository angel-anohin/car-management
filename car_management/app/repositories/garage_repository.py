# app/repositories/garage_repository.py
from sqlalchemy.orm import Session
from app.models.garage_model import Garage

class GarageRepository:
    @staticmethod
    def create(db: Session, garage: Garage):
        db.add(garage)
        db.commit()
        db.refresh(garage)
        return garage

    @staticmethod
    def get_by_id(db: Session, garageId: int):
        return db.query(Garage).filter(Garage.id == garageId).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Garage).all()

    @staticmethod
    def update(db: Session, garage: Garage):
        db.commit()
        db.refresh(garage)
        return garage

    @staticmethod
    def delete(db: Session, garage: Garage):
        db.delete(garage)
        db.commit()
        
        
    def get_garages_by_city(db: Session, city: str):
    # Търсим гаражи, които съвпадат с посочения град
        return db.query(Garage).filter(Garage.city == city).all()
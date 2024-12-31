# app/repositories/car_repository.py
from sqlalchemy.orm import Session
from app.models.car_model import Car
from app.models.garage_model import Garage
from app.schemas.car_schemas import CreateCarDTO, UpdateCarDTO
from sqlalchemy.orm import joinedload
from app.services.car_service import format_car_response

class CarRepository:
    @staticmethod
    def create(db: Session, car: CreateCarDTO):
        # Създаване на нова кола
        db_car = Car(
            make=car.make,
            model=car.model,
            productionYear=car.productionYear,
            licensePlate=car.licensePlate
    )
    
    # Добавяне на гаражите
        for garageId in car.garageIds:
            garage = db.query(Garage).filter(Garage.id == garageId).first()
            if garage:
                db_car.garages.append(garage)
    
    # Записване на колата в базата данни
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        return db_car
    
    
    @staticmethod
    def get_by_id(db: Session, carId: int):
        car = db.query(Car).filter(Car.id == carId).first()
        if not car:
            raise ValueError("Car not found.")
    
    # Използваме форматирането на отговор
        return format_car_response(car)

    @staticmethod
    def get_all(db: Session):
        return db.query(Car).all()

    @staticmethod
    def update(db: Session, carId: int, car_update: UpdateCarDTO):
        # Намиране на съществуващата кола
        db_car = db.query(Car).filter(Car.id == carId).first()
    
        if not db_car:
            return None  # Ако колата не съществува, върни None или можеш да хвърлиш грешка

    # Актуализиране на атрибутите на колата
        db_car.make = car_update.make
        db_car.model = car_update.model
        db_car.productionYear = car_update.productionYear
        db_car.licensePlate = car_update.licensePlate
    
    # Премахване на текущите гаражи и добавяне на нови
        db_car.garages = []  # Изчистване на старите гаражи
        for garageId in car_update.garage_ids:
            garage = db.query(Garage).filter(Garage.id == garageId).first()
            if garage:
                db_car.garages.append(garage)  # Добавяне на новите гаражи

    # Записване на промените в базата данни
        db.commit()
        db.refresh(db_car)

        return db_car

    @staticmethod
    def delete(db: Session, car: Car):
        db.delete(car)
        db.commit()
from sqlalchemy.orm import Session
from app.models.car_model import Car
from app.models.garage_model import Garage
from app.schemas.car_schemas import CreateCarDTO, UpdateCarDTO
from sqlalchemy.orm import joinedload
from app.services.car_service import format_car_response

class CarRepository:
    @staticmethod
    def create(db: Session, car: CreateCarDTO):
        
        db_car = Car(
            make=car.make,
            model=car.model,
            productionYear=car.productionYear,
            licensePlate=car.licensePlate
    )
    
    
        for garageId in car.garageIds:
            garage = db.query(Garage).filter(Garage.id == garageId).first()
            if garage:
                db_car.garages.append(garage)
    
    
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        return db_car
    
    
    @staticmethod
    def get_by_id(db: Session, carId: int):
        car = db.query(Car).filter(Car.id == carId).first()
        if not car:
            raise ValueError("Car not found.")
    
    
        return format_car_response(car)

    @staticmethod
    def get_all(db: Session):
        return db.query(Car).all()

    @staticmethod
    def update(db: Session, carId: int, car_update: UpdateCarDTO):
        
        db_car = db.query(Car).filter(Car.id == carId).first()
    
        if not db_car:
            return None  

    
        db_car.make = car_update.make
        db_car.model = car_update.model
        db_car.productionYear = car_update.productionYear
        db_car.licensePlate = car_update.licensePlate
    
    
        db_car.garages = []  
        for garageId in car_update.garageIds:
            garage = db.query(Garage).filter(Garage.id == garageId).first()
            if garage:
                db_car.garages.append(garage)  

    
        db.commit()
        db.refresh(db_car)

        return db_car

    @staticmethod
    def delete(db: Session, car: Car):
        db.delete(car)
        db.commit()
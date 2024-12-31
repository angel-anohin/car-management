from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.car_schemas import CreateCarDTO, UpdateCarDTO, ResponseCarDTO, CarWithGarages
from app.repositories.car_repository import CarRepository
from app.database import get_db
from app.models.car_model import Car

router = APIRouter()

@router.post("/", response_model=ResponseCarDTO)
def create_car(car: CreateCarDTO, db: Session = Depends(get_db)):
    return CarRepository.create(db=db, car=car)

@router.get("/{carId}", response_model=ResponseCarDTO)
def get_car(carId: int, db: Session = Depends(get_db)):
    return db.query(Car).filter(Car.id == carId).first()

@router.get("/", response_model=list[ResponseCarDTO])
def get_cars(db: Session = Depends(get_db)):
    return CarRepository.get_all(db)

@router.put("/cars/{carId}", response_model=CarWithGarages)
def update_car(carId: int, car_update: UpdateCarDTO, db: Session = Depends(get_db)):
    updated_car = CarRepository.update(db=db, carId=carId, car_update=car_update)
    
    if not updated_car:
        raise HTTPException(status_code=404, detail="Car not found")

    return updated_car

@router.delete("/{carId}", status_code=204)
def delete_car(carId: int, db: Session = Depends(get_db)):
    car = CarRepository.get_by_id(db, carId)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    CarRepository.delete(db, car)
    return {"message": "Car deleted"}

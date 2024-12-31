from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.garage_schemas import CreateGarageDTO, UpdateGarageDTO, ResponseGarageDTO, Garage
from app.repositories.garage_repository import GarageRepository
from app.database import get_db
from app.models.garage_model import Garage

router = APIRouter()

@router.post("/", response_model=ResponseGarageDTO)
def create_garage(garage: CreateGarageDTO, db: Session = Depends(get_db)):
    new_garage = Garage(**garage.dict())
    return GarageRepository.create(db, new_garage)

@router.get("/{garageId}", response_model=ResponseGarageDTO)
def get_garage(garageId: int, db: Session = Depends(get_db)):
    garage = GarageRepository.get_by_id(db, garageId)
    if not garage:
        raise HTTPException(status_code=404, detail="Garage not found")
    return garage

@router.get("/", response_model=list[ResponseGarageDTO])
def get_garages(db: Session = Depends(get_db)):
    return GarageRepository.get_all(db)

@router.put("/{garageId}", response_model=ResponseGarageDTO)
def update_garage(garageId: int, garage: UpdateGarageDTO, db: Session = Depends(get_db)):
    existing_garage = GarageRepository.get_by_id(db, garageId)
    if not existing_garage:
        raise HTTPException(status_code=404, detail="Garage not found")
    for key, value in garage.dict().items():
        setattr(existing_garage, key, value)
    return GarageRepository.update(db, existing_garage)

@router.delete("/{garageId}", status_code=204)
def delete_garage(garageId: int, db: Session = Depends(get_db)):
    garage = GarageRepository.get_by_id(db, garageId)
    if not garage:
        raise HTTPException(status_code=404, detail="Garage not found")
    GarageRepository.delete(db, garage)
    return {"message": "Garage deleted"}



@router.get("/garages", response_model=List[ResponseGarageDTO])
def filter_garages_by_city(city: str, db: Session = Depends(get_db)):
    # Извикваме функцията за търсене на гаражи по град
    garages = GarageRepository.get_garages_by_city(db=db, city=city)
    
    if not garages:
        raise HTTPException(status_code=404, detail="No garages found in this city")
    
    return garages

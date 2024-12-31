from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.maintenance_schemas import CreateMaintenanceDTO, UpdateMaintenanceDTO, ResponseMaintenanceDTO
from app.repositories.maintenance_repository import MaintenanceRepository
from app.database import get_db
from app.models.maintenance_model import Maintenance

router = APIRouter()

@router.post("/maintenance", response_model=CreateMaintenanceDTO)
def create_maintenance(maintenance: CreateMaintenanceDTO, db: Session = Depends(get_db)):
    db_car = MaintenanceRepository.get_car_by_id(db=db, carId=maintenance.carId)  
    db_garage = MaintenanceRepository.get_garage_by_id(db=db, garageId=maintenance.garageId)  

    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    if not db_garage:
        raise HTTPException(status_code=404, detail="Garage not found")

    db_maintenance = MaintenanceRepository.create_maintenance(db=db, maintenance=maintenance)
    return db_maintenance

@router.get("/{maintenance_id}", response_model=ResponseMaintenanceDTO)
def get_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    maintenance = MaintenanceRepository.get_by_id(db, maintenance_id)
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return maintenance

@router.get("/", response_model=list[ResponseMaintenanceDTO])
def get_maintenances(db: Session = Depends(get_db)):
    return MaintenanceRepository.get_all(db)

@router.put("/{maintenance_id}", response_model=ResponseMaintenanceDTO)
def update_maintenance(maintenance_id: int, maintenance: UpdateMaintenanceDTO, db: Session = Depends(get_db)):
    existing_maintenance = MaintenanceRepository.get_by_id(db, maintenance_id)
    if not existing_maintenance:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    for key, value in maintenance.dict().items():
        setattr(existing_maintenance, key, value)
    return MaintenanceRepository.update(db, existing_maintenance)

@router.delete("/{maintenance_id}", status_code=204)
def delete_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    maintenance = MaintenanceRepository.get_by_id(db, maintenance_id)
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    MaintenanceRepository.delete(db, maintenance)
    return {"message": "Maintenance deleted"}

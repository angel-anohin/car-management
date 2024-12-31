from pydantic import BaseModel
from datetime import date

class CreateMaintenanceDTO(BaseModel):
    garageId: int
    carId: int
    serviceType: str
    scheduledDate: date

class UpdateMaintenanceDTO(BaseModel):
    carId: int
    serviceType: str
    scheduledDate: date
    garageId: int

class ResponseMaintenanceDTO(BaseModel):
    id: int
    carId: int
    carName: str
    serviceType: str
    scheduledDate: date
    garageId: int
    garageName: str

    class Config:
        orm_mode = True
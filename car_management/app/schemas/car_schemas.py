from pydantic import BaseModel
from typing import List

from app.schemas.garage_schemas import ResponseGarageDTO, GarageBase

class CarBase(BaseModel):
    id: int
    make: str
    model: str
    productionYear: int
    licensePlate: str

    class Config:
        orm_mode = True

class CreateCarDTO(BaseModel):
    make: str
    model: str
    productionYear: int
    licensePlate: str
    garageIds: List[int]
    
    
class CarWithGarages(CarBase):
    garages: List[GarageBase]  

    class Config:
        orm_mode = True    

class UpdateCarDTO(BaseModel):
    make: str
    model: str
    productionYear: int
    licensePlate: str
    garageIds: List[int]

class ResponseCarDTO(BaseModel):
    id: int
    make: str
    model: str
    productionYear: int
    licensePlate: str
    garages: List[ResponseGarageDTO]

    class Config:
        orm_mode = True
# app/schemas/garage_schemas.py
from pydantic import BaseModel


class GarageBase(BaseModel):
    id: int
    name: str
    location: str
    city: str
    capacity: int

    class Config:
        orm_mode = True  # Позволява на Pydantic да работи с ORM модели
        
class CreateGarageDTO(BaseModel):
    name: str
    location: str
    city: str
    capacity: int

class UpdateGarageDTO(BaseModel):
    name: str
    location: str
    city: str
    capacity: int

class ResponseGarageDTO(BaseModel):
    id: int
    name: str
    location: str
    city: str
    capacity: int

    class Config:
        orm_mode = True


class Garage(BaseModel):
    id: int
    name: str
    location: str
    city: str
    capacity: int

    class Config:
        orm_mode = True
# app/main.py
from fastapi import FastAPI
from app.routers import garages, cars, maintenances
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можете да зададете конкретни домейни
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(garages.router, prefix="/garages", tags=["Garages"])
app.include_router(cars.router, prefix="/cars", tags=["Cars"])
app.include_router(maintenances.router, prefix="/maintenances", tags=["Maintenances"])

@app.get("/")
def root():
    return {"message": "Car Management API is running"}